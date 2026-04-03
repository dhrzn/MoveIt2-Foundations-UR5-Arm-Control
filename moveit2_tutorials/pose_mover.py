import rclpy
import time
from rclpy.node import Node
from pymoveit2 import MoveIt2
from pymoveit2.robots import ur

class PoseMover(Node):
    def __init__(self):
        super().__init__('pose_mover')
        
        self.moveit2 = MoveIt2(
            node=self,
            joint_names=ur.joint_names(),
            base_link_name=ur.base_link_name(),
            end_effector_name=ur.end_effector_name(),
            group_name=ur.MOVE_GROUP_ARM,
        )

    def move_to_pose(self):
        time.sleep(5.0)
    
    # Home - no rotation, straight down (our home position)
        self.moveit2.move_to_pose(
            position=[0.4, 0.0, 0.5],
            quat_xyzw=[0.0, 0.0, 0.0, 1.0],
        )
        self.moveit2.wait_until_executed()
    
    #waiting
        time.sleep(3.33)
    
    # Pose 1 - experimenting with x axis rotation at new position
        self.moveit2.move_to_pose(
            position=[0.5, 0.1, 0.2],
            quat_xyzw=[0.7071, 0.0, 0.0, 0.7071],
        )
        self.moveit2.wait_until_executed()

    #Pose 2 - experimenting with mixed orientation in space
        time.sleep(3.33)
        self.moveit2.move_to_pose(
            position=[0.0, 0.2, 0.5],
            quat_xyzw=[0.5, 0.0, 0.0, 0.866],
        )
        self.moveit2.wait_until_executed()

    #Pose 3 - testing y axis rotation at extended position
        time.sleep(3.33)
        self.moveit2.move_to_pose(
            position=[0.3, 0.3, 0.4],
            quat_xyzw=[0.0, 0.2839, 0.0, 0.9589]
        )
        self.moveit2.wait_until_executed()

    #pose 4 - final position (returning to neutral position)
        time.sleep(3.33)
        self.moveit2.move_to_pose(
            position=[0.333, 0.333, 0.333],
            quat_xyzw=[0.0, 0.0, 0.0, 1.0]
        )
        self.moveit2.wait_until_executed()




def main(args=None):
    rclpy.init(args=args)
    node = PoseMover()
    node.move_to_pose()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# analogy for self
#Your node is basically just a messenger. It says to move_group "hey, I want the group called MOVE_GROUP_ARM, with joints called these names, with base link called this, with end effector called this — please move to this pose." And move_group goes "okay I recognize all those names, I know exactly what you're talking about, let me handle the actual planning."
# QUATERNION RULE: x² + y² + z² + w² must always equal 1.0
# This ensures pure rotation with no scaling of the coordinate frame
# Example check - Pose 2: 0.5² + 0.0² + 0.0² + 0.866² = 0.999 ≈ 1.0 