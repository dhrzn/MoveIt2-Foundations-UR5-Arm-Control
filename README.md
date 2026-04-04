# MoveIt2 Tutorials — UR5 Arm Control

ROS2 Jazzy + MoveIt2 package for controlling a simulated UR5 robot arm using pymoveit2. Built as part of a robotics software engineering learning path toward dual-arm origami folding research.

## Environment

- Ubuntu 24.04
- ROS2 Jazzy
- Gazebo Harmonic
- MoveIt2
- pymoveit2

## Nodes

### arm_mover.py

Commands the UR5 to joint angle configurations in radians using pymoveit2.

**Run:**
```
ros2 run moveit2_tutorials arm_mover
```

### pose_mover.py

Commands the UR5 to XYZ positions in 3D space with quaternion orientations. Executes a choreographed 5-pose sequence demonstrating position and orientation control.

**Run:**
```
ros2 run moveit2_tutorials pose_mover
```

### cartesian_mover.py

Commands the UR5 to move in a guaranteed straight line between positions using Cartesian path planning. Instead of letting OMPL pick a random path through joint space, cartesian=True forces the end effector to travel linearly. Uses a max_step of 0.01m (1cm) for precise interpolation along the path.

**Run:**
```
ros2 run moveit2_tutorials cartesian_mover
```

## Launch Simulation
```
ros2 launch ur_simulation_gz ur_sim_moveit.launch.py ur_type:=ur5
```

## Demo

My.Movie.12.mov

## Key Concepts

- Joint space vs Cartesian space control
- Quaternion orientation (x, y, z, w) — unit quaternion rule: x² + y² + z² + w² = 1.0
- MoveIt2 pipeline: pymoveit2 → move_group → OMPL → ros2_control → Gazebo
- Cartesian path planning: cartesian=True forces straight line end effector motion instead of unpredictable OMPL paths
## Demo



https://github.com/user-attachments/assets/7e2328d4-c468-473c-830e-42f12e2d8230
