# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from syropod_remote/AndroidSensor.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class AndroidSensor(genpy.Message):
  _md5sum = "05a22ff6b1072fe74d2077e0d442d058"
  _type = "syropod_remote/AndroidSensor"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
std_msgs/String id_name
std_msgs/Bool override_priority_interface
geometry_msgs/Point orientation
std_msgs/Float64 relative_compass
std_msgs/Int8 robot_state
std_msgs/Int8 posing_mode
geometry_msgs/Point control_axis

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: std_msgs/Bool
bool data
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: std_msgs/Float64
float64 data
================================================================================
MSG: std_msgs/Int8
int8 data
"""
  __slots__ = ['header','id_name','override_priority_interface','orientation','relative_compass','robot_state','posing_mode','control_axis']
  _slot_types = ['std_msgs/Header','std_msgs/String','std_msgs/Bool','geometry_msgs/Point','std_msgs/Float64','std_msgs/Int8','std_msgs/Int8','geometry_msgs/Point']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,id_name,override_priority_interface,orientation,relative_compass,robot_state,posing_mode,control_axis

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AndroidSensor, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id_name is None:
        self.id_name = std_msgs.msg.String()
      if self.override_priority_interface is None:
        self.override_priority_interface = std_msgs.msg.Bool()
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Point()
      if self.relative_compass is None:
        self.relative_compass = std_msgs.msg.Float64()
      if self.robot_state is None:
        self.robot_state = std_msgs.msg.Int8()
      if self.posing_mode is None:
        self.posing_mode = std_msgs.msg.Int8()
      if self.control_axis is None:
        self.control_axis = geometry_msgs.msg.Point()
    else:
      self.header = std_msgs.msg.Header()
      self.id_name = std_msgs.msg.String()
      self.override_priority_interface = std_msgs.msg.Bool()
      self.orientation = geometry_msgs.msg.Point()
      self.relative_compass = std_msgs.msg.Float64()
      self.robot_state = std_msgs.msg.Int8()
      self.posing_mode = std_msgs.msg.Int8()
      self.control_axis = geometry_msgs.msg.Point()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.id_name.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B4d2b3d().pack(_x.override_priority_interface.data, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.relative_compass.data, _x.robot_state.data, _x.posing_mode.data, _x.control_axis.x, _x.control_axis.y, _x.control_axis.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id_name is None:
        self.id_name = std_msgs.msg.String()
      if self.override_priority_interface is None:
        self.override_priority_interface = std_msgs.msg.Bool()
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Point()
      if self.relative_compass is None:
        self.relative_compass = std_msgs.msg.Float64()
      if self.robot_state is None:
        self.robot_state = std_msgs.msg.Int8()
      if self.posing_mode is None:
        self.posing_mode = std_msgs.msg.Int8()
      if self.control_axis is None:
        self.control_axis = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id_name.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id_name.data = str[start:end]
      _x = self
      start = end
      end += 59
      (_x.override_priority_interface.data, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.relative_compass.data, _x.robot_state.data, _x.posing_mode.data, _x.control_axis.x, _x.control_axis.y, _x.control_axis.z,) = _get_struct_B4d2b3d().unpack(str[start:end])
      self.override_priority_interface.data = bool(self.override_priority_interface.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.id_name.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B4d2b3d().pack(_x.override_priority_interface.data, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.relative_compass.data, _x.robot_state.data, _x.posing_mode.data, _x.control_axis.x, _x.control_axis.y, _x.control_axis.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id_name is None:
        self.id_name = std_msgs.msg.String()
      if self.override_priority_interface is None:
        self.override_priority_interface = std_msgs.msg.Bool()
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Point()
      if self.relative_compass is None:
        self.relative_compass = std_msgs.msg.Float64()
      if self.robot_state is None:
        self.robot_state = std_msgs.msg.Int8()
      if self.posing_mode is None:
        self.posing_mode = std_msgs.msg.Int8()
      if self.control_axis is None:
        self.control_axis = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.id_name.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.id_name.data = str[start:end]
      _x = self
      start = end
      end += 59
      (_x.override_priority_interface.data, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.relative_compass.data, _x.robot_state.data, _x.posing_mode.data, _x.control_axis.x, _x.control_axis.y, _x.control_axis.z,) = _get_struct_B4d2b3d().unpack(str[start:end])
      self.override_priority_interface.data = bool(self.override_priority_interface.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B4d2b3d = None
def _get_struct_B4d2b3d():
    global _struct_B4d2b3d
    if _struct_B4d2b3d is None:
        _struct_B4d2b3d = struct.Struct("<B4d2b3d")
    return _struct_B4d2b3d
