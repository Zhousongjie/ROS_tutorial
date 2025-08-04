#include <ros/ros.h>
#include <geometry_msgs/Twist.h>

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "vel_node");
    ros::NodeHandle n;
    ros::Publisher vel_pub = n.advertise<geometry_msgs::Twist>("cmd_vel", 10);

    geometry_msgs::Twist msg;
    msg.linear.x = 0;  // Set linear velocity
    msg.linear.y = 0;  // Set linear velocity
    msg.linear.z = 0;  // Set linear velocity
    msg.angular.x = 0.0; // Set angular velocity
    msg.angular.y = 0.0; // Set angular velocity
    msg.angular.z = 0.5; // Set angular velocity

    ros::Rate loop_rate(10); // 10 Hz
    while (ros::ok())
    {
        vel_pub.publish(msg); // Publish the message
        // ros::spinOnce(); // Allow callbacks to process
        loop_rate.sleep(); // Sleep to maintain the loop rate
    }   

    return 0;
}
