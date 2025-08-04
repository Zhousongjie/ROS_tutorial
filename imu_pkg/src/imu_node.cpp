#include "ros/ros.h"
#include "sensor_msgs/Imu.h"
#include "tf/tf.h"
#include "geometry_msgs/Twist.h"

// 速度消息发布对象（全局变量）
ros::Publisher vel_pub;

// IMU 回调函数
void IMUCallback(const sensor_msgs::Imu msg)
{
    // 检测消息包中四元数数据是否存在
    if(msg.orientation_covariance[0] < 0)
        return;
    // 四元数转成欧拉角
    tf::Quaternion quaternion(
        msg.orientation.x,
        msg.orientation.y,
        msg.orientation.z,
        msg.orientation.w
    );
    double roll, pitch, yaw;
    tf::Matrix3x3(quaternion).getRPY(roll, pitch, yaw);
    // 弧度换算成角度
    roll = roll*180/M_PI;
    pitch = pitch*180/M_PI;
    yaw = yaw*180/M_PI;
    ROS_INFO("滚转= %.0f 俯仰= %.0f 朝向= %.0f", roll, pitch, yaw);
    // 速度消息包
    geometry_msgs::Twist vel_cmd;
    // 目标朝向角
    double target_yaw = 90;
    // 计算速度
    double diff_angle = target_yaw - yaw;
    vel_cmd.angular.z = diff_angle * 0.01;
    vel_cmd.linear.x = 0.1;
    vel_pub.publish(vel_cmd);
}

int main(int argc, char **argv)
{
    setlocale(LC_ALL, "");
    ros::init(argc,argv, "imu_node"); 

    ros::NodeHandle n;
    // 订阅 IMU 的数据话题
    ros::Subscriber sub = n.subscribe("imu/data", 100, IMUCallback);
    // 发布速度控制话题
    vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel",10);
    ros::spin();

    return 0;
}
