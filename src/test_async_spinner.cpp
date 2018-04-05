#include "ros/ros.h"
#include "std_msgs/String.h"
#include <boost/thread.hpp>

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("Subscriber callback: I heard %s", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "subscriber");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("chatter", 1000, chatterCallback);

  ros::AsyncSpinner spinner(1);
  spinner.start();

  while (ros::ok())
  {
      ROS_INFO("calling spingOnce()");
      //ros::spinOnce();
      ROS_INFO("sleeping after spinOnce");
      sleep(5);
  }

  return 0;
}
