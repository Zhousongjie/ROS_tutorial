#include <ros/ros.h>
#include <std_msgs/String.h>
#include <qq_msgs/Carry.h>

// 回调函数：处理接收到的消息
void chao_messageCallback(const qq_msgs::Carry& msg) {
    ROS_WARN("grade: %s",msg.grade.c_str());
    ROS_WARN("Star: %ld", msg.star);
    ROS_WARN("Data: %s", msg.data.c_str());
}

// 回调函数：处理接收到的消息
void yao_messageCallback(const std_msgs::String& msg) {
    ROS_WARN("Publishing:  %s\n", msg.data.c_str());
}

int main(int argc, char **argv) {
    // 设置环境变量，确保中文显示正常
    setenv("LC_ALL", "en_US.UTF-8", 1);
    
    ros::init(argc, argv, "ma_node");
    ros::NodeHandle nh;
    
    // 创建订阅者，订阅chao_topic话题，队列长度10，接收到消息时调用messageCallback函数
    ros::Subscriber sub_chao = nh.subscribe("chao_topic", 10, chao_messageCallback);
    ros::Subscriber sub_yao = nh.subscribe("yao_topic", 10, yao_messageCallback);
    
    // 进入循环等待回调
    // ros::spin();

    while(ros::ok())
    {
        ros::spinOnce();
    }
    
    return 0;
}