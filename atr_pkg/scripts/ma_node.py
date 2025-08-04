#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String
from qq_msgs.msg import Carry

# 回调函数：处理chao_topic的消息（INFO级别日志）
def chao_messageCallback(msg):
    rospy.loginfo("接收到chao_topic消息: %s", msg.grade)
    rospy.loginfo("接收到chao_topic消息: %ld", msg.star)
    rospy.loginfo("接收到chao_topic消息: %s", msg.data)

# 回调函数：处理yao_topic的消息（WARN级别日志）
def yao_messageCallback(msg):
    rospy.logwarn("接收到yao_topic消息: %s", msg.data)

if __name__ == '__main__':
    try:
        # 初始化节点，名称为"ma_node"
        rospy.init_node('ma_node', anonymous=False)
        
        # 创建两个订阅者，分别绑定不同的回调函数
        rospy.Subscriber('chao_topic', Carry, chao_messageCallback)
        rospy.Subscriber('yao_topic', String, yao_messageCallback)
        
        # 进入循环等待回调（两种方式均可）
        # 方式一：使用spin()进入阻塞循环（更简洁）
        rospy.spin()
        
        # 方式二：手动循环调用spinOnce()（等价于C++版本）
        # while not rospy.is_shutdown():
        #     rospy.spinOnce()
            
    except rospy.ROSInterruptException:
        pass