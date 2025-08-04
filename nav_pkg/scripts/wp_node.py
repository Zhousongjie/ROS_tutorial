#!/usr/bin/env python3
#coding=utf-8

"""
wp_node.py - Python 版本的导航点控制节点

功能：
1. 发布导航点编号到 /waterplus/navi_waypoint 话题
2. 订阅 /waterplus/navi_result 话题的导航结果
3. 收到结果时打印警告信息
"""

import rospy
from std_msgs.msg import String
import time

def nav_result_callback(msg):
    """
    导航结果回调函数
    
    参数:
        msg (std_msgs/String): 从 /waterplus/navi_result 话题接收到的消息
    """
    rospy.logwarn("[NavResultCallback] %s", msg.data)


def main():
    """
    主函数 - 初始化节点并执行导航点发布
    """
    # 初始化 ROS 节点，名称为 "wp_node"
    rospy.init_node('wp_node', anonymous=False)
    
    # 创建节点句柄 (NodeHandle)
    # 在 rospy 中，通常直接使用全局命名空间，所以不需要显式创建
    # 但为了代码清晰，我们保留这个概念
    
    # 创建发布者：发布 String 消息到 /waterplus/navi_waypoint 话题
    # 队列大小为 10
    nav_pub = rospy.Publisher('/waterplus/navi_waypoint', String, queue_size=10)
    
    # 创建订阅者：订阅 /waterplus/navi_result 话题
    # 当收到消息时，调用 nav_result_callback 函数
    # 队列大小为 10
    res_sub = rospy.Subscriber('/waterplus/navi_result', String, nav_result_callback, queue_size=10)
    
    # 等待 1 秒，确保发布者有时间建立连接
    # 在 rospy 中，使用 rospy.sleep() 更符合 Python 风格
    rospy.sleep(1.0)
    
    # 创建要发布的消息
    nav_msg = String()
    nav_msg.data = "3"  # 设置导航点编号为 "2"
    
    # 发布消息
    nav_pub.publish(nav_msg)
    
    # 打印发布信息
    rospy.loginfo("Published waypoint: %s", nav_msg.data)
    
    # 进入主循环，处理回调函数
    # rospy.spin() 会保持节点运行，处理传入的消息
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass