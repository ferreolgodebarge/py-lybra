# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import py_libra.protos.access_path_pb2 as access__path__pb2
import py_libra.protos.proof_pb2 as proof__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='events.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x65vents.proto\x12\x05types\x1a\x11\x61\x63\x63\x65ss_path.proto\x1a\x0bproof.proto\"\\\n\x05\x45vent\x12&\n\x0b\x61\x63\x63\x65ss_path\x18\x01 \x01(\x0b\x32\x11.types.AccessPath\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x04\x12\x12\n\nevent_data\x18\x03 \x01(\x0c\"\x81\x01\n\x0e\x45ventWithProof\x12\x1b\n\x13transaction_version\x18\x01 \x01(\x04\x12\x13\n\x0b\x65vent_index\x18\x02 \x01(\x04\x12\x1b\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x0c.types.Event\x12 \n\x05proof\x18\x04 \x01(\x0b\x32\x11.types.EventProof\"*\n\nEventsList\x12\x1c\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x0c.types.Event\"B\n\x11\x45ventsForVersions\x12-\n\x12\x65vents_for_version\x18\x01 \x03(\x0b\x32\x11.types.EventsListb\x06proto3')
  ,
  dependencies=[access__path__pb2.DESCRIPTOR,proof__pb2.DESCRIPTOR,])




_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='types.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_path', full_name='types.Event.access_path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='types.Event.sequence_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_data', full_name='types.Event.event_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=147,
)


_EVENTWITHPROOF = _descriptor.Descriptor(
  name='EventWithProof',
  full_name='types.EventWithProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_version', full_name='types.EventWithProof.transaction_version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_index', full_name='types.EventWithProof.event_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='types.EventWithProof.event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='types.EventWithProof.proof', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=279,
)


_EVENTSLIST = _descriptor.Descriptor(
  name='EventsList',
  full_name='types.EventsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='types.EventsList.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=323,
)


_EVENTSFORVERSIONS = _descriptor.Descriptor(
  name='EventsForVersions',
  full_name='types.EventsForVersions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events_for_version', full_name='types.EventsForVersions.events_for_version', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=391,
)

_EVENT.fields_by_name['access_path'].message_type = access__path__pb2._ACCESSPATH
_EVENTWITHPROOF.fields_by_name['event'].message_type = _EVENT
_EVENTWITHPROOF.fields_by_name['proof'].message_type = proof__pb2._EVENTPROOF
_EVENTSLIST.fields_by_name['events'].message_type = _EVENT
_EVENTSFORVERSIONS.fields_by_name['events_for_version'].message_type = _EVENTSLIST
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['EventWithProof'] = _EVENTWITHPROOF
DESCRIPTOR.message_types_by_name['EventsList'] = _EVENTSLIST
DESCRIPTOR.message_types_by_name['EventsForVersions'] = _EVENTSFORVERSIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'events_pb2'
  # @@protoc_insertion_point(class_scope:types.Event)
  ))
_sym_db.RegisterMessage(Event)

EventWithProof = _reflection.GeneratedProtocolMessageType('EventWithProof', (_message.Message,), dict(
  DESCRIPTOR = _EVENTWITHPROOF,
  __module__ = 'events_pb2'
  # @@protoc_insertion_point(class_scope:types.EventWithProof)
  ))
_sym_db.RegisterMessage(EventWithProof)

EventsList = _reflection.GeneratedProtocolMessageType('EventsList', (_message.Message,), dict(
  DESCRIPTOR = _EVENTSLIST,
  __module__ = 'events_pb2'
  # @@protoc_insertion_point(class_scope:types.EventsList)
  ))
_sym_db.RegisterMessage(EventsList)

EventsForVersions = _reflection.GeneratedProtocolMessageType('EventsForVersions', (_message.Message,), dict(
  DESCRIPTOR = _EVENTSFORVERSIONS,
  __module__ = 'events_pb2'
  # @@protoc_insertion_point(class_scope:types.EventsForVersions)
  ))
_sym_db.RegisterMessage(EventsForVersions)


# @@protoc_insertion_point(module_scope)