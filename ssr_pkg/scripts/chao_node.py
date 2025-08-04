#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String
from qq_msgs.msg import Carry

if __name__ == '__main__':
    try:
        # 初始化节点，命名为"chao_node"
        rospy.init_node('chao_node', anonymous=False)
        
        # 创建发布者，发布String类型消息到chao_topic话题，队列长度10
        pub = rospy.Publisher('chao_topic', Carry, queue_size=10)
        
        # 设置发布频率为1Hz
        rate = rospy.Rate(1)  # 1 Hz
        
        # 创建消息对象
        msg = Carry()
        msg.grade = "王者" 
        msg.star = 50
        msg.data = "test_chao"
        
        # 循环发布消息
        while not rospy.is_shutdown():
            # 发布消息
            pub.publish(msg)
            
            # 打印日志信息
            rospy.loginfo("Publishing: %s", msg.data)
            
            # 按照设定频率休眠
            rate.sleep()
            
    except rospy.ROSInterruptException:
        pass