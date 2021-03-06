#!/bin/bash

BASE_DIR=`dirname $0`

function usage {
    echo "Usage: $0 [OPTION]..."
    echo "Run Heat's test suite(s)"
    echo ""
    echo "  -V, --virtual-env        Use virtualenv.  Install automatically if not present."
    echo "                           (Default is to run tests in local environment)"
    echo "  -F, --force              Force a clean re-build of the virtual environment. Useful when dependencies have been added."
    echo "  -f, --func               Run functional tests"
    echo "  -u, --unit               Run unit tests (default when nothing specified)"
    echo "  -p, --pep8               Run pep8 tests"
    echo "  --all                    Run all tests"
    echo "  -c, --coverage           Generate coverage report (selects --unit)"
    echo "  -h, --help               Print this usage message"
    exit
}

# must not assign -a as an option, needed for selecting custom attributes
no_venv=1
function process_option {
    case "$1" in
        -V|--virtual-env) no_venv=0;;
        -F|--force) force=1;;
        -f|--func) test_func=1; noseargs="$noseargs -a tag=func";;
        -u|--unit) test_unit=1; noseargs="$noseargs -a tag=unit";;
        -p|--pep8) test_pep8=1;;
        --all) test_func=1; test_unit=1; test_pep8=1; noseargs="$noseargs -a tag=func -a tag=unit";;
        -c|--coverage) coverage=1; test_unit=1; noseargs="$noseargs -a tag=unit";;
        -h|--help) usage;;
        *) noseargs="$noseargs $1"
    esac
}

venv=.venv
with_venv=tools/with_venv.sh
wrapper=""

function run_tests {
    echo 'Running tests'
    NOSETESTS="python heat/testing/runner.py $noseopts $noseargs"
    # Just run the test suites in current environment
    ${wrapper} $NOSETESTS 2> run_tests.err.log
}

function run_pep8 {
    # Check the installed pep8 matches what is in the tox.ini,
    # so the local test matches the jenkins gate tests
    TOX_PEP_VERSION=$(grep "pep8==" $BASE_DIR/tox.ini | sed "s/.*pep8==//")
    INST_PEP_VERSION=$(pep8 --version 2>/dev/null)
    if [[ "$TOX_PEP_VERSION" != "$INST_PEP_VERSION" ]]; then
        if [[ -z "$INST_PEP_VERSION" ]]; then
            echo "ERROR pep8 is not installed, please install pep8 $TOX_PEP_VERSION" >&2
        else
            echo "ERROR installed version of pep8 $INST_PEP_VERSION"  >&2
            echo "does not match the required version in tox.ini ($TOX_PEP_VERSION)" >&2
            echo "please install the required version of pep8" >&2
        fi
        exit 1
    fi
    echo "Running pep8..."
    PEP8_OPTIONS="--exclude=$PEP8_EXCLUDE --repeat"
    PEP8_INCLUDE="bin/heat-cfn bin/heat-boto bin/heat-api-cfn bin/heat-api bin/heat-engine heat tools setup.py heat/testing/runner.py"
    ${wrapper} pep8 $PEP8_OPTIONS $PEP8_INCLUDE
}

# run unit tests with pep8 when no arguments are specified
# otherwise process CLI options
if [[ $# == 0 ]]; then
    noseargs="$noseargs -a tag=unit"
    test_pep8=1
else
    for arg in "$@"; do
        process_option $arg
    done
fi

# If enabled, tell nose to collect coverage data
if [ "$coverage" == 1 ]; then
    noseopts="$noseopts --with-coverage --cover-package=heat"
fi

if [ "$no_venv" == 0 ]
then
    # Remove the virtual environment if --force used
    if [ "$force" == 1 ]; then
        echo "Cleaning virtualenv..."
        rm -rf ${venv}
    fi
    if [ -e ${venv} ]; then
        wrapper="${with_venv}"
    else
        # Automatically install the virtualenv
        python tools/install_venv.py
        wrapper="${with_venv}"
    fi
fi

# Delete old coverage data from previous runs
if [ "$coverage" == 1 ]; then
    ${wrapper} coverage erase
fi

result=0

# If functional or unit tests have been selected, run them
if [ ! -z "$noseargs" ]; then
    run_tests
    result=$?
fi

# Run pep8 if it was selected
if [ "$test_pep8" == 1 ]; then
    run_pep8
fi

# Generate coverage report
if [ "$coverage" == 1 ]; then
    echo "Generating coverage report in covhtml/"
    # Don't compute coverage for common code, which is tested elsewhere
    ${wrapper} coverage html --include='heat/*' --omit='heat/openstack/common/*' -d covhtml -i
fi

exit $result
