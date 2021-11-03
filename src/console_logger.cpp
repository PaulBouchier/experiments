#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "console_logger");
  ros::NodeHandle nh;
  ROS_INFO("Starting console_logger");

  ros::Rate loop_rate(2);
  while (ros::ok())
  {
    ROS_ERROR("Error msg");
    ros::spinOnce();
    loop_rate.sleep();

    ROS_WARN("Warn msg");
    ros::spinOnce();
    loop_rate.sleep();

    ROS_INFO("Info msg");
    ros::spinOnce();
    loop_rate.sleep();

    ROS_DEBUG("Debug msg");
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
