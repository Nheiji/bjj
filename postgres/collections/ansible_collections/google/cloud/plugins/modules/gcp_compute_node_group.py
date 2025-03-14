#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    Type: MMv1     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_node_group
description:
- Represents a NodeGroup resource to manage a group of sole-tenant nodes.
short_description: Creates a GCP NodeGroup
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  description:
    description:
    - An optional textual description of the resource.
    required: false
    type: str
  name:
    description:
    - Name of the resource.
    required: false
    type: str
  node_template:
    description:
    - The URL of the node template to which this node group belongs.
    - 'This field represents a link to a NodeTemplate resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''selfLink'' and value
      of your resource''s selfLink Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_node_template task and then set this node_template field to
      "{{ name-of-resource }}"'
    required: true
    type: dict
  size:
    description:
    - The total number of nodes in the node group.
    required: true
    type: int
  maintenance_policy:
    description:
    - 'Specifies how to handle instances when a node in the group undergoes maintenance.
      Set to one of: DEFAULT, RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The
      default value is DEFAULT.'
    required: false
    default: DEFAULT
    type: str
  maintenance_window:
    description:
    - contains properties for the timeframe of maintenance .
    required: false
    type: dict
    suboptions:
      start_time:
        description:
        - instances.start time of the window. This must be in UTC format that resolves
          to one of 00:00, 04:00, 08:00, 12:00, 16:00, or 20:00. For example, both
          13:00-5 and 08:00 are valid.
        required: true
        type: str
  autoscaling_policy:
    description:
    - If you use sole-tenant nodes for your workloads, you can use the node group
      autoscaler to automatically manage the sizes of your node groups.
    required: false
    type: dict
    suboptions:
      mode:
        description:
        - 'The autoscaling mode. Set to one of the following: - OFF: Disables the
          autoscaler.'
        - "- ON: Enables scaling in and scaling out."
        - "- ONLY_SCALE_OUT: Enables only scaling out."
        - You must use this mode if your node groups are configured to restart their
          hosted VMs on minimal servers.
        - 'Some valid choices include: "OFF", "ON", "ONLY_SCALE_OUT"'
        required: true
        type: str
      min_nodes:
        description:
        - Minimum size of the node group. Must be less than or equal to max-nodes.
          The default value is 0.
        required: false
        type: int
      max_nodes:
        description:
        - Maximum size of the node group. Set to a value less than or equal to 100
          and greater than or equal to min-nodes.
        required: true
        type: int
  zone:
    description:
    - Zone where this node group is located .
    required: true
    type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
    - accesstoken
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  access_token:
    description:
    - An OAuth2 access token if credential type is accesstoken.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups)'
- 'Sole-Tenant Nodes: U(https://cloud.google.com/compute/docs/nodes/)'
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set access_token using the C(GCP_ACCESS_TOKEN)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a node template
  google.cloud.gcp_compute_node_template:
    name: "{{ resource_name }}"
    region: us-central1
    node_type: n1-node-96-624
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: node_template

- name: create a node group
  google.cloud.gcp_compute_node_group:
    name: test_object
    zone: us-central1-a
    description: example group for ansible
    size: 1
    node_template: "{{ node_template }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional textual description of the resource.
  returned: success
  type: str
name:
  description:
  - Name of the resource.
  returned: success
  type: str
nodeTemplate:
  description:
  - The URL of the node template to which this node group belongs.
  returned: success
  type: dict
size:
  description:
  - The total number of nodes in the node group.
  returned: success
  type: int
maintenancePolicy:
  description:
  - 'Specifies how to handle instances when a node in the group undergoes maintenance.
    Set to one of: DEFAULT, RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default
    value is DEFAULT.'
  returned: success
  type: str
maintenanceWindow:
  description:
  - contains properties for the timeframe of maintenance .
  returned: success
  type: complex
  contains:
    startTime:
      description:
      - instances.start time of the window. This must be in UTC format that resolves
        to one of 00:00, 04:00, 08:00, 12:00, 16:00, or 20:00. For example, both 13:00-5
        and 08:00 are valid.
      returned: success
      type: str
