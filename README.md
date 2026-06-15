# Create UR5 & Robotiq85 USD

### 环境配置
- ubuntu24.04
- isaacsim 5.1

### isaacsim import urdf


### ur5 & robotiq85 connection


### make scene


### launch simulation by python script


### 说明
1. prepare urdf，这里UR5和robotiq85 urdf是分别导入isaac sim的, 需要在ros2环境中奖xacro转成urdf:
- xacro导出urdf
```
xacro robotiq_85_gripper_standalone.urdf.xacro > robotiq85.urdf # export robotiq85 urdf

xacro ur5_standalone.urdf.xacro > ur5.urdf # export ur5 urdf
```

- 将文件夹结构调整成：
```
/folder_name_A/
├── urdf_file
└── folder_name_B
    └── meshes
        ├── collision
        └── visual
```


### 参考
1. isaac sim官方教程：[Tutorial 6: Setup a Manipulator](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/tutorial_import_assemble_manipulator.html)

2. URDF代码仓库：[ur5_robotiq85_description
](git@github.com:WAI-f/ur5_robotiq85_description.git)