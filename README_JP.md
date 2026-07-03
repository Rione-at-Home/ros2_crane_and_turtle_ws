<div align="center">

# TurtleBot2.5 Robotics Challenge Framework

[![English](https://img.shields.io/badge/Language-English-blue)](README.md)
[![日本語](https://img.shields.io/badge/言語-日本語-red)](README_JP.md)

TurtleBot2.5 ROS 2 自律ロボティクスチャレンジ用フレームワーク

</div>

このリポジトリは、**TurtleBot2.5 Robotics Challenge** 用に作成されたROS 2ソフトウェアフレームワークです。

TurtleBot2（Kobukiベース）とCrane+ 5自由度ロボットアームを組み合わせたロボットを制御し、自律走行やマニピュレーションを行うためのプログラムが含まれています。

本プロジェクトは、ROS 2を学び始めた学生でも扱いやすいように設計されています。

---

# ロボット構成

TurtleBot2.5は以下のハードウェアで構成されています。

- TurtleBot2（Kobuki）
- Crane+ 5自由度ロボットアーム
- ROS 2

競技では、ロボットベースとロボットアームの両方を制御するプログラムを作成します。

---

# ディレクトリ構成

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

## 各ファイルの説明

| ファイル | 内容 |
|----------|------|
| `challenge_node.py` | 競技で編集するメインプログラム |
| `robot.py` | アームとベースをまとめたクラス |
| `arm.py` | Crane+アームの高レベル制御 |
| `base.py` | TurtleBot2ベースの高レベル制御 |
| `poses.py` | アームのプリセット姿勢 |
| `gui.py` | ロボットの動作確認・手動操作用GUI |
| `crane_driver_node.py` | Dynamixelドライバ |

---

# ビルド方法

ワークスペースで以下を実行してください。

```bash
cd ~/ros2_crane_and_turtle_ws

colcon build --symlink-install

source install/setup.bash
```

---

# 実行方法

必要なハードウェアドライバを起動します。

1つ目のターミナルで、Kobukiの起動ファイルを親行します：
```bash
ros2 run kobuki_node kobuki_ros_node --ros-args -p device_port:=/dev/ttyUSB0
```

または

```bash
ros2 launch kobuki_node kobuki_node-launch.py device:=/dev/kobuki
```

2つ目のターミナルで、Crane Plusアームのドライバを起動します：
```bash
ros2 run crane_and_turtle_pkg driver_node
```

その後、チャレンジプログラムを実行します：

```bash
ros2 run crane_and_turtle_pkg challenge_node
```

---

# GUI

GUIでは以下のことができます。

- アームの各関節を個別に動かす
- アーム速度の変更
- プリセット動作の実行
- TurtleBotベースの移動テスト
- ロボットの動作確認

GUIの起動方法

```bash
ros2 run crane_and_turtle_pkg gui
```

---

# チャレンジプログラム

参加者が編集するファイルは

```
challenge_node.py
```

のみです。

このファイルから高レベルAPIを利用してロボットを制御します。

## ベース操作

```python
self.robot.base.forward(distance_m)
self.robot.base.backward(distance_m)

self.robot.base.left(angle_deg)
self.robot.base.right(angle_deg)

self.robot.base.wait(seconds)
```

## アーム操作

```python
self.robot.arm.home()

self.robot.arm.pick_can()

self.robot.arm.lift()

self.robot.arm.place_left()

self.robot.arm.place_right()

self.robot.arm.catapult()
```

---

# 使用例

```python
self.robot.arm.home()

self.robot.base.forward(1.0)

self.robot.base.left(90)

self.robot.base.forward(0.5)

self.robot.base.backward(0.5)
```

---

# 競技について

競技内容、得点方法、コースレイアウト、ルールなどは別途配布されます。

参加者は、

- 動作を少しずつ確認する
- 移動距離や旋回角度を記録する
- 少しずつプログラムを改善する
- チームで協力してロボットの精度を向上させる

ことをおすすめします。

---

頑張ってください！
