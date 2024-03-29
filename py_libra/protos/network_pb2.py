# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='network.proto',
  package='network',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rnetwork.proto\x12\x07network\"(\n\x08PeerInfo\x12\r\n\x05\x61\x64\x64rs\x18\x01 \x03(\x0c\x12\r\n\x05\x65poch\x18\x02 \x01(\x04\"=\n\x04Note\x12\x0f\n\x07peer_id\x18\x01 \x01(\x0c\x12\x11\n\tpeer_info\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\",\n\x0c\x44iscoveryMsg\x12\x1c\n\x05notes\x18\x01 \x03(\x0b\x32\r.network.Note\";\n\x0bIdentityMsg\x12\x0f\n\x07peer_id\x18\x01 \x01(\x0c\x12\x1b\n\x13supported_protocols\x18\x02 \x03(\x0c\"\x06\n\x04Ping\"\x06\n\x04Pongb\x06proto3')
)




_PEERINFO = _descriptor.Descriptor(
  name='PeerInfo',
  full_name='network.PeerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addrs', full_name='network.PeerInfo.addrs', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='network.PeerInfo.epoch', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=26,
  serialized_end=66,
)


_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='network.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer_id', full_name='network.Note.peer_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer_info', full_name='network.Note.peer_info', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='network.Note.signature', index=2,
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
  serialized_start=68,
  serialized_end=129,
)


_DISCOVERYMSG = _descriptor.Descriptor(
  name='DiscoveryMsg',
  full_name='network.DiscoveryMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notes', full_name='network.DiscoveryMsg.notes', index=0,
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
  serialized_start=131,
  serialized_end=175,
)


_IDENTITYMSG = _descriptor.Descriptor(
  name='IdentityMsg',
  full_name='network.IdentityMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer_id', full_name='network.IdentityMsg.peer_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supported_protocols', full_name='network.IdentityMsg.supported_protocols', index=1,
      number=2, type=12, cpp_type=9, label=3,
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
  serialized_start=177,
  serialized_end=236,
)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='network.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=238,
  serialized_end=244,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='network.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=246,
  serialized_end=252,
)

_DISCOVERYMSG.fields_by_name['notes'].message_type = _NOTE
DESCRIPTOR.message_types_by_name['PeerInfo'] = _PEERINFO
DESCRIPTOR.message_types_by_name['Note'] = _NOTE
DESCRIPTOR.message_types_by_name['DiscoveryMsg'] = _DISCOVERYMSG
DESCRIPTOR.message_types_by_name['IdentityMsg'] = _IDENTITYMSG
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PeerInfo = _reflection.GeneratedProtocolMessageType('PeerInfo', (_message.Message,), dict(
  DESCRIPTOR = _PEERINFO,
  __module__ = 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.PeerInfo)
  ))
_sym_db.RegisterMessage(PeerInfo)

Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), dict(
  DESCRIPTOR = _NOTE,
  __module__ = 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.Note)
  ))
_sym_db.RegisterMessage(Note)

DiscoveryMsg = _reflection.GeneratedProtocolMessageType('DiscoveryMsg', (_message.Message,), dict(
  DESCRIPTOR = _DISCOVERYMSG,
  __module__ = 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.DiscoveryMsg)
  ))
_sym_db.RegisterMessage(DiscoveryMsg)

IdentityMsg = _reflection.GeneratedProtocolMessageType('IdentityMsg', (_message.Message,), dict(
  DESCRIPTOR = _IDENTITYMSG,
  __module__ = 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.IdentityMsg)
  ))
_sym_db.RegisterMessage(IdentityMsg)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.Ping)
  ))
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), dict(
  DESCRIPTOR = _PONG,
  __module__ = 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.Pong)
  ))
_sym_db.RegisterMessage(Pong)


# @@protoc_insertion_point(module_scope)
