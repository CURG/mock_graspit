# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import graspable_object_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='run_recognition.proto',
  package='graspit_rpcz',
  serialized_pb='\n\x15run_recognition.proto\x12\x0cgraspit_rpcz\x1a\x16graspable_object.proto\"\x1a\n\x18ObjectRecognitionRequest\"C\n\x19ObjectRecognitionResponse\x12&\n\x0c\x66oundObjects\x18\x01 \x03(\x0b\x32\x10.GraspableObject2r\n\x18ObjectRecognitionService\x12V\n\x03run\x12&.graspit_rpcz.ObjectRecognitionRequest\x1a\'.graspit_rpcz.ObjectRecognitionResponse')




_OBJECTRECOGNITIONREQUEST = descriptor.Descriptor(
  name='ObjectRecognitionRequest',
  full_name='graspit_rpcz.ObjectRecognitionRequest',
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=63,
  serialized_end=89,
)


_OBJECTRECOGNITIONRESPONSE = descriptor.Descriptor(
  name='ObjectRecognitionResponse',
  full_name='graspit_rpcz.ObjectRecognitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='foundObjects', full_name='graspit_rpcz.ObjectRecognitionResponse.foundObjects', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=91,
  serialized_end=158,
)

_OBJECTRECOGNITIONRESPONSE.fields_by_name['foundObjects'].message_type = graspable_object_pb2._GRASPABLEOBJECT
DESCRIPTOR.message_types_by_name['ObjectRecognitionRequest'] = _OBJECTRECOGNITIONREQUEST
DESCRIPTOR.message_types_by_name['ObjectRecognitionResponse'] = _OBJECTRECOGNITIONRESPONSE

class ObjectRecognitionRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OBJECTRECOGNITIONREQUEST
  
  # @@protoc_insertion_point(class_scope:graspit_rpcz.ObjectRecognitionRequest)

class ObjectRecognitionResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OBJECTRECOGNITIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:graspit_rpcz.ObjectRecognitionResponse)

# @@protoc_insertion_point(module_scope)