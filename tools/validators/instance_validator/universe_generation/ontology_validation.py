# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Uses ontology universe to validate parsed instance data."""

from __future__ import print_function

def _validate_type(entity, universe):
  """Uses information from the generated ontology universe to validate
  an entity's type.

  Args:
    entity: parsed instance YAML file formatted as dictionary
    universe: ConfigUniverse generated from the ontology

  Returns:
    Throws Exceptions if entity type is invalid.
  """
  entity_type_str = str(entity['type'])
  type_parse = entity_type_str.split('/')

  if len(type_parse) != 2:
    print('type improperly formatted:', entity_type_str)
    return False

  namespace = type_parse[0]
  entity_type = type_parse[1]

  if universe.GetEntityTypeNamespace(namespace) is None:
    print('invalid namespace:', namespace)
    return False

  if universe.GetEntityType(namespace, entity_type) is None:
    print('invalid entity type:', entity_type)
    return False

  return True

def validate_entity(entity, universe):
  """Uses information from the generated ontology universe to validate an
  entity.

  Args:
    entity: parsed instance YAML file formatted as dictionary
    universe: ConfigUniverse generated from the ontology

  Returns:
    Throws Exceptions if entity is invalid.
  """
  return _validate_type(entity, universe)
