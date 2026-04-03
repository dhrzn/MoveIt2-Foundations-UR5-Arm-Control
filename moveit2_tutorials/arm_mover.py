import rclpy
from rclpy.node import Node

# pymoveit2 is just a lightweight client that places "orders" on the already running move_group
# removed MoveItPy because it tries to spin up its own complete MoveIt2 instance rather than
# connecting to the already running ur_moveit_config stack
from pymoveit2 import MoveIt2

# ur module is a pre-built file with all UR robot specific constants already defined
# (joint names, link names, group names) so we dont have to look them up manually
# note: its just "ur" not "ur5" in this version of pymoveit2
from pymoveit2.robots import ur

def main():
    # turn on ROS2 communication - must always be first in any ROS2 python script
    rclpy.init()

    # create our node - this is what lives in the ROS2 network and communicates
    node = Node("arm_mover")

    # create the MoveIt2 client - this is our "remote control" that connects to
    # the already running move_group node from the ur_moveit_config launch file
    # we pass it UR specific constants so it knows which joints and links to control
    moveit2 = MoveIt2(
        node=node,
        joint_names=ur.joint_names(),           # the names of all UR arm joints
        base_link_name=ur.base_link_name(),     # the root/base link of the arm
        end_effector_name=ur.end_effector_name(), # the tip of the arm we are controlling
        group_name=ur.MOVE_GROUP_ARM,         # the planning group name from the SRDF
    )

    # define the "up" pose as joint angles in radians
    # these are the 6 joint angles (one per joint) that put the arm straight up
    # radians are used because thats how ROS2 and MoveIt2 measure joint positions
    up_position = [0.0, -1.5708, 0.0, -3.1416, 0.0, 0.0]

    # send the goal to move_group - this triggers the full pipeline:
    # move_group receives goal -> OMPL plans trajectory -> ros2_control executes -> gazebo simulates
    node.get_logger().info("Sending move command to move_group...")
    moveit2.move_to_configuration(joint_positions=up_position)

    # wait here until the arm finishes moving before continuing
    moveit2.wait_until_executed()

    node.get_logger().info("Motion complete!")

    # shut down ROS2 communication cleanly when done
    rclpy.shutdown()

if __name__ == "__main__":
    main()
