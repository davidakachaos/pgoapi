# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/camera_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import camera_target_pb2 as pogoprotos_dot_enums_dot_camera__target__pb2
from pogoprotos.enums import camera_interpolation_pb2 as pogoprotos_dot_enums_dot_camera__interpolation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/camera_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/settings/master/camera_settings.proto\x12\x1apogoprotos.settings.master\x1a$pogoprotos/enums/camera_target.proto\x1a+pogoprotos/enums/camera_interpolation.proto\"\xd7\x03\n\x0e\x43\x61meraSettings\x12\x13\n\x0bnext_camera\x18\x01 \x01(\t\x12<\n\rinterpolation\x18\x02 \x03(\x0e\x32%.pogoprotos.enums.CameraInterpolation\x12\x33\n\x0btarget_type\x18\x03 \x03(\x0e\x32\x1e.pogoprotos.enums.CameraTarget\x12\x15\n\rease_in_speed\x18\x04 \x03(\x02\x12\x16\n\x0e\x65\x61se_out_speed\x18\x05 \x03(\x02\x12\x18\n\x10\x64uration_seconds\x18\x06 \x03(\x02\x12\x14\n\x0cwait_seconds\x18\x07 \x03(\x02\x12\x1a\n\x12transition_seconds\x18\x08 \x03(\x02\x12\x14\n\x0c\x61ngle_degree\x18\t \x03(\x02\x12\x1b\n\x13\x61ngle_offset_degree\x18\n \x03(\x02\x12\x14\n\x0cpitch_degree\x18\x0b \x03(\x02\x12\x1b\n\x13pitch_offset_degree\x18\x0c \x03(\x02\x12\x13\n\x0broll_degree\x18\r \x03(\x02\x12\x17\n\x0f\x64istance_meters\x18\x0e \x03(\x02\x12\x16\n\x0eheight_percent\x18\x0f \x03(\x02\x12\x16\n\x0evert_ctr_ratio\x18\x10 \x03(\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_camera__target__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_camera__interpolation__pb2.DESCRIPTOR,])




_CAMERASETTINGS = _descriptor.Descriptor(
  name='CameraSettings',
  full_name='pogoprotos.settings.master.CameraSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_camera', full_name='pogoprotos.settings.master.CameraSettings.next_camera', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interpolation', full_name='pogoprotos.settings.master.CameraSettings.interpolation', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_type', full_name='pogoprotos.settings.master.CameraSettings.target_type', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ease_in_speed', full_name='pogoprotos.settings.master.CameraSettings.ease_in_speed', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ease_out_speed', full_name='pogoprotos.settings.master.CameraSettings.ease_out_speed', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_seconds', full_name='pogoprotos.settings.master.CameraSettings.duration_seconds', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wait_seconds', full_name='pogoprotos.settings.master.CameraSettings.wait_seconds', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transition_seconds', full_name='pogoprotos.settings.master.CameraSettings.transition_seconds', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_degree', full_name='pogoprotos.settings.master.CameraSettings.angle_degree', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_offset_degree', full_name='pogoprotos.settings.master.CameraSettings.angle_offset_degree', index=9,
      number=10, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pitch_degree', full_name='pogoprotos.settings.master.CameraSettings.pitch_degree', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pitch_offset_degree', full_name='pogoprotos.settings.master.CameraSettings.pitch_offset_degree', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roll_degree', full_name='pogoprotos.settings.master.CameraSettings.roll_degree', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance_meters', full_name='pogoprotos.settings.master.CameraSettings.distance_meters', index=13,
      number=14, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_percent', full_name='pogoprotos.settings.master.CameraSettings.height_percent', index=14,
      number=15, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vert_ctr_ratio', full_name='pogoprotos.settings.master.CameraSettings.vert_ctr_ratio', index=15,
      number=16, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=635,
)

_CAMERASETTINGS.fields_by_name['interpolation'].enum_type = pogoprotos_dot_enums_dot_camera__interpolation__pb2._CAMERAINTERPOLATION
_CAMERASETTINGS.fields_by_name['target_type'].enum_type = pogoprotos_dot_enums_dot_camera__target__pb2._CAMERATARGET
DESCRIPTOR.message_types_by_name['CameraSettings'] = _CAMERASETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraSettings = _reflection.GeneratedProtocolMessageType('CameraSettings', (_message.Message,), dict(
  DESCRIPTOR = _CAMERASETTINGS,
  __module__ = 'pogoprotos.settings.master.camera_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CameraSettings)
  ))
_sym_db.RegisterMessage(CameraSettings)


# @@protoc_insertion_point(module_scope)
