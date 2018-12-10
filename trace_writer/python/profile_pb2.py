# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='profile.proto',
  package='perftools.profiles',
  syntax='proto3',
  serialized_pb=_b('\n\rprofile.proto\x12\x12perftools.profiles\"\xd2\x03\n\x07Profile\x12\x31\n\nSampleType\x18\x01 \x03(\x0b\x32\x1d.perftools.profiles.ValueType\x12*\n\x06Sample\x18\x02 \x03(\x0b\x32\x1a.perftools.profiles.Sample\x12,\n\x07Mapping\x18\x03 \x03(\x0b\x32\x1b.perftools.profiles.Mapping\x12.\n\x08Location\x18\x04 \x03(\x0b\x32\x1c.perftools.profiles.Location\x12.\n\x08\x46unction\x18\x05 \x03(\x0b\x32\x1c.perftools.profiles.Function\x12\x11\n\tTimeNanos\x18\t \x01(\x03\x12\x15\n\rDurationNanos\x18\n \x01(\x03\x12\x31\n\nPeriodType\x18\x0b \x01(\x0b\x32\x1d.perftools.profiles.ValueType\x12\x0e\n\x06Period\x18\x0c \x01(\x03\x12\x10\n\x08\x63ommentX\x18\r \x03(\x03\x12\x13\n\x0b\x64ropFramesX\x18\x07 \x01(\x03\x12\x13\n\x0bkeepFramesX\x18\x08 \x01(\x03\x12\x13\n\x0bstringTable\x18\x06 \x03(\t\x12\x1c\n\x14\x64\x65\x66\x61ult_sample_typeX\x18\x0e \x01(\x03\"E\n\tValueType\x12\x0c\n\x04Type\x18\x03 \x01(\t\x12\x0c\n\x04Unit\x18\x04 \x01(\t\x12\r\n\x05typeX\x18\x01 \x01(\x03\x12\r\n\x05unitX\x18\x02 \x01(\x03\".\n\x10MapStrFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x03(\t\".\n\x10MapIntFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x03(\x03\"\xf4\x01\n\x06Sample\x12.\n\x08Location\x18\x04 \x03(\x0b\x32\x1c.perftools.profiles.Location\x12\r\n\x05Value\x18\x02 \x03(\x03\x12\x33\n\x05Label\x18\x05 \x03(\x0b\x32$.perftools.profiles.MapStrFieldEntry\x12\x36\n\x08NumLabel\x18\x06 \x03(\x0b\x32$.perftools.profiles.MapIntFieldEntry\x12\x13\n\x0blocationIDX\x18\x01 \x03(\x04\x12)\n\x06labelX\x18\x03 \x03(\x0b\x32\x19.perftools.profiles.Label\"1\n\x05Label\x12\x0c\n\x04keyX\x18\x01 \x01(\x03\x12\x0c\n\x04strX\x18\x02 \x01(\x03\x12\x0c\n\x04numX\x18\x03 \x01(\x03\"\xe0\x01\n\x07Mapping\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\r\n\x05Start\x18\x02 \x01(\x04\x12\r\n\x05Limit\x18\x03 \x01(\x04\x12\x0e\n\x06Offset\x18\x04 \x01(\x04\x12\x0c\n\x04\x46ile\x18\x0b \x01(\t\x12\x0f\n\x07\x42uildID\x18\x0c \x01(\t\x12\x14\n\x0cHasFunctions\x18\x07 \x01(\x08\x12\x14\n\x0cHasFilenames\x18\x08 \x01(\x08\x12\x16\n\x0eHasLineNumbers\x18\t \x01(\x08\x12\x17\n\x0fHasInlineFrames\x18\n \x01(\x08\x12\r\n\x05\x66ileX\x18\x05 \x01(\x03\x12\x10\n\x08\x62uildIDX\x18\x06 \x01(\x03\"\x91\x01\n\x08Location\x12\n\n\x02ID\x18\x01 \x01(\x04\x12,\n\x07Mapping\x18\x05 \x01(\x0b\x32\x1b.perftools.profiles.Mapping\x12\x0f\n\x07\x41\x64\x64ress\x18\x03 \x01(\x04\x12&\n\x04Line\x18\x04 \x03(\x0b\x32\x18.perftools.profiles.Line\x12\x12\n\nmappingIDX\x18\x02 \x01(\x04\"Y\n\x04Line\x12.\n\x08\x46unction\x18\x03 \x01(\x0b\x32\x1c.perftools.profiles.Function\x12\x0c\n\x04Line\x18\x02 \x01(\x03\x12\x13\n\x0b\x66unctionIDX\x18\x01 \x01(\x04\"\x94\x01\n\x08\x46unction\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x0c\n\x04Name\x18\x06 \x01(\t\x12\x12\n\nSystemName\x18\x07 \x01(\t\x12\x10\n\x08\x46ilename\x18\x08 \x01(\t\x12\x11\n\tStartLine\x18\x05 \x01(\x03\x12\r\n\x05nameX\x18\x02 \x01(\x03\x12\x13\n\x0bsystemNameX\x18\x03 \x01(\x03\x12\x11\n\tfilenameX\x18\x04 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='perftools.profiles.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SampleType', full_name='perftools.profiles.Profile.SampleType', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sample', full_name='perftools.profiles.Profile.Sample', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mapping', full_name='perftools.profiles.Profile.Mapping', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Location', full_name='perftools.profiles.Profile.Location', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Function', full_name='perftools.profiles.Profile.Function', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeNanos', full_name='perftools.profiles.Profile.TimeNanos', index=5,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DurationNanos', full_name='perftools.profiles.Profile.DurationNanos', index=6,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PeriodType', full_name='perftools.profiles.Profile.PeriodType', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Period', full_name='perftools.profiles.Profile.Period', index=8,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commentX', full_name='perftools.profiles.Profile.commentX', index=9,
      number=13, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropFramesX', full_name='perftools.profiles.Profile.dropFramesX', index=10,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keepFramesX', full_name='perftools.profiles.Profile.keepFramesX', index=11,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stringTable', full_name='perftools.profiles.Profile.stringTable', index=12,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_sample_typeX', full_name='perftools.profiles.Profile.default_sample_typeX', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=38,
  serialized_end=504,
)