autoscalingPolicy:
  description:
  - If you use sole-tenant nodes for your workloads, you can use the node group autoscaler
    to automatically manage the sizes of your node groups.
  returned: success
  type: complex
  contains:
    mode:
      description:
      - 'The autoscaling mode. Set to one of the following: - OFF: Disables the autoscaler.'
      - "- ON: Enables scaling in and scaling out."
      - "- ONLY_SCALE_OUT: Enables only scaling out."
      - You must use this mode if your node groups are configured to restart their
        hosted VMs on minimal servers.
      returned: success
      type: str
    minNodes:
      description:
      - Minimum size of the node group. Must be less than or equal to max-nodes. The
        default value is 0.
      returned: success
      type: int
    maxNodes:
      description:
      - Maximum size of the node group. Set to a value less than or equal to 100 and
        greater than or equal to min-nodes.
      returned: success
      type: int
zone:
  description:
  - Zone where this node group is located .
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import (
    navigate_hash,
    GcpSession,
    GcpModule,
    GcpRequest,
    remove_nones_from_dict,
    replace_resource_dict,
)
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(type='str'),
            name=dict(type='str'),
            node_template=dict(required=True, type='dict'),
            size=dict(required=True, type='int'),
            maintenance_policy=dict(default='DEFAULT', type='str'),
            maintenance_window=dict(type='dict', options=dict(start_time=dict(required=True, type='str'))),
            autoscaling_policy=dict(
                type='dict', options=dict(mode=dict(required=True, type='str'), min_nodes=dict(type='int'), max_nodes=dict(required=True, type='int'))
            ),
            zone=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#NodeGroup'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind, fetch)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, create_link(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind, fetch):
    update_fields(module, resource_to_request(module), response_to_hash(module, fetch))
    return fetch_resource(module, self_link(module), kind)


def update_fields(module, request, response):
    if response.get('nodeTemplate') != request.get('nodeTemplate'):
        node_template_update(module, request, response)


def node_template_update(module, request, response):
    auth = GcpSession(module, 'compute')
    auth.post(
        ''.join(["https://compute.googleapis.com/compute/v1/", "projects/{project}/zones/{zone}/nodeGroups/{name}/setNodeTemplate"]).format(**module.params),
        {u'nodeTemplate': replace_resource_dict(module.params.get(u'node_template', {}), 'selfLink')},
    )


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#NodeGroup',
        u'description': module.params.get('description'),
        u'name': module.params.get('name'),
        u'nodeTemplate': replace_resource_dict(module.params.get(u'node_template', {}), 'selfLink'),
        u'size': module.params.get('size'),
        u'maintenancePolicy': module.params.get('maintenance_policy'),
        u'maintenanceWindow': NodeGroupMaintenancewindow(module.params.get('maintenance_window', {}), module).to_request(),
        u'autoscalingPolicy': NodeGroupAutoscalingpolicy(module.params.get('autoscaling_policy', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/nodeGroups/{name}".format(**module.params)


def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/nodeGroups".format(**module.params)


def create_link(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/nodeGroups?initialNodeCount={size}".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'name': response.get(u'name'),
        u'nodeTemplate': response.get(u'nodeTemplate'),
        u'size': module.params.get('size'),
        u'maintenancePolicy': response.get(u'maintenancePolicy'),
        u'maintenanceWindow': NodeGroupMaintenancewindow(response.get(u'maintenanceWindow', {}), module).from_response(),
        u'autoscalingPolicy': NodeGroupAutoscalingpolicy(response.get(u'autoscalingPolicy', {}), module).from_response(),
    }


def region_selflink(name, params):
    if name is None:
        return
    url = r"https://compute.googleapis.com/compute/v1/projects/.*/regions/.*"
    if not re.match(url, name):
        name = "https://compute.googleapis.com/compute/v1/projects/{project}/regions/%s".format(**params) % name
    return name


def zone_selflink(name, params):
    if name is None:
        return
    url = r"https://compute.googleapis.com/compute/v1/projects/.*/zones/.*"
    if not re.match(url, name):
        name = "https://compute.googleapis.com/compute/v1/projects/{project}/zones/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#NodeGroup')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class NodeGroupMaintenancewindow(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'startTime': self.request.get('start_time')})

    def from_response(self):
        return remove_nones_from_dict({u'startTime': self.request.get(u'startTime')})


class NodeGroupAutoscalingpolicy(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {u'mode': self.request.get('mode'), u'minNodes': self.request.get('min_nodes'), u'maxNodes': self.request.get('max_nodes')}
        )

    def from_response(self):
        return remove_nones_from_dict(
            {u'mode': self.request.get(u'mode'), u'minNodes': self.request.get(u'minNodes'), u'maxNodes': self.request.get(u'maxNodes')}
        )


if __name__ == '__main__':
    main()
