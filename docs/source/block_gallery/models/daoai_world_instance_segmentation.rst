.. _daoai_world_instance_segmentation:

实例分割模型 (Instance Segmentation)
=====================================

.. note::
   本页面介绍DaoAI World模型的实例分割类型。返回 :ref:`DaoAI World模型主页 <DaoAI World模型>`

模型简介
--------

实例分割模型是目标检测的增强版本，不仅能识别物体并输出边界框，还能为每个物体实例生成精确的像素级分割掩码。这使得您可以获得物体的准确轮廓，而不仅仅是矩形框。

**输出内容：**

- **边界框坐标** (x, y, width, height)
- **类别标签** (如：car, person, dog等)
- **置信度分数** (0~1之间的浮点数)
- **分割掩码** (像素级的二值掩码或多边形轮廓)

适用场景
--------

实例分割模型适用于以下需要精确物体轮廓的场景：

- **图像编辑**：背景替换、物体抠图、自动合成
- **医学影像**：器官分割、肿瘤轮廓提取
- **自动驾驶**：车道线检测、车辆精确定位
- **机器人视觉**：物体抓取、障碍物规避
- **精确计数**：物体重叠场景的准确计数
- **面积测量**：物体面积、尺寸的精确计算
- **3D重建**：物体轮廓作为3D建模的输入

输出格式
--------

实例分割模型的输出包含检测信息和分割掩码：

.. code-block:: json

   {
     "instances": [
       {
         "class": "person",
         "confidence": 0.92,
         "bbox": {
           "x": 100,
           "y": 50,
           "width": 150,
           "height": 300
         },
         "mask": {
           "type": "polygon",
           "points": [[120, 80], [180, 75], [200, 150], ...]
         },
         "area": 28500,
         "instance_id": 1
       },
       {
         "class": "car",
         "confidence": 0.88,
         "bbox": {
           "x": 300,
           "y": 200,
           "width": 250,
           "height": 180
         },
         "mask": {
           "type": "rle",
           "data": "encoded_mask_data"
         },
         "area": 35200,
         "instance_id": 2
       }
     ],
     "count": 2
   }

**字段说明：**

- ``class``: 物体类别
- ``confidence``: 检测置信度
- ``bbox``: 边界框坐标
- ``mask``: 分割掩码数据
  
  - ``type``: 掩码格式（polygon多边形 或 rle游程编码）
  - ``points``: 多边形顶点坐标列表（polygon格式）
  - ``data``: RLE编码的掩码数据（rle格式）

- ``area``: 分割区域的像素面积
- ``instance_id``: 实例唯一标识符

配置示例
--------

**基础配置**

.. code-block:: json

   {
     "step_name": "instance_seg",
     "image": "input.image",
     "model_type": "instance_segmentation",
     "confidence": 0.5
   }

**高精度场景**

适用于需要精确分割的场景，如医学影像：

.. code-block:: json

   {
     "step_name": "medical_segmentation",
     "image": "medical.scan",
     "model_type": "instance_segmentation",
     "confidence": 0.8,
     "label_confidence_thresholds": {
       "tumor": 0.9,
       "organ": 0.85
     }
   }

**多类别物体分割**

.. code-block:: json

   {
     "step_name": "multi_object_seg",
     "image": "camera.frame",
     "model_type": "instance_segmentation",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "person": 0.7,
       "car": 0.65,
       "bicycle": 0.6,
       "dog": 0.7
     }
   }

使用技巧与最佳实践
------------------

1. **掩码格式选择**
   
   - **Polygon（多边形）**：适合轮廓简单的物体，数据量小，易于可视化
   - **RLE（游程编码）**：适合复杂轮廓，保留更多细节，但数据量较大

2. **置信度阈值调整**
   
   - 初始建议值：0.5-0.6
   - 高精度需求（如医疗）：0.8-0.9
   - 实时应用：0.5-0.7（平衡速度和精度）