_VALUETYPE = _descriptor.Descriptor(
  name='ValueType',
  full_name='perftools.profiles.ValueType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='perftools.profiles.ValueType.Type', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Unit', full_name='perftools.profiles.ValueType.Unit', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='typeX', full_name='perftools.profiles.ValueType.typeX', index=2,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unitX', full_name='perftools.profiles.ValueType.unitX', index=3,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=506,
  serialized_end=575,
)


_MAPSTRFIELDENTRY = _descriptor.Descriptor(
  name='MapStrFieldEntry',
  full_name='perftools.profiles.MapStrFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='perftools.profiles.MapStrFieldEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='perftools.profiles.MapStrFieldEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=577,
  serialized_end=623,
)


_MAPINTFIELDENTRY = _descriptor.Descriptor(
  name='MapIntFieldEntry',
  full_name='perftools.profiles.MapIntFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='perftools.profiles.MapIntFieldEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='perftools.profiles.MapIntFieldEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=3,
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
  serialized_start=625,
  serialized_end=671,
)


_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='perftools.profiles.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Location', full_name='perftools.profiles.Sample.Location', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Value', full_name='perftools.profiles.Sample.Value', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Label', full_name='perftools.profiles.Sample.Label', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumLabel', full_name='perftools.profiles.Sample.NumLabel', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locationIDX', full_name='perftools.profiles.Sample.locationIDX', index=4,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labelX', full_name='perftools.profiles.Sample.labelX', index=5,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=674,
  serialized_end=918,
)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='perftools.profiles.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyX', full_name='perftools.profiles.Label.keyX', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strX', full_name='perftools.profiles.Label.strX', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numX', full_name='perftools.profiles.Label.numX', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=920,
  serialized_end=969,
)


_MAPPING = _descriptor.Descriptor(
  name='Mapping',
  full_name='perftools.profiles.Mapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='perftools.profiles.Mapping.ID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Start', full_name='perftools.profiles.Mapping.Start', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Limit', full_name='perftools.profiles.Mapping.Limit', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Offset', full_name='perftools.profiles.Mapping.Offset', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='File', full_name='perftools.profiles.Mapping.File', index=4,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BuildID', full_name='perftools.profiles.Mapping.BuildID', index=5,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HasFunctions', full_name='perftools.profiles.Mapping.HasFunctions', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HasFilenames', full_name='perftools.profiles.Mapping.HasFilenames', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HasLineNumbers', full_name='perftools.profiles.Mapping.HasLineNumbers', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HasInlineFrames', full_name='perftools.profiles.Mapping.HasInlineFrames', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileX', full_name='perftools.profiles.Mapping.fileX', index=10,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildIDX', full_name='perftools.profiles.Mapping.buildIDX', index=11,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=972,
  serialized_end=1196,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='perftools.profiles.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='perftools.profiles.Location.ID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mapping', full_name='perftools.profiles.Location.Mapping', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Address', full_name='perftools.profiles.Location.Address', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Line', full_name='perftools.profiles.Location.Line', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mappingIDX', full_name='perftools.profiles.Location.mappingIDX', index=4,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1199,
  serialized_end=1344,
)


