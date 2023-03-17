# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from syropod_highlevel_controller/LegState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class LegState(genpy.Message):
  _md5sum = "dadda7ca412e345da1ddcca95ddf0ccc"
  _type = "syropod_highlevel_controller/LegState"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
string name

geometry_msgs/PoseStamped walker_tip_pose
geometry_msgs/PoseStamped target_tip_pose
geometry_msgs/PoseStamped poser_tip_pose
geometry_msgs/PoseStamped model_tip_pose
geometry_msgs/PoseStamped actual_tip_pose

geometry_msgs/TwistStamped model_tip_velocity

float64[] joint_positions
float64[] joint_velocities
float64[] joint_efforts

float64 stance_progress
float64 swing_progress

float64 time_to_swing_end
geometry_msgs/Pose pose_delta

geometry_msgs/Pose auto_pose

geometry_msgs/Vector3 tip_force
geometry_msgs/Vector3 admittance_delta
float64 virtual_stiffness



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
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/TwistStamped
# A twist with reference coordinate frame and timestamp
Header header
Twist twist

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','name','walker_tip_pose','target_tip_pose','poser_tip_pose','model_tip_pose','actual_tip_pose','model_tip_velocity','joint_positions','joint_velocities','joint_efforts','stance_progress','swing_progress','time_to_swing_end','pose_delta','auto_pose','tip_force','admittance_delta','virtual_stiffness']
  _slot_types = ['std_msgs/Header','string','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/TwistStamped','float64[]','float64[]','float64[]','float64','float64','float64','geometry_msgs/Pose','geometry_msgs/Pose','geometry_msgs/Vector3','geometry_msgs/Vector3','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,name,walker_tip_pose,target_tip_pose,poser_tip_pose,model_tip_pose,actual_tip_pose,model_tip_velocity,joint_positions,joint_velocities,joint_efforts,stance_progress,swing_progress,time_to_swing_end,pose_delta,auto_pose,tip_force,admittance_delta,virtual_stiffness

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LegState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.name is None:
        self.name = ''
      if self.walker_tip_pose is None:
        self.walker_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.target_tip_pose is None:
        self.target_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.poser_tip_pose is None:
        self.poser_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.model_tip_pose is None:
        self.model_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.actual_tip_pose is None:
        self.actual_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.model_tip_velocity is None:
        self.model_tip_velocity = geometry_msgs.msg.TwistStamped()
      if self.joint_positions is None:
        self.joint_positions = []
      if self.joint_velocities is None:
        self.joint_velocities = []
      if self.joint_efforts is None:
        self.joint_efforts = []
      if self.stance_progress is None:
        self.stance_progress = 0.
      if self.swing_progress is None:
        self.swing_progress = 0.
      if self.time_to_swing_end is None:
        self.time_to_swing_end = 0.
      if self.pose_delta is None:
        self.pose_delta = geometry_msgs.msg.Pose()
      if self.auto_pose is None:
        self.auto_pose = geometry_msgs.msg.Pose()
      if self.tip_force is None:
        self.tip_force = geometry_msgs.msg.Vector3()
      if self.admittance_delta is None:
        self.admittance_delta = geometry_msgs.msg.Vector3()
      if self.virtual_stiffness is None:
        self.virtual_stiffness = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.name = ''
      self.walker_tip_pose = geometry_msgs.msg.PoseStamped()
      self.target_tip_pose = geometry_msgs.msg.PoseStamped()
      self.poser_tip_pose = geometry_msgs.msg.PoseStamped()
      self.model_tip_pose = geometry_msgs.msg.PoseStamped()
      self.actual_tip_pose = geometry_msgs.msg.PoseStamped()
      self.model_tip_velocity = geometry_msgs.msg.TwistStamped()
      self.joint_positions = []
      self.joint_velocities = []
      self.joint_efforts = []
      self.stance_progress = 0.
      self.swing_progress = 0.
      self.time_to_swing_end = 0.
      self.pose_delta = geometry_msgs.msg.Pose()
      self.auto_pose = geometry_msgs.msg.Pose()
      self.tip_force = geometry_msgs.msg.Vector3()
      self.admittance_delta = geometry_msgs.msg.Vector3()
      self.virtual_stiffness = 0.

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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.walker_tip_pose.header.seq, _x.walker_tip_pose.header.stamp.secs, _x.walker_tip_pose.header.stamp.nsecs))
      _x = self.walker_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.walker_tip_pose.pose.position.x, _x.walker_tip_pose.pose.position.y, _x.walker_tip_pose.pose.position.z, _x.walker_tip_pose.pose.orientation.x, _x.walker_tip_pose.pose.orientation.y, _x.walker_tip_pose.pose.orientation.z, _x.walker_tip_pose.pose.orientation.w, _x.target_tip_pose.header.seq, _x.target_tip_pose.header.stamp.secs, _x.target_tip_pose.header.stamp.nsecs))
      _x = self.target_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.target_tip_pose.pose.position.x, _x.target_tip_pose.pose.position.y, _x.target_tip_pose.pose.position.z, _x.target_tip_pose.pose.orientation.x, _x.target_tip_pose.pose.orientation.y, _x.target_tip_pose.pose.orientation.z, _x.target_tip_pose.pose.orientation.w, _x.poser_tip_pose.header.seq, _x.poser_tip_pose.header.stamp.secs, _x.poser_tip_pose.header.stamp.nsecs))
      _x = self.poser_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.poser_tip_pose.pose.position.x, _x.poser_tip_pose.pose.position.y, _x.poser_tip_pose.pose.position.z, _x.poser_tip_pose.pose.orientation.x, _x.poser_tip_pose.pose.orientation.y, _x.poser_tip_pose.pose.orientation.z, _x.poser_tip_pose.pose.orientation.w, _x.model_tip_pose.header.seq, _x.model_tip_pose.header.stamp.secs, _x.model_tip_pose.header.stamp.nsecs))
      _x = self.model_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.model_tip_pose.pose.position.x, _x.model_tip_pose.pose.position.y, _x.model_tip_pose.pose.position.z, _x.model_tip_pose.pose.orientation.x, _x.model_tip_pose.pose.orientation.y, _x.model_tip_pose.pose.orientation.z, _x.model_tip_pose.pose.orientation.w, _x.actual_tip_pose.header.seq, _x.actual_tip_pose.header.stamp.secs, _x.actual_tip_pose.header.stamp.nsecs))
      _x = self.actual_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.actual_tip_pose.pose.position.x, _x.actual_tip_pose.pose.position.y, _x.actual_tip_pose.pose.position.z, _x.actual_tip_pose.pose.orientation.x, _x.actual_tip_pose.pose.orientation.y, _x.actual_tip_pose.pose.orientation.z, _x.actual_tip_pose.pose.orientation.w, _x.model_tip_velocity.header.seq, _x.model_tip_velocity.header.stamp.secs, _x.model_tip_velocity.header.stamp.nsecs))
      _x = self.model_tip_velocity.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.model_tip_velocity.twist.linear.x, _x.model_tip_velocity.twist.linear.y, _x.model_tip_velocity.twist.linear.z, _x.model_tip_velocity.twist.angular.x, _x.model_tip_velocity.twist.angular.y, _x.model_tip_velocity.twist.angular.z))
      length = len(self.joint_positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.joint_positions))
      length = len(self.joint_velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.joint_velocities))
      length = len(self.joint_efforts)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.joint_efforts))
      _x = self
      buff.write(_get_struct_24d().pack(_x.stance_progress, _x.swing_progress, _x.time_to_swing_end, _x.pose_delta.position.x, _x.pose_delta.position.y, _x.pose_delta.position.z, _x.pose_delta.orientation.x, _x.pose_delta.orientation.y, _x.pose_delta.orientation.z, _x.pose_delta.orientation.w, _x.auto_pose.position.x, _x.auto_pose.position.y, _x.auto_pose.position.z, _x.auto_pose.orientation.x, _x.auto_pose.orientation.y, _x.auto_pose.orientation.z, _x.auto_pose.orientation.w, _x.tip_force.x, _x.tip_force.y, _x.tip_force.z, _x.admittance_delta.x, _x.admittance_delta.y, _x.admittance_delta.z, _x.virtual_stiffness))
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
      if self.walker_tip_pose is None:
        self.walker_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.target_tip_pose is None:
        self.target_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.poser_tip_pose is None:
        self.poser_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.model_tip_pose is None:
        self.model_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.actual_tip_pose is None:
        self.actual_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.model_tip_velocity is None:
        self.model_tip_velocity = geometry_msgs.msg.TwistStamped()
      if self.pose_delta is None:
        self.pose_delta = geometry_msgs.msg.Pose()
      if self.auto_pose is None:
        self.auto_pose = geometry_msgs.msg.Pose()
      if self.tip_force is None:
        self.tip_force = geometry_msgs.msg.Vector3()
      if self.admittance_delta is None:
        self.admittance_delta = geometry_msgs.msg.Vector3()
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
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.walker_tip_pose.header.seq, _x.walker_tip_pose.header.stamp.secs, _x.walker_tip_pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.walker_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.walker_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.walker_tip_pose.pose.position.x, _x.walker_tip_pose.pose.position.y, _x.walker_tip_pose.pose.position.z, _x.walker_tip_pose.pose.orientation.x, _x.walker_tip_pose.pose.orientation.y, _x.walker_tip_pose.pose.orientation.z, _x.walker_tip_pose.pose.orientation.w, _x.target_tip_pose.header.seq, _x.target_tip_pose.header.stamp.secs, _x.target_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.target_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.target_tip_pose.pose.position.x, _x.target_tip_pose.pose.position.y, _x.target_tip_pose.pose.position.z, _x.target_tip_pose.pose.orientation.x, _x.target_tip_pose.pose.orientation.y, _x.target_tip_pose.pose.orientation.z, _x.target_tip_pose.pose.orientation.w, _x.poser_tip_pose.header.seq, _x.poser_tip_pose.header.stamp.secs, _x.poser_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.poser_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.poser_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.poser_tip_pose.pose.position.x, _x.poser_tip_pose.pose.position.y, _x.poser_tip_pose.pose.position.z, _x.poser_tip_pose.pose.orientation.x, _x.poser_tip_pose.pose.orientation.y, _x.poser_tip_pose.pose.orientation.z, _x.poser_tip_pose.pose.orientation.w, _x.model_tip_pose.header.seq, _x.model_tip_pose.header.stamp.secs, _x.model_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.model_tip_pose.pose.position.x, _x.model_tip_pose.pose.position.y, _x.model_tip_pose.pose.position.z, _x.model_tip_pose.pose.orientation.x, _x.model_tip_pose.pose.orientation.y, _x.model_tip_pose.pose.orientation.z, _x.model_tip_pose.pose.orientation.w, _x.actual_tip_pose.header.seq, _x.actual_tip_pose.header.stamp.secs, _x.actual_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.actual_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.actual_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.actual_tip_pose.pose.position.x, _x.actual_tip_pose.pose.position.y, _x.actual_tip_pose.pose.position.z, _x.actual_tip_pose.pose.orientation.x, _x.actual_tip_pose.pose.orientation.y, _x.actual_tip_pose.pose.orientation.z, _x.actual_tip_pose.pose.orientation.w, _x.model_tip_velocity.header.seq, _x.model_tip_velocity.header.stamp.secs, _x.model_tip_velocity.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_tip_velocity.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_tip_velocity.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.model_tip_velocity.twist.linear.x, _x.model_tip_velocity.twist.linear.y, _x.model_tip_velocity.twist.linear.z, _x.model_tip_velocity.twist.angular.x, _x.model_tip_velocity.twist.angular.y, _x.model_tip_velocity.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_positions = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_velocities = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_efforts = s.unpack(str[start:end])
      _x = self
      start = end
      end += 192
      (_x.stance_progress, _x.swing_progress, _x.time_to_swing_end, _x.pose_delta.position.x, _x.pose_delta.position.y, _x.pose_delta.position.z, _x.pose_delta.orientation.x, _x.pose_delta.orientation.y, _x.pose_delta.orientation.z, _x.pose_delta.orientation.w, _x.auto_pose.position.x, _x.auto_pose.position.y, _x.auto_pose.position.z, _x.auto_pose.orientation.x, _x.auto_pose.orientation.y, _x.auto_pose.orientation.z, _x.auto_pose.orientation.w, _x.tip_force.x, _x.tip_force.y, _x.tip_force.z, _x.admittance_delta.x, _x.admittance_delta.y, _x.admittance_delta.z, _x.virtual_stiffness,) = _get_struct_24d().unpack(str[start:end])
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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.walker_tip_pose.header.seq, _x.walker_tip_pose.header.stamp.secs, _x.walker_tip_pose.header.stamp.nsecs))
      _x = self.walker_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.walker_tip_pose.pose.position.x, _x.walker_tip_pose.pose.position.y, _x.walker_tip_pose.pose.position.z, _x.walker_tip_pose.pose.orientation.x, _x.walker_tip_pose.pose.orientation.y, _x.walker_tip_pose.pose.orientation.z, _x.walker_tip_pose.pose.orientation.w, _x.target_tip_pose.header.seq, _x.target_tip_pose.header.stamp.secs, _x.target_tip_pose.header.stamp.nsecs))
      _x = self.target_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.target_tip_pose.pose.position.x, _x.target_tip_pose.pose.position.y, _x.target_tip_pose.pose.position.z, _x.target_tip_pose.pose.orientation.x, _x.target_tip_pose.pose.orientation.y, _x.target_tip_pose.pose.orientation.z, _x.target_tip_pose.pose.orientation.w, _x.poser_tip_pose.header.seq, _x.poser_tip_pose.header.stamp.secs, _x.poser_tip_pose.header.stamp.nsecs))
      _x = self.poser_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.poser_tip_pose.pose.position.x, _x.poser_tip_pose.pose.position.y, _x.poser_tip_pose.pose.position.z, _x.poser_tip_pose.pose.orientation.x, _x.poser_tip_pose.pose.orientation.y, _x.poser_tip_pose.pose.orientation.z, _x.poser_tip_pose.pose.orientation.w, _x.model_tip_pose.header.seq, _x.model_tip_pose.header.stamp.secs, _x.model_tip_pose.header.stamp.nsecs))
      _x = self.model_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.model_tip_pose.pose.position.x, _x.model_tip_pose.pose.position.y, _x.model_tip_pose.pose.position.z, _x.model_tip_pose.pose.orientation.x, _x.model_tip_pose.pose.orientation.y, _x.model_tip_pose.pose.orientation.z, _x.model_tip_pose.pose.orientation.w, _x.actual_tip_pose.header.seq, _x.actual_tip_pose.header.stamp.secs, _x.actual_tip_pose.header.stamp.nsecs))
      _x = self.actual_tip_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.actual_tip_pose.pose.position.x, _x.actual_tip_pose.pose.position.y, _x.actual_tip_pose.pose.position.z, _x.actual_tip_pose.pose.orientation.x, _x.actual_tip_pose.pose.orientation.y, _x.actual_tip_pose.pose.orientation.z, _x.actual_tip_pose.pose.orientation.w, _x.model_tip_velocity.header.seq, _x.model_tip_velocity.header.stamp.secs, _x.model_tip_velocity.header.stamp.nsecs))
      _x = self.model_tip_velocity.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.model_tip_velocity.twist.linear.x, _x.model_tip_velocity.twist.linear.y, _x.model_tip_velocity.twist.linear.z, _x.model_tip_velocity.twist.angular.x, _x.model_tip_velocity.twist.angular.y, _x.model_tip_velocity.twist.angular.z))
      length = len(self.joint_positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.joint_positions.tostring())
      length = len(self.joint_velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.joint_velocities.tostring())
      length = len(self.joint_efforts)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.joint_efforts.tostring())
      _x = self
      buff.write(_get_struct_24d().pack(_x.stance_progress, _x.swing_progress, _x.time_to_swing_end, _x.pose_delta.position.x, _x.pose_delta.position.y, _x.pose_delta.position.z, _x.pose_delta.orientation.x, _x.pose_delta.orientation.y, _x.pose_delta.orientation.z, _x.pose_delta.orientation.w, _x.auto_pose.position.x, _x.auto_pose.position.y, _x.auto_pose.position.z, _x.auto_pose.orientation.x, _x.auto_pose.orientation.y, _x.auto_pose.orientation.z, _x.auto_pose.orientation.w, _x.tip_force.x, _x.tip_force.y, _x.tip_force.z, _x.admittance_delta.x, _x.admittance_delta.y, _x.admittance_delta.z, _x.virtual_stiffness))
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
      if self.walker_tip_pose is None:
        self.walker_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.target_tip_pose is None:
        self.target_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.poser_tip_pose is None:
        self.poser_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.model_tip_pose is None:
        self.model_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.actual_tip_pose is None:
        self.actual_tip_pose = geometry_msgs.msg.PoseStamped()
      if self.model_tip_velocity is None:
        self.model_tip_velocity = geometry_msgs.msg.TwistStamped()
      if self.pose_delta is None:
        self.pose_delta = geometry_msgs.msg.Pose()
      if self.auto_pose is None:
        self.auto_pose = geometry_msgs.msg.Pose()
      if self.tip_force is None:
        self.tip_force = geometry_msgs.msg.Vector3()
      if self.admittance_delta is None:
        self.admittance_delta = geometry_msgs.msg.Vector3()
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
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.walker_tip_pose.header.seq, _x.walker_tip_pose.header.stamp.secs, _x.walker_tip_pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.walker_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.walker_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.walker_tip_pose.pose.position.x, _x.walker_tip_pose.pose.position.y, _x.walker_tip_pose.pose.position.z, _x.walker_tip_pose.pose.orientation.x, _x.walker_tip_pose.pose.orientation.y, _x.walker_tip_pose.pose.orientation.z, _x.walker_tip_pose.pose.orientation.w, _x.target_tip_pose.header.seq, _x.target_tip_pose.header.stamp.secs, _x.target_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.target_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.target_tip_pose.pose.position.x, _x.target_tip_pose.pose.position.y, _x.target_tip_pose.pose.position.z, _x.target_tip_pose.pose.orientation.x, _x.target_tip_pose.pose.orientation.y, _x.target_tip_pose.pose.orientation.z, _x.target_tip_pose.pose.orientation.w, _x.poser_tip_pose.header.seq, _x.poser_tip_pose.header.stamp.secs, _x.poser_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.poser_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.poser_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.poser_tip_pose.pose.position.x, _x.poser_tip_pose.pose.position.y, _x.poser_tip_pose.pose.position.z, _x.poser_tip_pose.pose.orientation.x, _x.poser_tip_pose.pose.orientation.y, _x.poser_tip_pose.pose.orientation.z, _x.poser_tip_pose.pose.orientation.w, _x.model_tip_pose.header.seq, _x.model_tip_pose.header.stamp.secs, _x.model_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.model_tip_pose.pose.position.x, _x.model_tip_pose.pose.position.y, _x.model_tip_pose.pose.position.z, _x.model_tip_pose.pose.orientation.x, _x.model_tip_pose.pose.orientation.y, _x.model_tip_pose.pose.orientation.z, _x.model_tip_pose.pose.orientation.w, _x.actual_tip_pose.header.seq, _x.actual_tip_pose.header.stamp.secs, _x.actual_tip_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.actual_tip_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.actual_tip_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.actual_tip_pose.pose.position.x, _x.actual_tip_pose.pose.position.y, _x.actual_tip_pose.pose.position.z, _x.actual_tip_pose.pose.orientation.x, _x.actual_tip_pose.pose.orientation.y, _x.actual_tip_pose.pose.orientation.z, _x.actual_tip_pose.pose.orientation.w, _x.model_tip_velocity.header.seq, _x.model_tip_velocity.header.stamp.secs, _x.model_tip_velocity.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.model_tip_velocity.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.model_tip_velocity.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.model_tip_velocity.twist.linear.x, _x.model_tip_velocity.twist.linear.y, _x.model_tip_velocity.twist.linear.z, _x.model_tip_velocity.twist.angular.x, _x.model_tip_velocity.twist.angular.y, _x.model_tip_velocity.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.joint_efforts = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 192
      (_x.stance_progress, _x.swing_progress, _x.time_to_swing_end, _x.pose_delta.position.x, _x.pose_delta.position.y, _x.pose_delta.position.z, _x.pose_delta.orientation.x, _x.pose_delta.orientation.y, _x.pose_delta.orientation.z, _x.pose_delta.orientation.w, _x.auto_pose.position.x, _x.auto_pose.position.y, _x.auto_pose.position.z, _x.auto_pose.orientation.x, _x.auto_pose.orientation.y, _x.auto_pose.orientation.z, _x.auto_pose.orientation.w, _x.tip_force.x, _x.tip_force.y, _x.tip_force.z, _x.admittance_delta.x, _x.admittance_delta.y, _x.admittance_delta.z, _x.virtual_stiffness,) = _get_struct_24d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_24d = None
def _get_struct_24d():
    global _struct_24d
    if _struct_24d is None:
        _struct_24d = struct.Struct("<24d")
    return _struct_24d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
_struct_7d3I = None
def _get_struct_7d3I():
    global _struct_7d3I
    if _struct_7d3I is None:
        _struct_7d3I = struct.Struct("<7d3I")
    return _struct_7d3I