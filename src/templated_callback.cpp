#include "experiments/templated_callback.h"

namespace experiment {

void C::runTest()
{
    ros::NodeHandle nh;

    ros::Subscriber int16Sub = nh.subscribe("topic1", 1, &C::printMsg<std_msgs::Int16>, this);
    ros::Subscriber int32Sub = nh.subscribe("topic2", 1, &C::printMsg<std_msgs::Int32>, this);

    ros::Publisher int16Pub = nh.advertise<std_msgs::Int16>("topic1", 1);
    ros::Publisher int32Pub = nh.advertise<std_msgs::Int32>("topic2", 1);

    sleep(1);

    i16.data = 16;
    i32.data = 32;

    int16Pub.publish(i16);
    int32Pub.publish(i32);
    ros::spinOnce();
    sleep(1);
    ros::spinOnce();

}

} // namespace

int main(int argc, char **argv)
{
    ros::init(argc, argv, "templated_callback");
    experiment::C c;
    c.runTest();
    return 0;
}


