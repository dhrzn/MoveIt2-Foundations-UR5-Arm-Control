import rclpy
from rclpy.node import Node
from pymoveit2 import MoveIt2
from pymoveit2.robots import ur
import time

class controled_move(Node):
    def __init__(self):
        super().__init__('controled_move')

        self.moveit2 = MoveIt2(
            node=self,
            joint_names=ur.joint_names(),
            base_link_name=ur.base_link_name(),
            end_effector_name=ur.end_effector_name(),
            group_name=ur.MOVE_GROUP_ARM,
        )

        self.moveit2.max_velocity_scaling_factor = 0.1
        self.moveit2.max_acceleration_scaling_factor = 0.1

    # scaling factor is a multiplier on max speed — 0.1 means 10% of full speed
    # 1.0 = full speed, 0.5 = half speed, etc.


    def move_direction(self):
        time.sleep(5.0)

        # defining home pose
        self.moveit2.move_to_pose(
            position=[0.3, 0.0, 0.5],
            quat_xyzw=[0.0, 0.0, 0.0, 1.0],
        )
        self.moveit2.wait_until_executed()

        time.sleep(3.33)

        # moving 20cm forward in x direction in a straight line
        self.moveit2.move_to_pose(
            position=[0.5, 0.0, 0.5],
            quat_xyzw=[0.0, 0.0, 0.0, 1.0],
            cartesian=True,
            cartesian_max_step=0.01,
        )
        self.moveit2.wait_until_executed()

# cartesian=True forces the end effector to travel in a straight line
# instead of letting OMPL pick a random chaotic path through joint space
# cartesian_max_step=0.01 means MoveIt2 samples a point every 1cm along
# the straight line — more points = more precise, less drift off the line


def main(args=None):
    rclpy.init(args=args)
    node = controled_move()
    node.move_direction()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


#summary for cartesian=true
#it's telling MoveIt2 "don't let OMPL pick a random path, 
# force the end effector to travel in a straight line." 
# Instead of planning in joint space and ending up wherever, 
# it plans in Cartesian space and locks the path
#note: no matter what position you give, its path would always travel in a straight line