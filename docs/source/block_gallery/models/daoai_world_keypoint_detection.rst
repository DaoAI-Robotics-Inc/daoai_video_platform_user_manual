.. _daoai_world_keypoint_detection:

关键点检测模型 (Keypoint Detection)
====================================

.. note::
   本页面介绍DaoAI World模型的关键点检测类型。返回 :ref:`DaoAI World模型主页 <DaoAI World模型>`

模型简介
--------

关键点检测模型用于识别物体上的特定关键点位置，输出每个关键点的坐标和可见性信息。最常见的应用是人体姿态估计，但也可用于任何需要定位关键特征点的场景。

**输出内容：**

- **关键点坐标** (x, y)
- **关键点置信度/可见性** (0~1之间的浮点数)
- **物体边界框** (可选)
- **姿态骨架连接** (可选)

适用场景
--------

关键点检测模型适用于以下场景：

- **人体姿态估计**：健身动作识别、体态分析、动作捕捉
- **手势识别**：手部关键点检测、手语识别、AR交互
- **人脸关键点**：面部特征定位、表情识别、美颜滤镜
- **运动分析**：体育动作分析、步态识别、康复训练
- **工业检测**：零件关键点定位、装配引导
- **动物行为分析**：动物姿态跟踪、行为研究
- **车辆关键点**：车辆关键部位定位、损伤检测

输出格式
--------

关键点检测模型的输出包含检测到的所有实例及其关键点信息：

.. code-block:: json

   {
     "instances": [
       {
         "class": "person",
         "confidence": 0.95,
         "bbox": {
           "x": 100,
           "y": 50,
           "width": 200,
           "height": 400
         },
         "keypoints": [
           {
             "name": "nose",
             "x": 200,
             "y": 120,
             "confidence": 0.98,
             "visible": true
           },
           {
             "name": "left_eye",
             "x": 190,
             "y": 110,
             "confidence": 0.95,
             "visible": true
           },
           {
             "name": "right_eye",
             "x": 210,
             "y": 110,
             "confidence": 0.96,
             "visible": true
           },
           {
             "name": "left_shoulder",
             "x": 170,
             "y": 200,
             "confidence": 0.92,
             "visible": true
           },
           {
             "name": "right_shoulder",
             "x": 230,
             "y": 200,
             "confidence": 0.90,
             "visible": true
           }
         ],
         "skeleton": [
           ["nose", "left_eye"],
           ["nose", "right_eye"],
           ["left_shoulder", "right_shoulder"]
         ],
         "instance_id": 1
       }
     ],
     "count": 1
   }

**字段说明：**

- ``class``: 物体类别
- ``confidence``: 检测整体置信度
- ``bbox``: 物体边界框
- ``keypoints``: 关键点列表
  
  - ``name``: 关键点名称
  - ``x``, ``y``: 关键点坐标
  - ``confidence``: 该关键点的置信度
  - ``visible``: 关键点是否可见（未被遮挡）

- ``skeleton``: 骨架连接关系（定义哪些关键点之间有连接）
- ``instance_id``: 实例唯一标识符

常见关键点集合
--------------

**人体姿态关键点 (17点 - COCO格式)**

.. code-block:: text

   0: nose          (鼻子)
   1: left_eye      (左眼)
   2: right_eye     (右眼)
   3: left_ear      (左耳)
   4: right_ear     (右耳)
   5: left_shoulder (左肩)
   6: right_shoulder(右肩)
   7: left_elbow    (左肘)
   8: right_elbow   (右肘)
   9: left_wrist    (左腕)
   10: right_wrist  (右腕)
   11: left_hip     (左臀)
   12: right_hip    (右臀)
   13: left_knee    (左膝)
   14: right_knee   (右膝)
   15: left_ankle   (左踝)
   16: right_ankle  (右踝)

**手部关键点 (21点)**

手掌根部、5个手指各4个关节点

**人脸关键点 (68点/98点)**

面部轮廓、眉毛、眼睛、鼻子、嘴巴的特征点

配置示例
--------

**人体姿态检测**

.. code-block:: json

   {
     "step_name": "pose_estimation",
     "image": "input.image",
     "model_type": "keypoint_detection",
     "confidence": 0.5
   }

**高精度动作分析**

.. code-block:: json

   {
     "step_name": "fitness_pose_check",
     "image": "camera.frame",
     "model_type": "keypoint_detection",
     "confidence": 0.7,
     "label_confidence_thresholds": {
       "person": 0.8
     }
   }

**多人姿态检测**

.. code-block:: json

   {
     "step_name": "multi_person_pose",
     "image": "crowd.image",
     "model_type": "keypoint_detection",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "person": 0.7
     }
   }

使用技巧与最佳实践
------------------

