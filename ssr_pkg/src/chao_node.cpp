#include <ros/ros.h>
#include <std_msgs/String.h>
#include <qq_msgs/Carry.h>


int main(int argc, char *argv[])
{
    // 设置环境变量，强制使用UTF-8编码
    setenv("LC_ALL", "en_US.UTF-8", 1);

    ros::init(argc, argv, "chao_node");
    ros::NodeHandle nh;
    
    // 创建一个发布者，发布std_msgs/String类型的消息到chao_topic话题，队列长度10
    ros::Publisher pub = nh.advertise<qq_msgs::Carry>("chao_topic", 10);
    
    // 设置发布频率为1Hz
    ros::Rate rate(1);
    
    qq_msgs::Carry msg;
    msg.grade = "王者";
    msg.star = 1;
    msg.data = "test_chao";
    
    while (ros::ok())
    {
        // 发布消息
        pub.publish(msg);
        ROS_INFO("Publishing: %s", msg.data.c_str());
        // printf("刷屏\n");

        // 处理回调函数
        ros::spinOnce();
        
        // 按照设定频率休眠
        rate.sleep();
    }
    
    return 0;
}