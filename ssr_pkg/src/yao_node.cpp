#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{
    // 设置环境变量，强制使用UTF-8编码
    setenv("LC_ALL", "en_US.UTF-8", 1);

    ros::init(argc, argv, "yao_node");
    ros::NodeHandle nh;
    
    // 创建一个发布者，发布std_msgs/String类型的消息到yao_topic话题，队列长度10
    ros::Publisher pub = nh.advertise<std_msgs::String>("yao_topic", 10);
    
    // 设置发布频率为1Hz
    ros::Rate rate(1);
    
    std_msgs::String msg;
    msg.data = "test_yao";
    
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