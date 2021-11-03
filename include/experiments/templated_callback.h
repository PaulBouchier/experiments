#ifndef TEMPLATED_CALLBACK_H
#define TEMPLATED_CALLBACK_H

#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include "std_msgs/Int32.h"


#include <iostream>

namespace experiment {

class C
{
public:
    template <class T> void printMsg( T msg );
    void runTest();

    std_msgs::Int16 i16;
    std_msgs::Int32 i32;

};

template <class T>
inline void
C::printMsg( T msg )
{
    std::cout << msg.data << std::endl;
}

} // namespace

#endif