3. **处理遮挡场景**
   
   - 实例分割能区分重叠物体的不同实例
   - 通过 ``instance_id`` 追踪每个独立的物体实例
   - 使用 ``area`` 字段过滤部分遮挡的物体

4. **性能优化**
   
   - 实例分割比目标检测计算量更大
   - 高分辨率图像建议使用GPU加速
   - 考虑降低输入分辨率以提升速度

5. **后处理技巧**
   
   - 对掩码进行形态学操作（膨胀、腐蚀）优化边缘
   - 使用面积阈值过滤过小的检测结果
   - 合并相邻的同类实例（如需要）

常见问题
--------

**Q: 实例分割和语义分割有什么区别？**

A: 
   - **实例分割**：区分同类物体的不同实例（如3辆车会被标记为car_1, car_2, car_3）
   - **语义分割**：只区分类别（如3辆车都被标记为car，不区分是哪一辆）

**Q: 掩码的坐标系统是什么？**

A: 掩码坐标与输入图像的像素坐标系统一致，左上角为原点(0,0)。

**Q: 如何使用掩码进行抠图？**

A: 可以将掩码作为alpha通道，或在下游节点中使用掩码区域提取对应的图像像素。

**Q: 分割边缘不够精确怎么办？**

A: 
   - 提高输入图像分辨率
   - 使用更大的模型
   - 在训练时增加边缘质量的标注
   - 后处理时使用GrabCut等算法优化边缘

**Q: 如何计算物体的实际尺寸？**

A: 使用 ``area`` 字段获得像素面积，然后根据相机标定参数转换为实际尺寸。

应用案例
--------

**案例1：背景替换**

使用实例分割提取人物轮廓，实现背景替换。

.. code-block:: json

   {
     "step_name": "person_segmentation",
     "model_type": "instance_segmentation",
     "confidence": 0.8,
     "label_confidence_thresholds": {
       "person": 0.85
     }
   }

工作流：
1. 使用实例分割模型提取人物掩码
2. 使用掩码将人物从原图中抠出
3. 将人物合成到新背景上

**案例2：物体计数（重叠场景）**

在物体重叠的场景中准确计数，如仓库中的堆叠货物。

.. code-block:: json

   {
     "step_name": "overlapping_object_count",
     "model_type": "instance_segmentation",
     "confidence": 0.7,
     "label_confidence_thresholds": {
       "box": 0.75
     }
   }

通过 ``instance_id`` 区分每个独立的物体，即使它们相互遮挡。

**案例3：精确面积测量**

测量物体的像素面积，用于质量控制或尺寸检测。

.. code-block:: json

   {
     "step_name": "area_measurement",
     "model_type": "instance_segmentation",
     "confidence": 0.85,
     "label_confidence_thresholds": {
       "component": 0.9
     }
   }

下游节点可以读取 ``area`` 字段，结合相机标定参数计算实际面积。

**案例4：医学影像分析**

对医学扫描图像进行器官或病灶的精确分割。

.. code-block:: json

   {
     "step_name": "organ_segmentation",
     "model_type": "instance_segmentation",
     "confidence": 0.9,
     "label_confidence_thresholds": {
       "liver": 0.95,
       "kidney": 0.95,
       "tumor": 0.98
     }
   }

.. warning::
   医疗应用需要极高的准确性，建议结合专业医生审核。

性能对比
--------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - 特性
     - 目标检测
     - 实例分割
   * - 输出精度
     - 矩形边界框
     - 像素级掩码
   * - 计算复杂度
     - 较低
     - 较高
   * - 推理速度
     - 快
     - 中等
   * - 适用场景
     - 物体定位、计数
     - 精确轮廓、抠图、测量

相关链接
--------

- :ref:`DaoAI World模型主页 <DaoAI World模型>`
- :ref:`目标检测模型 <daoai_world_object_detection>` - 如不需要精确轮廓
- :ref:`语义分割模型 <daoai_world_semantic_segmentation>` - 如不需要区分实例


