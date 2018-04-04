#include "ros/ros.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "console_logger");
    ROS_DEBUG("A debug message");
    ROS_INFO("An info message");
    return 0;
}
