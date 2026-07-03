<div align="center">

# TurtleBot2.5 Robotics Challenge Framework

[![English](https://img.shields.io/badge/Language-English-blue)](README.md)
[![日本語](https://img.shields.io/badge/言語-日本語-red)](README_JP.md)

Framework for the TurtleBot2.5 ROS 2 autonomous robotics challenge.

</div>

---
This repository contains the software for the **TurtleBot2.5 Challenge**, a robotics activity where teams program a TurtleBot2 equipped with a Crane+ robotic arm to autonomously complete a sequence of tasks.

The project is designed for beginners learning ROS 2 while introducing concepts such as autonomous navigation, robot manipulation, and modular software design.

---

## Robot Platform

The TurtleBot2.5 consists of:

- TurtleBot2 mobile base (Kobuki)
- Crane+ 5-DOF robotic arm
- ROS 2 software stack

During the challenge, competitors write a sequence of commands that control both the mobile base and the robotic arm.

---

## Repository Structure

```
src/
├── crane_and_turtle_pkg/
│   ├── arm.py
│   ├── base.py
│   ├── robot.py
│   ├── poses.py
│   ├── challenge_node.py
│   ├── gui.py
│   └── crane_driver_node.py
│
└── turtlebot2_ros2/
```

### Package Overview

| File | Purpose |
|------|---------|
| `challenge_node.py` | Main program that teams edit during the competition |
| `robot.py` | Combines the arm and base controllers |
| `arm.py` | High-level Crane+ arm controller |
| `base.py` | High-level TurtleBot2 base controller |
| `poses.py` | Predefined arm poses |
| `gui.py` | GUI for testing and manually controlling the robot |
| `crane_driver_node.py` | Low-level Dynamixel driver |

---

## Building

From the workspace:

```bash
cd ~/ros2_crane_and_turtle_ws

colcon build --symlink-install

source install/setup.bash
```

---

## Running the Robot

Start the required hardware drivers.

In one terminal, run the Kobuki launch file: 
```bash
ros2 run kobuki_node kobuki_ros_node --ros-args -p device_port:=/dev/ttyUSB0
```

or

```bash
ros2 launch kobuki_node kobuki_node-launch.py device:=/dev/kobuki
```

In another terminal, run the driver for the Crane Plus arm: 
```bash
ros2 run crane_and_turtle_pkg driver_node
```



Then run the challenge program:

```bash
ros2 run crane_and_turtle_pkg challenge_node
```

---

## GUI

The GUI can be used to:

- Test individual arm movements
- Move joints manually
- Test autonomous arm actions
- Test TurtleBot base movements
- Verify hardware before running the challenge

Launch the GUI with:

```bash
ros2 run crane_and_turtle_pkg gui
```

---

## Programming the Challenge

Teams should only modify:

```
challenge_node.py
```

The provided framework contains high-level commands for both the mobile base and the robotic arm.

### Base Commands

```python
self.robot.base.forward(distance_m)
self.robot.base.backward(distance_m)

self.robot.base.left(angle_deg)
self.robot.base.right(angle_deg)

self.robot.base.wait(seconds)
```

### Arm Commands

```python
self.robot.arm.home()

self.robot.arm.pick_can()

self.robot.arm.lift()

self.robot.arm.place_left()

self.robot.arm.place_right()

self.robot.arm.catapult()
```

---

## Example

```python
self.robot.arm.home()

self.robot.base.forward(1.0)

self.robot.base.left(90)

self.robot.base.forward(0.5)

self.robot.base.backward(0.5)
```

---

## Competition

The specific challenge objectives, scoring rules, obstacle course, and competition requirements will be provided separately.

Teams are encouraged to:

- Test frequently
- Record successful movement distances and angles
- Build their solution incrementally
- Work together to improve reliability

Good luck and have fun!
