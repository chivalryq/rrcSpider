# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"\x8f\x01\n\x03\x43\x61r\x12\x1b\n\x0eoriginal_price\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1f\n\x12register_timestamp\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07mileage\x18\x03 \x01(\x02H\x02\x88\x01\x01\x42\x11\n\x0f_original_priceB\x15\n\x13_register_timestampB\n\n\x08_mileage\"/\n\rPredictOneReq\x12\x16\n\x03\x63\x61r\x18\x01 \x01(\x0b\x32\x04.CarH\x00\x88\x01\x01\x42\x06\n\x04_car\"-\n\rPredictOneRsp\x12\x12\n\x05price\x18\x01 \x01(\x02H\x00\x88\x01\x01\x42\x08\n\x06_price2>\n\x0cPricePredict\x12.\n\nPredictOne\x12\x0e.PredictOneReq\x1a\x0e.PredictOneRsp\"\x00\x62\x06proto3'
)




_CAR = _descriptor.Descriptor(
  name='Car',
  full_name='Car',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_price', full_name='Car.original_price', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='register_timestamp', full_name='Car.register_timestamp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mileage', full_name='Car.mileage', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_original_price', full_name='Car._original_price',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_register_timestamp', full_name='Car._register_timestamp',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_mileage', full_name='Car._mileage',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=18,
  serialized_end=161,
)


_PREDICTONEREQ = _descriptor.Descriptor(
  name='PredictOneReq',
  full_name='PredictOneReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='car', full_name='PredictOneReq.car', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_car', full_name='PredictOneReq._car',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=163,
  serialized_end=210,
)


_PREDICTONERSP = _descriptor.Descriptor(
  name='PredictOneRsp',
  full_name='PredictOneRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='PredictOneRsp.price', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_price', full_name='PredictOneRsp._price',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=212,
  serialized_end=257,
)

_CAR.oneofs_by_name['_original_price'].fields.append(
  _CAR.fields_by_name['original_price'])
_CAR.fields_by_name['original_price'].containing_oneof = _CAR.oneofs_by_name['_original_price']
_CAR.oneofs_by_name['_register_timestamp'].fields.append(
  _CAR.fields_by_name['register_timestamp'])
_CAR.fields_by_name['register_timestamp'].containing_oneof = _CAR.oneofs_by_name['_register_timestamp']
_CAR.oneofs_by_name['_mileage'].fields.append(
  _CAR.fields_by_name['mileage'])
_CAR.fields_by_name['mileage'].containing_oneof = _CAR.oneofs_by_name['_mileage']
_PREDICTONEREQ.fields_by_name['car'].message_type = _CAR
_PREDICTONEREQ.oneofs_by_name['_car'].fields.append(
  _PREDICTONEREQ.fields_by_name['car'])
_PREDICTONEREQ.fields_by_name['car'].containing_oneof = _PREDICTONEREQ.oneofs_by_name['_car']
_PREDICTONERSP.oneofs_by_name['_price'].fields.append(
  _PREDICTONERSP.fields_by_name['price'])
_PREDICTONERSP.fields_by_name['price'].containing_oneof = _PREDICTONERSP.oneofs_by_name['_price']
DESCRIPTOR.message_types_by_name['Car'] = _CAR
DESCRIPTOR.message_types_by_name['PredictOneReq'] = _PREDICTONEREQ
DESCRIPTOR.message_types_by_name['PredictOneRsp'] = _PREDICTONERSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Car = _reflection.GeneratedProtocolMessageType('Car', (_message.Message,), {
  'DESCRIPTOR' : _CAR,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Car)
  })
_sym_db.RegisterMessage(Car)

PredictOneReq = _reflection.GeneratedProtocolMessageType('PredictOneReq', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTONEREQ,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:PredictOneReq)
  })
_sym_db.RegisterMessage(PredictOneReq)

PredictOneRsp = _reflection.GeneratedProtocolMessageType('PredictOneRsp', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTONERSP,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:PredictOneRsp)
  })
_sym_db.RegisterMessage(PredictOneRsp)



_PRICEPREDICT = _descriptor.ServiceDescriptor(
  name='PricePredict',
  full_name='PricePredict',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=259,
  serialized_end=321,
  methods=[
  _descriptor.MethodDescriptor(
    name='PredictOne',
    full_name='PricePredict.PredictOne',
    index=0,
    containing_service=None,
    input_type=_PREDICTONEREQ,
    output_type=_PREDICTONERSP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRICEPREDICT)

DESCRIPTOR.services_by_name['PricePredict'] = _PRICEPREDICT

# @@protoc_insertion_point(module_scope)