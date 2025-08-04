#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    try:
        # 初始化节点，名称为"yao_node"
        rospy.init_node('yao_node', anonymous=False)
        
        # 创建发布者：发布String类型消息到"yao_topic"话题，队列长度10
        pub = rospy.Publisher('yao_topic', String, queue_size=10)
        
        # 设置发布频率为1Hz（每秒发布1次）
        rate = rospy.Rate(1)
        
        # 创建消息对象并赋值
        msg = String()
        msg.data = "test_yao"
        
        # 循环发布消息（直到节点被关闭）
        while not rospy.is_shutdown():
            # 发布消息到话题
            pub.publish(msg)
            
            # 输出日志（类似C++的ROS_INFO）
            rospy.loginfo("Publishing: %s", msg.data)
            
            # 按照设定频率休眠（控制发布节奏）
            rate.sleep()
            
    # 捕获ROS中断异常（如Ctrl+C终止程序时）
    except rospy.ROSInterruptException:
        pass