// Generated by gencpp from file mavros_msgs/DebugValue.msg
// DO NOT EDIT!


#ifndef MAVROS_MSGS_MESSAGE_DEBUGVALUE_H
#define MAVROS_MSGS_MESSAGE_DEBUGVALUE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace mavros_msgs
{
template <class ContainerAllocator>
struct DebugValue_
{
  typedef DebugValue_<ContainerAllocator> Type;

  DebugValue_()
    : header()
    , index(0)
    , name()
    , value_float(0.0)
    , value_int(0)
    , data()
    , type(0)  {
    }
  DebugValue_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , index(0)
    , name(_alloc)
    , value_float(0.0)
    , value_int(0)
    , data(_alloc)
    , type(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _index_type;
  _index_type index;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef float _value_float_type;
  _value_float_type value_float;

   typedef int32_t _value_int_type;
  _value_int_type value_int;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _data_type;
  _data_type data;

   typedef uint8_t _type_type;
  _type_type type;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(TYPE_DEBUG)
  #undef TYPE_DEBUG
#endif
#if defined(_WIN32) && defined(TYPE_DEBUG_VECT)
  #undef TYPE_DEBUG_VECT
#endif
#if defined(_WIN32) && defined(TYPE_DEBUG_ARRAY)
  #undef TYPE_DEBUG_ARRAY
#endif
#if defined(_WIN32) && defined(TYPE_NAMED_VALUE_FLOAT)
  #undef TYPE_NAMED_VALUE_FLOAT
#endif
#if defined(_WIN32) && defined(TYPE_NAMED_VALUE_INT)
  #undef TYPE_NAMED_VALUE_INT
#endif

  enum {
    TYPE_DEBUG = 0u,
    TYPE_DEBUG_VECT = 1u,
    TYPE_DEBUG_ARRAY = 2u,
    TYPE_NAMED_VALUE_FLOAT = 3u,
    TYPE_NAMED_VALUE_INT = 4u,
  };


  typedef boost::shared_ptr< ::mavros_msgs::DebugValue_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mavros_msgs::DebugValue_<ContainerAllocator> const> ConstPtr;

}; // struct DebugValue_

typedef ::mavros_msgs::DebugValue_<std::allocator<void> > DebugValue;

typedef boost::shared_ptr< ::mavros_msgs::DebugValue > DebugValuePtr;
typedef boost::shared_ptr< ::mavros_msgs::DebugValue const> DebugValueConstPtr;

// constants requiring out of line definition

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mavros_msgs::DebugValue_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mavros_msgs::DebugValue_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mavros_msgs::DebugValue_<ContainerAllocator1> & lhs, const ::mavros_msgs::DebugValue_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.index == rhs.index &&
    lhs.name == rhs.name &&
    lhs.value_float == rhs.value_float &&
    lhs.value_int == rhs.value_int &&
    lhs.data == rhs.data &&
    lhs.type == rhs.type;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mavros_msgs::DebugValue_<ContainerAllocator1> & lhs, const ::mavros_msgs::DebugValue_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mavros_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::DebugValue_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::DebugValue_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::DebugValue_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::DebugValue_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::DebugValue_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::DebugValue_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mavros_msgs::DebugValue_<ContainerAllocator> >
{
  static const char* value()
  {
    return "af412ff7223c64155e7e3c6b7508eaaa";
  }

  static const char* value(const ::mavros_msgs::DebugValue_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xaf412ff7223c6415ULL;
  static const uint64_t static_value2 = 0x5e7e3c6b7508eaaaULL;
};

template<class ContainerAllocator>
struct DataType< ::mavros_msgs::DebugValue_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mavros_msgs/DebugValue";
  }

  static const char* value(const ::mavros_msgs::DebugValue_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mavros_msgs::DebugValue_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Msg for Debug MAVLink API\n"
"#\n"
"# Supported types:\n"
"# DEBUG			https://mavlink.io/en/messages/common.html#DEBUG\n"
"# DEBUG_VECTOR			https://mavlink.io/en/messages/common.html#DEBUG_VECT\n"
"# NAMED_VALUE_FLOAT		https://mavlink.io/en/messages/common.html#NAMED_VALUE_FLOAT\n"
"# NAMED_VALUE_INT		https://mavlink.io/en/messages/common.html#NAMED_VALUE_INT\n"
"# @TODO: add support for DEBUG_ARRAY (https://github.com/mavlink/mavlink/pull/734)\n"
"\n"
"std_msgs/Header header\n"
"\n"
"int32 index			# index value of DEBUG value (-1 if not indexed)\n"
"\n"
"string name			# value name/key\n"
"\n"
"float32 value_float		# float value for NAMED_VALUE_FLOAT and DEBUG\n"
"int32 value_int		# int value for NAMED_VALUE_INT\n"
"float32[] data			# DEBUG vector or array\n"
"\n"
"uint8 type\n"
"uint8 TYPE_DEBUG		= 0\n"
"uint8 TYPE_DEBUG_VECT		= 1\n"
"uint8 TYPE_DEBUG_ARRAY		= 2\n"
"uint8 TYPE_NAMED_VALUE_FLOAT	= 3\n"
"uint8 TYPE_NAMED_VALUE_INT	= 4\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::mavros_msgs::DebugValue_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mavros_msgs::DebugValue_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.index);
      stream.next(m.name);
      stream.next(m.value_float);
      stream.next(m.value_int);
      stream.next(m.data);
      stream.next(m.type);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DebugValue_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mavros_msgs::DebugValue_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mavros_msgs::DebugValue_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "index: ";
    Printer<int32_t>::stream(s, indent + "  ", v.index);
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "value_float: ";
    Printer<float>::stream(s, indent + "  ", v.value_float);
    s << indent << "value_int: ";
    Printer<int32_t>::stream(s, indent + "  ", v.value_int);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.data[i]);
    }
    s << indent << "type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.type);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MAVROS_MSGS_MESSAGE_DEBUGVALUE_H
