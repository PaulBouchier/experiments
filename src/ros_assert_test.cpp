#include "ros/ros.h"
#include "ros/assert.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "asserter");
    ros::NodeHandle nh;

#ifdef NDEBUG
    ROS_INFO("NDEBUG is defined");
#endif

    ROS_INFO("aiming at the assert");

    // style 1
    ROS_ASSERT(false);

    // style 2
    int x = 5;
    ROS_ASSERT_MSG(6 < x, "Oops - intentionally hit an assert where 6 not less than %d", x);

    ROS_INFO("went past the assert");

    return 0;
}