1. **置信度阈值设置**
   
   - 整体检测置信度：0.5-0.7
   - 单个关键点置信度：0.3-0.5（关键点部分遮挡时会降低）
   - 关键应用（如医疗）：0.8-0.9

2. **处理遮挡情况**
   
   - 检查每个关键点的 ``visible`` 标志
   - 过滤掉 ``confidence`` 过低的关键点
   - 使用骨架连接关系推断被遮挡的关键点

3. **多人场景处理**
   
   - 通过 ``instance_id`` 区分不同的人
   - 使用边界框信息辅助追踪
   - 关注 ``count`` 字段获取总人数

4. **动作识别应用**
   
   - 计算关键点之间的角度判断姿态
   - 追踪关键点运动轨迹分析动作
   - 使用骨架长度比例进行姿态标准化

5. **性能优化**
   
   - 关键点检测计算量较大，建议使用GPU
   - 对于实时应用，可适当降低输入分辨率
   - 多人场景下性能随人数增加而降低

常见问题
--------

**Q: 关键点坐标是归一化的还是绝对坐标？**

A: 关键点坐标为绝对像素坐标，与输入图像尺寸对应。

**Q: 如何判断某个关键点是否被遮挡？**

A: 检查该关键点的 ``visible`` 标志和 ``confidence`` 值。如果 ``visible`` 为 false 或 ``confidence`` 很低（如<0.3），说明该点可能被遮挡。

**Q: 检测不到关键点怎么办？**

A: 可能的原因和解决方案：
   
   - 图像质量差：提高图像分辨率和清晰度
   - 姿态极端：确保训练数据包含各种姿态
   - 遮挡严重：降低关键点置信度阈值
   - 光照不佳：改善拍摄条件或使用数据增强

**Q: 如何计算两个关键点之间的角度？**

A: 使用三个关键点的坐标，通过向量夹角公式计算：

.. code-block:: python

   import math
   
   def calculate_angle(p1, p2, p3):
       """计算p1-p2-p3形成的角度"""
       v1 = (p1['x'] - p2['x'], p1['y'] - p2['y'])
       v2 = (p3['x'] - p2['x'], p3['y'] - p2['y'])
       
       dot = v1[0]*v2[0] + v1[1]*v2[1]
       len1 = math.sqrt(v1[0]**2 + v1[1]**2)
       len2 = math.sqrt(v2[0]**2 + v2[1]**2)
       
       angle = math.acos(dot / (len1 * len2))
       return math.degrees(angle)

**Q: 可以检测多个人吗？**

A: 可以。模型会为每个检测到的人输出独立的关键点集合，通过 ``instance_id`` 区分。

应用案例
--------

**案例1：健身动作检测**

检测用户的健身动作是否标准，如深蹲、俯卧撑等。

.. code-block:: json

   {
     "step_name": "fitness_coach",
     "model_type": "keypoint_detection",
     "confidence": 0.7
   }

**应用逻辑：**

1. 检测关键点位置
2. 计算关节角度（如膝盖角度、手臂角度）
3. 与标准动作对比
4. 给出实时反馈

**案例2：跌倒检测**

监测老人或患者的姿态，检测跌倒事件。

.. code-block:: json

   {
     "step_name": "fall_detection",
     "model_type": "keypoint_detection",
     "confidence": 0.6
   }

**检测逻辑：**

- 计算身体主轴（头部到臀部）与垂直方向的角度
- 如果角度>60度且头部高度低于臀部，触发跌倒警报

**案例3：手势识别**

识别手部关键点，实现手势控制。

.. code-block:: json

   {
     "step_name": "hand_gesture",
     "model_type": "keypoint_detection",
     "confidence": 0.7,
     "label_confidence_thresholds": {
       "hand": 0.75
     }
   }

**应用场景：**

- 非接触式界面控制
- 手语翻译
- AR/VR交互

**案例4：体育动作分析**

分析运动员的动作技术，用于训练改进。

.. code-block:: json

   {
     "step_name": "sports_analysis",
     "model_type": "keypoint_detection",
     "confidence": 0.8
   }

**分析内容：**

- 投篮/挥拍动作的标准性
- 跑步姿态分析
- 关节角度和运动轨迹追踪

性能参考
--------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - 场景
     - 推荐配置
     - 预期性能
   * - 单人实时检测
     - 640×480, GPU
     - 30+ FPS
   * - 多人场景（<5人）
     - 1280×720, GPU
     - 15-25 FPS
   * - 高精度分析
     - 1920×1080, GPU
     - 5-10 FPS

相关链接
--------

- :ref:`DaoAI World模型主页 <DaoAI World模型>`
- :ref:`目标检测模型 <daoai_world_object_detection>` - 先定位人物再检测关键点
- :ref:`实例分割模型 <daoai_world_instance_segmentation>` - 结合使用获得完整信息


