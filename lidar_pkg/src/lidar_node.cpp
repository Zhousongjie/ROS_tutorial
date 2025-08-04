#include <ros/ros.h>                  // ROS核心库头文件
#include <std_msgs/String.h>          // 标准字符串消息类型
#include <sensor_msgs/LaserScan.h>    // 激光雷达扫描数据类型
#include <geometry_msgs/Twist.h>      // 速度控制消息类型

ros::Publisher vel_pub;               // 声明速度指令发布器
static int nCount = 0;                // 状态保持计数器（控制转向持续时间）

// 激光雷达数据回调函数（每当收到/scan话题消息时触发）
void LidarCallback(const sensor_msgs::LaserScan msg)
{
    int nNum = msg.ranges.size();     // 获取激光点数量（通常为360或720）
    
    int nMid = nNum/2;                // 计算正前方激光点索引
    float fMidDist = msg.ranges[nMid];// 获取正前方障碍物距离
    ROS_INFO("前方测距 ranges[%d] = %f 米", nMid, fMidDist); // 打印测距信息

    // 转向状态保持逻辑（避免频繁转向）
    if(nCount > 0)
    {
        nCount--;                     // 计数器递减
        return;                       // 继续执行上一次转向指令
    }

    geometry_msgs::Twist vel_cmd;     // 创建速度指令消息
    if(fMidDist < 1.5f)               // 当前方障碍物小于1.5米时
    {
        vel_cmd.angular.z = 0.3;      // 设置角速度（顺时针旋转）
        nCount = 50;                  // 设置转向持续时间（约5秒）
    }
    else                              // 当前方无障碍物时
    {
        vel_cmd.linear.x = 0.05;      // 设置线速度（前进）
    }
    vel_pub.publish(vel_cmd);         // 发布速度指令到/cmd_vel话题
}

int main(int argc, char** argv)
{
    setlocale(LC_ALL,"");             // 设置中文输出环境
    ros::init(argc,argv,"lidar_node");// 初始化ROS节点，命名为lidar_node
    
    ros::NodeHandle n;                // 创建节点句柄
    // 订阅/scan话题，注册回调函数，队列长度10
    ros::Subscriber lidar_sub = n.subscribe("/scan", 10, &LidarCallback);
    // 创建/cmd_vel话题发布器，队列长度10
    vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel",10);

    ros::spin();                      // 进入循环等待回调（阻塞模式）
}