# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mavros_msgs/Trajectory.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import mavros_msgs.msg
import std_msgs.msg

class Trajectory(genpy.Message):
  _md5sum = "3d34ec9673348ab7c0bc80373ec76fc8"
  _type = "mavros_msgs/Trajectory"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# MAVLink message: TRAJECTORY
# https://mavlink.io/en/messages/common.html#TRAJECTORY

std_msgs/Header header

uint8 type # See enum MAV_TRAJECTORY_REPRESENTATION.
uint8 MAV_TRAJECTORY_REPRESENTATION_WAYPOINTS = 0
uint8 MAV_TRAJECTORY_REPRESENTATION_BEZIER = 1

mavros_msgs/PositionTarget point_1
mavros_msgs/PositionTarget point_2
mavros_msgs/PositionTarget point_3
mavros_msgs/PositionTarget point_4
mavros_msgs/PositionTarget point_5

uint8[5] point_valid # States if respective point is valid.

float32[5] time_horizon # if type MAV_TRAJECTORY_REPRESENTATION_BEZIER, it represents the time horizon for each point, otherwise set to NaN

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
MSG: mavros_msgs/PositionTarget
# Message for SET_POSITION_TARGET_LOCAL_NED
#
# Some complex system requires all feautures that mavlink
# message provide. See issue #402.

std_msgs/Header header

uint8 coordinate_frame
uint8 FRAME_LOCAL_NED = 1
uint8 FRAME_LOCAL_OFFSET_NED = 7
uint8 FRAME_BODY_NED = 8
uint8 FRAME_BODY_OFFSET_NED = 9

uint16 type_mask
uint16 IGNORE_PX = 1	# Position ignore flags
uint16 IGNORE_PY = 2
uint16 IGNORE_PZ = 4
uint16 IGNORE_VX = 8	# Velocity vector ignore flags
uint16 IGNORE_VY = 16
uint16 IGNORE_VZ = 32
uint16 IGNORE_AFX = 64	# Acceleration/Force vector ignore flags
uint16 IGNORE_AFY = 128
uint16 IGNORE_AFZ = 256
uint16 FORCE = 512	# Force in af vector flag
uint16 IGNORE_YAW = 1024
uint16 IGNORE_YAW_RATE = 2048