_LINE = _descriptor.Descriptor(
  name='Line',
  full_name='perftools.profiles.Line',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Function', full_name='perftools.profiles.Line.Function', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Line', full_name='perftools.profiles.Line.Line', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functionIDX', full_name='perftools.profiles.Line.functionIDX', index=2,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1346,
  serialized_end=1435,
)


_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='perftools.profiles.Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='perftools.profiles.Function.ID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='perftools.profiles.Function.Name', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SystemName', full_name='perftools.profiles.Function.SystemName', index=2,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Filename', full_name='perftools.profiles.Function.Filename', index=3,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartLine', full_name='perftools.profiles.Function.StartLine', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nameX', full_name='perftools.profiles.Function.nameX', index=5,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemNameX', full_name='perftools.profiles.Function.systemNameX', index=6,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filenameX', full_name='perftools.profiles.Function.filenameX', index=7,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1438,
  serialized_end=1586,
)

_PROFILE.fields_by_name['SampleType'].message_type = _VALUETYPE
_PROFILE.fields_by_name['Sample'].message_type = _SAMPLE
_PROFILE.fields_by_name['Mapping'].message_type = _MAPPING
_PROFILE.fields_by_name['Location'].message_type = _LOCATION
_PROFILE.fields_by_name['Function'].message_type = _FUNCTION
_PROFILE.fields_by_name['PeriodType'].message_type = _VALUETYPE
_SAMPLE.fields_by_name['Location'].message_type = _LOCATION
_SAMPLE.fields_by_name['Label'].message_type = _MAPSTRFIELDENTRY
_SAMPLE.fields_by_name['NumLabel'].message_type = _MAPINTFIELDENTRY
_SAMPLE.fields_by_name['labelX'].message_type = _LABEL
_LOCATION.fields_by_name['Mapping'].message_type = _MAPPING
_LOCATION.fields_by_name['Line'].message_type = _LINE
_LINE.fields_by_name['Function'].message_type = _FUNCTION
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['ValueType'] = _VALUETYPE
DESCRIPTOR.message_types_by_name['MapStrFieldEntry'] = _MAPSTRFIELDENTRY
DESCRIPTOR.message_types_by_name['MapIntFieldEntry'] = _MAPINTFIELDENTRY
DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['Mapping'] = _MAPPING
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Line'] = _LINE
DESCRIPTOR.message_types_by_name['Function'] = _FUNCTION

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(
  DESCRIPTOR = _PROFILE,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.Profile)
  ))
_sym_db.RegisterMessage(Profile)

ValueType = _reflection.GeneratedProtocolMessageType('ValueType', (_message.Message,), dict(
  DESCRIPTOR = _VALUETYPE,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.ValueType)
  ))
_sym_db.RegisterMessage(ValueType)

MapStrFieldEntry = _reflection.GeneratedProtocolMessageType('MapStrFieldEntry', (_message.Message,), dict(
  DESCRIPTOR = _MAPSTRFIELDENTRY,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.MapStrFieldEntry)
  ))
_sym_db.RegisterMessage(MapStrFieldEntry)

MapIntFieldEntry = _reflection.GeneratedProtocolMessageType('MapIntFieldEntry', (_message.Message,), dict(
  DESCRIPTOR = _MAPINTFIELDENTRY,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.MapIntFieldEntry)
  ))
_sym_db.RegisterMessage(MapIntFieldEntry)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.Sample)
  ))
_sym_db.RegisterMessage(Sample)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(
  DESCRIPTOR = _LABEL,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.Label)
  ))
_sym_db.RegisterMessage(Label)

Mapping = _reflection.GeneratedProtocolMessageType('Mapping', (_message.Message,), dict(
  DESCRIPTOR = _MAPPING,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.Mapping)
  ))
_sym_db.RegisterMessage(Mapping)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.Location)
  ))
_sym_db.RegisterMessage(Location)

Line = _reflection.GeneratedProtocolMessageType('Line', (_message.Message,), dict(
  DESCRIPTOR = _LINE,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.Line)
  ))
_sym_db.RegisterMessage(Line)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTION,
  __module__ = 'profile_pb2'
  # @@protoc_insertion_point(class_scope:perftools.profiles.Function)
  ))
_sym_db.RegisterMessage(Function)


# @@protoc_insertion_point(module_scope)
