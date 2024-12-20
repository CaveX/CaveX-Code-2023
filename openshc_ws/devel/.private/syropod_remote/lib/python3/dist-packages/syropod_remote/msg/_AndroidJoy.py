# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from syropod_remote/AndroidJoy.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class AndroidJoy(genpy.Message):
  _md5sum = "f798248626a520efb6e3973bbe95d25a"
  _type = "syropod_remote/AndroidJoy"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
std_msgs/String id_name
std_msgs/Bool override_priority_interface
geometry_msgs/Point primary_control_axis
geometry_msgs/Point secondary_control_axis
std_msgs/Int8 system_state
std_msgs/Int8 robot_state
std_msgs/Int8 gait_selection
std_msgs/Int8 cruise_control_mode
std_msgs/Int8 auto_navigation_mode
std_msgs/Int8 posing_mode
std_msgs/Int8 pose_reset_mode
std_msgs/Int8 primary_leg_selection
std_msgs/Int8 secondary_leg_selection
std_msgs/Int8 primary_leg_state
std_msgs/Int8 secondary_leg_state
std_msgs/Int8 parameter_selection
std_msgs/Int8 parameter_adjustment


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
MSG: std_msgs/Int8
int8 data
"""
  __slots__ = ['header','id_name','override_priority_interface','primary_control_axis','secondary_control_axis','system_state','robot_state','gait_selection','cruise_control_mode','auto_navigation_mode','posing_mode','pose_reset_mode','primary_leg_selection','secondary_leg_selection','primary_leg_state','secondary_leg_state','parameter_selection','parameter_adjustment']
  _slot_types = ['std_msgs/Header','std_msgs/String','std_msgs/Bool','geometry_msgs/Point','geometry_msgs/Point','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8','std_msgs/Int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,id_name,override_priority_interface,primary_control_axis,secondary_control_axis,system_state,robot_state,gait_selection,cruise_control_mode,auto_navigation_mode,posing_mode,pose_reset_mode,primary_leg_selection,secondary_leg_selection,primary_leg_state,secondary_leg_state,parameter_selection,parameter_adjustment

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AndroidJoy, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id_name is None:
        self.id_name = std_msgs.msg.String()
      if self.override_priority_interface is None:
        self.override_priority_interface = std_msgs.msg.Bool()
      if self.primary_control_axis is None:
        self.primary_control_axis = geometry_msgs.msg.Point()
      if self.secondary_control_axis is None:
        self.secondary_control_axis = geometry_msgs.msg.Point()
      if self.system_state is None:
        self.system_state = std_msgs.msg.Int8()
      if self.robot_state is None:
        self.robot_state = std_msgs.msg.Int8()
      if self.gait_selection is None:
        self.gait_selection = std_msgs.msg.Int8()
      if self.cruise_control_mode is None:
        self.cruise_control_mode = std_msgs.msg.Int8()
      if self.auto_navigation_mode is None:
        self.auto_navigation_mode = std_msgs.msg.Int8()
      if self.posing_mode is None:
        self.posing_mode = std_msgs.msg.Int8()
      if self.pose_reset_mode is None:
        self.pose_reset_mode = std_msgs.msg.Int8()
      if self.primary_leg_selection is None:
        self.primary_leg_selection = std_msgs.msg.Int8()
      if self.secondary_leg_selection is None:
        self.secondary_leg_selection = std_msgs.msg.Int8()
      if self.primary_leg_state is None:
        self.primary_leg_state = std_msgs.msg.Int8()
      if self.secondary_leg_state is None:
        self.secondary_leg_state = std_msgs.msg.Int8()
      if self.parameter_selection is None:
        self.parameter_selection = std_msgs.msg.Int8()
      if self.parameter_adjustment is None:
        self.parameter_adjustment = std_msgs.msg.Int8()
    else:
      self.header = std_msgs.msg.Header()
      self.id_name = std_msgs.msg.String()
      self.override_priority_interface = std_msgs.msg.Bool()
      self.primary_control_axis = geometry_msgs.msg.Point()
      self.secondary_control_axis = geometry_msgs.msg.Point()
      self.system_state = std_msgs.msg.Int8()
      self.robot_state = std_msgs.msg.Int8()
      self.gait_selection = std_msgs.msg.Int8()
      self.cruise_control_mode = std_msgs.msg.Int8()
      self.auto_navigation_mode = std_msgs.msg.Int8()
      self.posing_mode = std_msgs.msg.Int8()
      self.pose_reset_mode = std_msgs.msg.Int8()
      self.primary_leg_selection = std_msgs.msg.Int8()
      self.secondary_leg_selection = std_msgs.msg.Int8()
      self.primary_leg_state = std_msgs.msg.Int8()
      self.secondary_leg_state = std_msgs.msg.Int8()
      self.parameter_selection = std_msgs.msg.Int8()
      self.parameter_adjustment = std_msgs.msg.Int8()

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
      buff.write(_get_struct_B6d13b().pack(_x.override_priority_interface.data, _x.primary_control_axis.x, _x.primary_control_axis.y, _x.primary_control_axis.z, _x.secondary_control_axis.x, _x.secondary_control_axis.y, _x.secondary_control_axis.z, _x.system_state.data, _x.robot_state.data, _x.gait_selection.data, _x.cruise_control_mode.data, _x.auto_navigation_mode.data, _x.posing_mode.data, _x.pose_reset_mode.data, _x.primary_leg_selection.data, _x.secondary_leg_selection.data, _x.primary_leg_state.data, _x.secondary_leg_state.data, _x.parameter_selection.data, _x.parameter_adjustment.data))
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
      if self.primary_control_axis is None:
        self.primary_control_axis = geometry_msgs.msg.Point()
      if self.secondary_control_axis is None:
        self.secondary_control_axis = geometry_msgs.msg.Point()
      if self.system_state is None:
        self.system_state = std_msgs.msg.Int8()
      if self.robot_state is None:
        self.robot_state = std_msgs.msg.Int8()
      if self.gait_selection is None:
        self.gait_selection = std_msgs.msg.Int8()
      if self.cruise_control_mode is None:
        self.cruise_control_mode = std_msgs.msg.Int8()
      if self.auto_navigation_mode is None:
        self.auto_navigation_mode = std_msgs.msg.Int8()
      if self.posing_mode is None:
        self.posing_mode = std_msgs.msg.Int8()
      if self.pose_reset_mode is None:
        self.pose_reset_mode = std_msgs.msg.Int8()
      if self.primary_leg_selection is None:
        self.primary_leg_selection = std_msgs.msg.Int8()
      if self.secondary_leg_selection is None:
        self.secondary_leg_selection = std_msgs.msg.Int8()
      if self.primary_leg_state is None:
        self.primary_leg_state = std_msgs.msg.Int8()
      if self.secondary_leg_state is None:
        self.secondary_leg_state = std_msgs.msg.Int8()
      if self.parameter_selection is None:
        self.parameter_selection = std_msgs.msg.Int8()
      if self.parameter_adjustment is None:
        self.parameter_adjustment = std_msgs.msg.Int8()
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
      end += 62
      (_x.override_priority_interface.data, _x.primary_control_axis.x, _x.primary_control_axis.y, _x.primary_control_axis.z, _x.secondary_control_axis.x, _x.secondary_control_axis.y, _x.secondary_control_axis.z, _x.system_state.data, _x.robot_state.data, _x.gait_selection.data, _x.cruise_control_mode.data, _x.auto_navigation_mode.data, _x.posing_mode.data, _x.pose_reset_mode.data, _x.primary_leg_selection.data, _x.secondary_leg_selection.data, _x.primary_leg_state.data, _x.secondary_leg_state.data, _x.parameter_selection.data, _x.parameter_adjustment.data,) = _get_struct_B6d13b().unpack(str[start:end])
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
      buff.write(_get_struct_B6d13b().pack(_x.override_priority_interface.data, _x.primary_control_axis.x, _x.primary_control_axis.y, _x.primary_control_axis.z, _x.secondary_control_axis.x, _x.secondary_control_axis.y, _x.secondary_control_axis.z, _x.system_state.data, _x.robot_state.data, _x.gait_selection.data, _x.cruise_control_mode.data, _x.auto_navigation_mode.data, _x.posing_mode.data, _x.pose_reset_mode.data, _x.primary_leg_selection.data, _x.secondary_leg_selection.data, _x.primary_leg_state.data, _x.secondary_leg_state.data, _x.parameter_selection.data, _x.parameter_adjustment.data))
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
      if self.primary_control_axis is None:
        self.primary_control_axis = geometry_msgs.msg.Point()
      if self.secondary_control_axis is None:
        self.secondary_control_axis = geometry_msgs.msg.Point()
      if self.system_state is None:
        self.system_state = std_msgs.msg.Int8()
      if self.robot_state is None:
        self.robot_state = std_msgs.msg.Int8()
      if self.gait_selection is None:
        self.gait_selection = std_msgs.msg.Int8()
      if self.cruise_control_mode is None:
        self.cruise_control_mode = std_msgs.msg.Int8()
      if self.auto_navigation_mode is None:
        self.auto_navigation_mode = std_msgs.msg.Int8()
      if self.posing_mode is None:
        self.posing_mode = std_msgs.msg.Int8()
      if self.pose_reset_mode is None:
        self.pose_reset_mode = std_msgs.msg.Int8()
      if self.primary_leg_selection is None:
        self.primary_leg_selection = std_msgs.msg.Int8()
      if self.secondary_leg_selection is None:
        self.secondary_leg_selection = std_msgs.msg.Int8()
      if self.primary_leg_state is None:
        self.primary_leg_state = std_msgs.msg.Int8()
      if self.secondary_leg_state is None:
        self.secondary_leg_state = std_msgs.msg.Int8()
      if self.parameter_selection is None:
        self.parameter_selection = std_msgs.msg.Int8()
      if self.parameter_adjustment is None:
        self.parameter_adjustment = std_msgs.msg.Int8()
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
      end += 62
      (_x.override_priority_interface.data, _x.primary_control_axis.x, _x.primary_control_axis.y, _x.primary_control_axis.z, _x.secondary_control_axis.x, _x.secondary_control_axis.y, _x.secondary_control_axis.z, _x.system_state.data, _x.robot_state.data, _x.gait_selection.data, _x.cruise_control_mode.data, _x.auto_navigation_mode.data, _x.posing_mode.data, _x.pose_reset_mode.data, _x.primary_leg_selection.data, _x.secondary_leg_selection.data, _x.primary_leg_state.data, _x.secondary_leg_state.data, _x.parameter_selection.data, _x.parameter_adjustment.data,) = _get_struct_B6d13b().unpack(str[start:end])
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
_struct_B6d13b = None
def _get_struct_B6d13b():
    global _struct_B6d13b
    if _struct_B6d13b is None:
        _struct_B6d13b = struct.Struct("<B6d13b")
    return _struct_B6d13b