geometry_msgs/Point position
geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 acceleration_or_force
float32 yaw
float32 yaw_rate

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

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
  # Pseudo-constants
  MAV_TRAJECTORY_REPRESENTATION_WAYPOINTS = 0
  MAV_TRAJECTORY_REPRESENTATION_BEZIER = 1

  __slots__ = ['header','type','point_1','point_2','point_3','point_4','point_5','point_valid','time_horizon']
  _slot_types = ['std_msgs/Header','uint8','mavros_msgs/PositionTarget','mavros_msgs/PositionTarget','mavros_msgs/PositionTarget','mavros_msgs/PositionTarget','mavros_msgs/PositionTarget','uint8[5]','float32[5]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,type,point_1,point_2,point_3,point_4,point_5,point_valid,time_horizon

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Trajectory, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.type is None:
        self.type = 0
      if self.point_1 is None:
        self.point_1 = mavros_msgs.msg.PositionTarget()
      if self.point_2 is None:
        self.point_2 = mavros_msgs.msg.PositionTarget()
      if self.point_3 is None:
        self.point_3 = mavros_msgs.msg.PositionTarget()
      if self.point_4 is None:
        self.point_4 = mavros_msgs.msg.PositionTarget()
      if self.point_5 is None:
        self.point_5 = mavros_msgs.msg.PositionTarget()
      if self.point_valid is None:
        self.point_valid = b'\0'*5
      if self.time_horizon is None:
        self.time_horizon = [0.] * 5
    else:
      self.header = std_msgs.msg.Header()
      self.type = 0
      self.point_1 = mavros_msgs.msg.PositionTarget()
      self.point_2 = mavros_msgs.msg.PositionTarget()
      self.point_3 = mavros_msgs.msg.PositionTarget()
      self.point_4 = mavros_msgs.msg.PositionTarget()
      self.point_5 = mavros_msgs.msg.PositionTarget()
      self.point_valid = b'\0'*5
      self.time_horizon = [0.] * 5

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
      _x = self
      buff.write(_get_struct_B3I().pack(_x.type, _x.point_1.header.seq, _x.point_1.header.stamp.secs, _x.point_1.header.stamp.nsecs))
      _x = self.point_1.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_1.coordinate_frame, _x.point_1.type_mask, _x.point_1.position.x, _x.point_1.position.y, _x.point_1.position.z, _x.point_1.velocity.x, _x.point_1.velocity.y, _x.point_1.velocity.z, _x.point_1.acceleration_or_force.x, _x.point_1.acceleration_or_force.y, _x.point_1.acceleration_or_force.z, _x.point_1.yaw, _x.point_1.yaw_rate, _x.point_2.header.seq, _x.point_2.header.stamp.secs, _x.point_2.header.stamp.nsecs))
      _x = self.point_2.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_2.coordinate_frame, _x.point_2.type_mask, _x.point_2.position.x, _x.point_2.position.y, _x.point_2.position.z, _x.point_2.velocity.x, _x.point_2.velocity.y, _x.point_2.velocity.z, _x.point_2.acceleration_or_force.x, _x.point_2.acceleration_or_force.y, _x.point_2.acceleration_or_force.z, _x.point_2.yaw, _x.point_2.yaw_rate, _x.point_3.header.seq, _x.point_3.header.stamp.secs, _x.point_3.header.stamp.nsecs))
      _x = self.point_3.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_3.coordinate_frame, _x.point_3.type_mask, _x.point_3.position.x, _x.point_3.position.y, _x.point_3.position.z, _x.point_3.velocity.x, _x.point_3.velocity.y, _x.point_3.velocity.z, _x.point_3.acceleration_or_force.x, _x.point_3.acceleration_or_force.y, _x.point_3.acceleration_or_force.z, _x.point_3.yaw, _x.point_3.yaw_rate, _x.point_4.header.seq, _x.point_4.header.stamp.secs, _x.point_4.header.stamp.nsecs))
      _x = self.point_4.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_4.coordinate_frame, _x.point_4.type_mask, _x.point_4.position.x, _x.point_4.position.y, _x.point_4.position.z, _x.point_4.velocity.x, _x.point_4.velocity.y, _x.point_4.velocity.z, _x.point_4.acceleration_or_force.x, _x.point_4.acceleration_or_force.y, _x.point_4.acceleration_or_force.z, _x.point_4.yaw, _x.point_4.yaw_rate, _x.point_5.header.seq, _x.point_5.header.stamp.secs, _x.point_5.header.stamp.nsecs))
      _x = self.point_5.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f().pack(_x.point_5.coordinate_frame, _x.point_5.type_mask, _x.point_5.position.x, _x.point_5.position.y, _x.point_5.position.z, _x.point_5.velocity.x, _x.point_5.velocity.y, _x.point_5.velocity.z, _x.point_5.acceleration_or_force.x, _x.point_5.acceleration_or_force.y, _x.point_5.acceleration_or_force.z, _x.point_5.yaw, _x.point_5.yaw_rate))
      _x = self.point_valid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_5B().pack(*_x))
      else:
        buff.write(_get_struct_5s().pack(_x))
      buff.write(_get_struct_5f().pack(*self.time_horizon))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.point_1 is None:
        self.point_1 = mavros_msgs.msg.PositionTarget()
      if self.point_2 is None:
        self.point_2 = mavros_msgs.msg.PositionTarget()
      if self.point_3 is None:
        self.point_3 = mavros_msgs.msg.PositionTarget()
      if self.point_4 is None:
        self.point_4 = mavros_msgs.msg.PositionTarget()
      if self.point_5 is None:
        self.point_5 = mavros_msgs.msg.PositionTarget()
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
      _x = self
      start = end
      end += 13
      (_x.type, _x.point_1.header.seq, _x.point_1.header.stamp.secs, _x.point_1.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_1.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_1.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_1.coordinate_frame, _x.point_1.type_mask, _x.point_1.position.x, _x.point_1.position.y, _x.point_1.position.z, _x.point_1.velocity.x, _x.point_1.velocity.y, _x.point_1.velocity.z, _x.point_1.acceleration_or_force.x, _x.point_1.acceleration_or_force.y, _x.point_1.acceleration_or_force.z, _x.point_1.yaw, _x.point_1.yaw_rate, _x.point_2.header.seq, _x.point_2.header.stamp.secs, _x.point_2.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_2.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_2.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_2.coordinate_frame, _x.point_2.type_mask, _x.point_2.position.x, _x.point_2.position.y, _x.point_2.position.z, _x.point_2.velocity.x, _x.point_2.velocity.y, _x.point_2.velocity.z, _x.point_2.acceleration_or_force.x, _x.point_2.acceleration_or_force.y, _x.point_2.acceleration_or_force.z, _x.point_2.yaw, _x.point_2.yaw_rate, _x.point_3.header.seq, _x.point_3.header.stamp.secs, _x.point_3.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_3.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_3.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_3.coordinate_frame, _x.point_3.type_mask, _x.point_3.position.x, _x.point_3.position.y, _x.point_3.position.z, _x.point_3.velocity.x, _x.point_3.velocity.y, _x.point_3.velocity.z, _x.point_3.acceleration_or_force.x, _x.point_3.acceleration_or_force.y, _x.point_3.acceleration_or_force.z, _x.point_3.yaw, _x.point_3.yaw_rate, _x.point_4.header.seq, _x.point_4.header.stamp.secs, _x.point_4.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_4.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_4.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_4.coordinate_frame, _x.point_4.type_mask, _x.point_4.position.x, _x.point_4.position.y, _x.point_4.position.z, _x.point_4.velocity.x, _x.point_4.velocity.y, _x.point_4.velocity.z, _x.point_4.acceleration_or_force.x, _x.point_4.acceleration_or_force.y, _x.point_4.acceleration_or_force.z, _x.point_4.yaw, _x.point_4.yaw_rate, _x.point_5.header.seq, _x.point_5.header.stamp.secs, _x.point_5.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_5.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_5.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 83
      (_x.point_5.coordinate_frame, _x.point_5.type_mask, _x.point_5.position.x, _x.point_5.position.y, _x.point_5.position.z, _x.point_5.velocity.x, _x.point_5.velocity.y, _x.point_5.velocity.z, _x.point_5.acceleration_or_force.x, _x.point_5.acceleration_or_force.y, _x.point_5.acceleration_or_force.z, _x.point_5.yaw, _x.point_5.yaw_rate,) = _get_struct_BH9d2f().unpack(str[start:end])
      start = end
      end += 5
      self.point_valid = str[start:end]
      start = end
      end += 20
      self.time_horizon = _get_struct_5f().unpack(str[start:end])
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
      _x = self
      buff.write(_get_struct_B3I().pack(_x.type, _x.point_1.header.seq, _x.point_1.header.stamp.secs, _x.point_1.header.stamp.nsecs))
      _x = self.point_1.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_1.coordinate_frame, _x.point_1.type_mask, _x.point_1.position.x, _x.point_1.position.y, _x.point_1.position.z, _x.point_1.velocity.x, _x.point_1.velocity.y, _x.point_1.velocity.z, _x.point_1.acceleration_or_force.x, _x.point_1.acceleration_or_force.y, _x.point_1.acceleration_or_force.z, _x.point_1.yaw, _x.point_1.yaw_rate, _x.point_2.header.seq, _x.point_2.header.stamp.secs, _x.point_2.header.stamp.nsecs))
      _x = self.point_2.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_2.coordinate_frame, _x.point_2.type_mask, _x.point_2.position.x, _x.point_2.position.y, _x.point_2.position.z, _x.point_2.velocity.x, _x.point_2.velocity.y, _x.point_2.velocity.z, _x.point_2.acceleration_or_force.x, _x.point_2.acceleration_or_force.y, _x.point_2.acceleration_or_force.z, _x.point_2.yaw, _x.point_2.yaw_rate, _x.point_3.header.seq, _x.point_3.header.stamp.secs, _x.point_3.header.stamp.nsecs))
      _x = self.point_3.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_3.coordinate_frame, _x.point_3.type_mask, _x.point_3.position.x, _x.point_3.position.y, _x.point_3.position.z, _x.point_3.velocity.x, _x.point_3.velocity.y, _x.point_3.velocity.z, _x.point_3.acceleration_or_force.x, _x.point_3.acceleration_or_force.y, _x.point_3.acceleration_or_force.z, _x.point_3.yaw, _x.point_3.yaw_rate, _x.point_4.header.seq, _x.point_4.header.stamp.secs, _x.point_4.header.stamp.nsecs))
      _x = self.point_4.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f3I().pack(_x.point_4.coordinate_frame, _x.point_4.type_mask, _x.point_4.position.x, _x.point_4.position.y, _x.point_4.position.z, _x.point_4.velocity.x, _x.point_4.velocity.y, _x.point_4.velocity.z, _x.point_4.acceleration_or_force.x, _x.point_4.acceleration_or_force.y, _x.point_4.acceleration_or_force.z, _x.point_4.yaw, _x.point_4.yaw_rate, _x.point_5.header.seq, _x.point_5.header.stamp.secs, _x.point_5.header.stamp.nsecs))
      _x = self.point_5.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH9d2f().pack(_x.point_5.coordinate_frame, _x.point_5.type_mask, _x.point_5.position.x, _x.point_5.position.y, _x.point_5.position.z, _x.point_5.velocity.x, _x.point_5.velocity.y, _x.point_5.velocity.z, _x.point_5.acceleration_or_force.x, _x.point_5.acceleration_or_force.y, _x.point_5.acceleration_or_force.z, _x.point_5.yaw, _x.point_5.yaw_rate))
      _x = self.point_valid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_5B().pack(*_x))
      else:
        buff.write(_get_struct_5s().pack(_x))
      buff.write(self.time_horizon.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.point_1 is None:
        self.point_1 = mavros_msgs.msg.PositionTarget()
      if self.point_2 is None:
        self.point_2 = mavros_msgs.msg.PositionTarget()
      if self.point_3 is None:
        self.point_3 = mavros_msgs.msg.PositionTarget()
      if self.point_4 is None:
        self.point_4 = mavros_msgs.msg.PositionTarget()
      if self.point_5 is None:
        self.point_5 = mavros_msgs.msg.PositionTarget()
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
      _x = self
      start = end
      end += 13
      (_x.type, _x.point_1.header.seq, _x.point_1.header.stamp.secs, _x.point_1.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_1.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_1.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_1.coordinate_frame, _x.point_1.type_mask, _x.point_1.position.x, _x.point_1.position.y, _x.point_1.position.z, _x.point_1.velocity.x, _x.point_1.velocity.y, _x.point_1.velocity.z, _x.point_1.acceleration_or_force.x, _x.point_1.acceleration_or_force.y, _x.point_1.acceleration_or_force.z, _x.point_1.yaw, _x.point_1.yaw_rate, _x.point_2.header.seq, _x.point_2.header.stamp.secs, _x.point_2.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_2.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_2.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_2.coordinate_frame, _x.point_2.type_mask, _x.point_2.position.x, _x.point_2.position.y, _x.point_2.position.z, _x.point_2.velocity.x, _x.point_2.velocity.y, _x.point_2.velocity.z, _x.point_2.acceleration_or_force.x, _x.point_2.acceleration_or_force.y, _x.point_2.acceleration_or_force.z, _x.point_2.yaw, _x.point_2.yaw_rate, _x.point_3.header.seq, _x.point_3.header.stamp.secs, _x.point_3.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_3.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_3.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_3.coordinate_frame, _x.point_3.type_mask, _x.point_3.position.x, _x.point_3.position.y, _x.point_3.position.z, _x.point_3.velocity.x, _x.point_3.velocity.y, _x.point_3.velocity.z, _x.point_3.acceleration_or_force.x, _x.point_3.acceleration_or_force.y, _x.point_3.acceleration_or_force.z, _x.point_3.yaw, _x.point_3.yaw_rate, _x.point_4.header.seq, _x.point_4.header.stamp.secs, _x.point_4.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_4.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_4.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 95
      (_x.point_4.coordinate_frame, _x.point_4.type_mask, _x.point_4.position.x, _x.point_4.position.y, _x.point_4.position.z, _x.point_4.velocity.x, _x.point_4.velocity.y, _x.point_4.velocity.z, _x.point_4.acceleration_or_force.x, _x.point_4.acceleration_or_force.y, _x.point_4.acceleration_or_force.z, _x.point_4.yaw, _x.point_4.yaw_rate, _x.point_5.header.seq, _x.point_5.header.stamp.secs, _x.point_5.header.stamp.nsecs,) = _get_struct_BH9d2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.point_5.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.point_5.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 83
      (_x.point_5.coordinate_frame, _x.point_5.type_mask, _x.point_5.position.x, _x.point_5.position.y, _x.point_5.position.z, _x.point_5.velocity.x, _x.point_5.velocity.y, _x.point_5.velocity.z, _x.point_5.acceleration_or_force.x, _x.point_5.acceleration_or_force.y, _x.point_5.acceleration_or_force.z, _x.point_5.yaw, _x.point_5.yaw_rate,) = _get_struct_BH9d2f().unpack(str[start:end])
      start = end
      end += 5
      self.point_valid = str[start:end]
      start = end
      end += 20
      self.time_horizon = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=5)
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
_struct_5B = None
def _get_struct_5B():
    global _struct_5B
    if _struct_5B is None:
        _struct_5B = struct.Struct("<5B")
    return _struct_5B
_struct_5f = None
def _get_struct_5f():
    global _struct_5f
    if _struct_5f is None:
        _struct_5f = struct.Struct("<5f")
    return _struct_5f
_struct_5s = None
def _get_struct_5s():
    global _struct_5s
    if _struct_5s is None:
        _struct_5s = struct.Struct("<5s")
    return _struct_5s
_struct_B3I = None
def _get_struct_B3I():
    global _struct_B3I
    if _struct_B3I is None:
        _struct_B3I = struct.Struct("<B3I")
    return _struct_B3I
_struct_BH9d2f = None
def _get_struct_BH9d2f():
    global _struct_BH9d2f
    if _struct_BH9d2f is None:
        _struct_BH9d2f = struct.Struct("<BH9d2f")
    return _struct_BH9d2f
_struct_BH9d2f3I = None
def _get_struct_BH9d2f3I():
    global _struct_BH9d2f3I
    if _struct_BH9d2f3I is None:
        _struct_BH9d2f3I = struct.Struct("<BH9d2f3I")
    return _struct_BH9d2f3I
