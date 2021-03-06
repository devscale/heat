# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

PARAM_KEYS = (PARAM_TIMEOUT, ) = ('timeout_mins', )

STACK_KEYS = (
    STACK_NAME, STACK_ID,
    STACK_CREATION_TIME, STACK_UPDATED_TIME, STACK_DELETION_TIME,
    STACK_NOTIFICATION_TOPICS,
    STACK_DESCRIPTION, STACK_TMPL_DESCRIPTION,
    STACK_PARAMETERS, STACK_OUTPUTS,
    STACK_STATUS, STACK_STATUS_DATA, STACK_CAPABILITIES,
    STACK_DISABLE_ROLLBACK, STACK_TIMEOUT,
) = (
    'stack_name', 'stack_identity',
    'creation_time', 'updated_time', 'deletion_time',
    'notification_topics',
    'description', 'template_description',
    'parameters', 'outputs',
    'stack_status', 'stack_status_reason', 'capabilities',
    'disable_rollback', 'timeout_mins'
)

STACK_OUTPUT_KEYS = (
    OUTPUT_DESCRIPTION,
    OUTPUT_KEY, OUTPUT_VALUE,
) = (
    'description',
    'output_key', 'output_value',
)

RES_KEYS = (
    RES_DESCRIPTION, RES_UPDATED_TIME,
    RES_NAME, RES_PHYSICAL_ID, RES_METADATA,
    RES_STATUS, RES_STATUS_DATA, RES_TYPE,
    RES_ID, RES_STACK_ID, RES_STACK_NAME,
) = (
    'description', 'updated_time',
    'logical_resource_id', 'physical_resource_id', 'metadata',
    'resource_status', 'resource_status_reason', 'resource_type',
    'resource_identity', STACK_ID, STACK_NAME,
)

EVENT_KEYS = (
    EVENT_ID,
    EVENT_STACK_ID, EVENT_STACK_NAME,
    EVENT_TIMESTAMP,
    EVENT_RES_NAME, EVENT_RES_PHYSICAL_ID,
    EVENT_RES_STATUS, EVENT_RES_STATUS_DATA, EVENT_RES_TYPE,
    EVENT_RES_PROPERTIES,
) = (
    'event_identity',
    STACK_ID, STACK_NAME,
    "event_time",
    RES_NAME, RES_PHYSICAL_ID,
    RES_STATUS, RES_STATUS_DATA, RES_TYPE,
    'resource_properties',
)

# This is the representation of a watch we expose to the API via RPC
WATCH_KEYS = (
    WATCH_ACTIONS_ENABLED, WATCH_ALARM_ACTIONS, WATCH_TOPIC,
    WATCH_UPDATED_TIME, WATCH_DESCRIPTION, WATCH_NAME,
    WATCH_COMPARISON, WATCH_DIMENSIONS, WATCH_PERIODS,
    WATCH_INSUFFICIENT_ACTIONS, WATCH_METRIC_NAME, WATCH_NAMESPACE,
    WATCH_OK_ACTIONS, WATCH_PERIOD, WATCH_STATE_REASON,
    WATCH_STATE_REASON_DATA, WATCH_STATE_UPDATED_TIME, WATCH_STATE_VALUE,
    WATCH_STATISTIC, WATCH_THRESHOLD, WATCH_UNIT, WATCH_STACK_ID
) = (
    'actions_enabled', 'actions', 'topic',
    'updated_time', 'description', 'name',
    'comparison', 'dimensions', 'periods',
    'insufficient_actions', 'metric_name', 'namespace',
    'ok_actions', 'period', 'state_reason',
    'state_reason_data', 'state_updated_time', 'state_value',
    'statistic', 'threshold', 'unit', 'stack_id')

# Alternate representation of a watch rule to align with DB format
# FIXME : These align with AWS naming for compatibility with the
# current cfn-push-stats & metadata server, fix when we've ported
# cfn-push-stats to use the Cloudwatch server and/or moved metric
# collection into ceilometer, these should just be WATCH_KEYS
# or each field should be stored separately in the DB watch_data
# table if we stick to storing watch data in the heat DB
WATCH_RULE_KEYS = (
    RULE_ACTIONS_ENABLED, RULE_ALARM_ACTIONS, RULE_TOPIC,
    RULE_UPDATED_TIME, RULE_DESCRIPTION, RULE_NAME,
    RULE_COMPARISON, RULE_DIMENSIONS, RULE_PERIODS,
    RULE_INSUFFICIENT_ACTIONS, RULE_METRIC_NAME, RULE_NAMESPACE,
    RULE_OK_ACTIONS, RULE_PERIOD, RULE_STATE_REASON,
    RULE_STATE_REASON_DATA, RULE_STATE_UPDATED_TIME, RULE_STATE_VALUE,
    RULE_STATISTIC, RULE_THRESHOLD, RULE_UNIT, RULE_STACK_NAME
) = (
    'ActionsEnabled', 'AlarmActions', 'AlarmArn',
    'AlarmConfigurationUpdatedTimestamp', 'AlarmDescription', 'AlarmName',
    'ComparisonOperator', 'Dimensions', 'EvaluationPeriods',
    'InsufficientDataActions', 'MetricName', 'Namespace',
    'OKActions', 'Period', 'StateReason',
    'StateReasonData', 'StateUpdatedTimestamp', 'StateValue',
    'Statistic', 'Threshold', 'Unit', 'StackName')

WATCH_STATES = (
    WATCH_STATE_OK, WATCH_STATE_ALARM, WATCH_STATE_NODATA
) = (
    'NORMAL', 'ALARM', 'NODATA',
)

WATCH_DATA_KEYS = (
    WATCH_DATA_ALARM, WATCH_DATA_METRIC, WATCH_DATA_TIME,
    WATCH_DATA_NAMESPACE, WATCH_DATA
) = (
    'watch_name', 'metric_name', 'timestamp',
    'namespace', 'data'
)
