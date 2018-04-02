#include "ros/ros.h"
#include "ros/assert.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "param_reader");
    ros::NodeHandle pnh("~");
    ros::NodeHandle myParamsNh("~/myParams");
    ros::NodeHandle yamlParamsNh("~/myYamlParams");

    ROS_INFO_STREAM("namespaces: \n~: " << pnh.getNamespace() << std::endl
                    << "myParamsNh: " << myParamsNh.getNamespace() << std::endl
                    << "myYamlParams: " << yamlParamsNh.getNamespace()
                    );

    std::string param1, param2, param3;

    if (pnh.hasParam("aPrivateParam")) {
        pnh.getParam("aPrivateParam", param1);
        ROS_INFO_STREAM("got a private param" << param1);
    }

    if (myParamsNh.hasParam("a2ndPrivateParam")) {
        myParamsNh.getParam("a2ndPrivateParam", param2);
        ROS_INFO_STREAM("got a 2nd private param " << param2);
    }

    std::map<std::string, std::string> yamlMap;
    if (yamlParamsNh.hasParam("Parameters")) {
        yamlParamsNh.getParam("Parameters", yamlMap);
        ROS_INFO_STREAM("yamlMap size: " << yamlMap.size());
        ROS_INFO_STREAM("got a yaml private param " << yamlMap["aFirstYamlParam"]);
        // This doesn't work
        yamlParamsNh.getParam("myYamlParams/Parameters/aFirstYamlParam", param3);
        ROS_INFO_STREAM("first yaml param got by name: " << param3);
    }

    return 0;
}
