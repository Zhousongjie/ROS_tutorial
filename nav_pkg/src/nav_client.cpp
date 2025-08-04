#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>

// 定义 MoveBaseAction 的简单客户端类型别名
typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

int main(int argc, char *argv[])
{
    // 初始化 ROS 节点
    ros::init(argc, argv, "nav_client");

    // 创建与 /move_base 动作服务器的连接
    MoveBaseClient ac("move_base", true);

    // 等待服务器启动
    while (!ac.waitForServer(ros::Duration(5.0)))
    {
        ROS_INFO("Waiting for the move_base action server to come up");
    }

    // 构造导航目标
    move_base_msgs::MoveBaseGoal goal;
    goal.target_pose.header.frame_id = "map";          // 使用 map 坐标系
    goal.target_pose.header.stamp = ros::Time::now();  // 当前时间戳
    goal.target_pose.pose.position.x = -3.0;           // 目标 x 坐标
    goal.target_pose.pose.position.y = 2.0;            // 目标 y 坐标
    goal.target_pose.pose.orientation.w = 1.0;         // 无旋转

    // 发送目标并等待结果
    ROS_INFO("Sending goal");
    ac.sendGoal(goal);
    ac.waitForResult();

    // 输出导航结果
    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
    {
        ROS_INFO("Reached the goal!");
    }
    else
    {
        ROS_ERROR("Failed to reach the goal.");
    }

    return 0;
}