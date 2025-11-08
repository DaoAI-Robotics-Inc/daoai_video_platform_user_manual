.. _daoai_world_semantic_segmentation:

语义分割模型 (Semantic Segmentation)
=====================================

.. note::
   本页面介绍DaoAI World模型的语义分割类型。返回 :ref:`DaoAI World模型主页 <DaoAI World模型>`

模型简介
--------

语义分割模型对图像中的每个像素进行分类，将图像分割成不同的语义区域。与实例分割不同，语义分割不区分同类物体的不同实例，所有同类像素都被归为同一类别。

**输出内容：**

- **分割图** (每个像素的类别标签)
- **类别统计** (每个类别的像素数量和占比)
- **彩色可视化图** (可选)

适用场景
--------

语义分割模型适用于以下需要整体场景理解的场景：

- **自动驾驶**：道路分割、车道线识别、可行驶区域检测
- **医学影像**：组织分割、病灶区域标记
- **卫星遥感**：土地类型分类、植被覆盖分析
- **场景理解**：室内场景布局分析、空间规划
- **视频会议**：背景虚化、虚拟背景
- **农业应用**：作物与杂草分割、耕地识别
- **工业检测**：表面缺陷区域分割

输出格式
--------

语义分割模型的输出包含分割掩码和统计信息：

.. code-block:: json

   {
     "segmentation": {
       "type": "mask",
       "width": 1920,
       "height": 1080,
       "data": "base64_encoded_mask_data",
       "encoding": "png"
     },
     "classes": [
       {
         "class": "road",
         "label_id": 0,
         "pixel_count": 520800,
         "percentage": 25.1,
         "color": [128, 64, 128]
       },
       {
         "class": "building",
         "label_id": 1,
         "pixel_count": 416000,
         "percentage": 20.0,
         "color": [70, 70, 70]
       },
       {
         "class": "vegetation",
         "label_id": 2,
         "pixel_count": 728000,
         "percentage": 35.0,
         "color": [107, 142, 35]
       },
       {
         "class": "sky",
         "label_id": 3,
         "pixel_count": 410400,
         "percentage": 19.9,
         "color": [70, 130, 180]
       }
     ],
     "num_classes": 4
   }

**字段说明：**

- ``segmentation``: 分割掩码数据
  
  - ``type``: 掩码类型（通常为mask）
  - ``width``, ``height``: 分割图尺寸
  - ``data``: Base64编码的分割图数据
  - ``encoding``: 编码格式（png、jpg等）

- ``classes``: 检测到的类别列表
  
  - ``class``: 类别名称
  - ``label_id``: 类别ID（对应分割图中的像素值）
  - ``pixel_count``: 该类别的像素总数
  - ``percentage``: 占图像的百分比
  - ``color``: 可视化时使用的颜色(RGB)

- ``num_classes``: 检测到的类别总数

配置示例
--------

**道路场景分割**

.. code-block:: json

   {
     "step_name": "road_segmentation",
     "image": "input.image",
     "model_type": "semantic_segmentation",
     "confidence": 0.5
   }

**高精度医学影像分割**

.. code-block:: json

   {
     "step_name": "medical_tissue_seg",
     "image": "medical.scan",
     "model_type": "semantic_segmentation",
     "confidence": 0.8,
     "label_confidence_thresholds": {
       "tumor": 0.9,
       "healthy_tissue": 0.7
     }
   }

**遥感图像分析**

.. code-block:: json

   {
     "step_name": "land_classification",
     "image": "satellite.image",
     "model_type": "semantic_segmentation",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "water": 0.7,
       "forest": 0.6,
       "urban": 0.65,
       "agriculture": 0.6
     }
   }

使用技巧与最佳实践
------------------

1. **分割粒度选择**
   
   - **粗粒度**：大类别（如建筑、道路、天空）
   - **细粒度**：详细分类（如人行道、车道、路肩）
   - 根据应用需求平衡分类精细度和模型复杂度

2. **置信度阈值设置**
   
   - 一般场景：0.5-0.6
   - 高精度需求：0.7-0.9
   - 注意：语义分割的置信度通常针对整体输出，而不是单个像素

3. **处理边界模糊**
   
   - 分类边界处的像素可能存在不确定性
   - 可使用形态学操作（开运算、闭运算）优化边界
   - 使用条件随机场(CRF)进行后处理优化

4. **类别不平衡处理**
   
   - 小面积类别可能被忽略
   - 为重要的小面积类别降低置信度阈值
   - 使用加权损失函数训练模型

5. **性能优化**
   
   - 语义分割计算密集，强烈建议使用GPU
   - 可以降低输出分辨率以提升速度
   - 使用轻量级模型架构（如MobileNet）提升实时性

6. **多尺度处理**
   
   - 对于复杂场景，使用多尺度输入可提高精度
   - 融合不同尺度的预测结果

常见问题
--------

**Q: 语义分割和实例分割的主要区别是什么？**

A: 
   - **语义分割**：只关注"是什么"，不区分个体。例如，多辆车都标记为"car"类别
   - **实例分割**：区分"是哪个"，每辆车有独立的ID和掩码

   **选择建议：**
   
   - 需要区分个体（如计数、跟踪）→ 使用实例分割
   - 只需要区域分类（如可行驶区域、背景分割）→ 使用语义分割

**Q: 分割图的像素值代表什么？**

A: 分割图中每个像素的值对应该像素的类别ID（label_id）。例如，值为0的像素属于label_id为0的类别。

**Q: 如何提取特定类别的区域？**

A: 
1. 读取分割图
2. 找到对应类别的label_id
3. 创建二值掩码：mask = (segmentation == label_id)
4. 使用该掩码提取原图对应区域

**Q: 为什么分割边缘不够平滑？**

A: 可能的原因和解决方案：
   
   - 模型输出分辨率低：使用更高分辨率的模型
   - 图像质量差：提高输入图像质量
   - 后处理：使用双边滤波、CRF等优化边缘

**Q: 如何计算某个类别的面积占比？**

A: 直接使用输出中的 ``percentage`` 字段，或用 ``pixel_count / (width * height)`` 计算。

应用案例
--------

**案例1：自动驾驶场景理解**

识别道路、车道线、人行道、车辆、行人等，为决策提供依据。

.. code-block:: json

   {
     "step_name": "driving_scene_seg",
     "model_type": "semantic_segmentation",
     "confidence": 0.7,
     "label_confidence_thresholds": {
       "road": 0.8,
       "lane_marking": 0.75,
       "sidewalk": 0.7,
       "vehicle": 0.75,
       "pedestrian": 0.8,
       "building": 0.6,
       "vegetation": 0.6,
       "sky": 0.5
     }
   }

**应用逻辑：**

1. 识别可行驶区域（road + lane_marking）
2. 检测障碍物（vehicle, pedestrian）
3. 辅助路径规划

**案例2：视频会议背景虚化**

分割人物和背景，实现背景虚化或替换。

.. code-block:: json

   {
     "step_name": "background_seg",
     "model_type": "semantic_segmentation",
     "confidence": 0.8,
     "label_confidence_thresholds": {
       "person": 0.85,
       "background": 0.5
     }
   }

**处理流程：**

1. 使用语义分割提取人物区域
2. 对背景区域应用模糊效果
3. 或将背景替换为虚拟背景

**案例3：农田作物监测**

分析卫星或无人机图像，识别不同的土地类型和作物。

.. code-block:: json

   {
     "step_name": "crop_monitoring",
     "model_type": "semantic_segmentation",
     "confidence": 0.65,
     "label_confidence_thresholds": {
       "wheat": 0.7,
       "corn": 0.7,
       "fallow": 0.6,
       "water": 0.75,
       "forest": 0.65
     }
   }

**分析内容：**

- 计算各类作物的种植面积
- 监测作物生长状态
- 检测水源分布

**案例4：工业表面检测**

分割产品表面的缺陷区域，用于质量控制。

.. code-block:: json

   {
     "step_name": "surface_defect_seg",
     "model_type": "semantic_segmentation",
     "confidence": 0.85,
     "label_confidence_thresholds": {
       "scratch": 0.9,
       "dent": 0.9,
       "stain": 0.88,
       "normal": 0.7
     }
   }

**质检流程：**

1. 分割出所有缺陷区域
2. 计算缺陷面积占比
3. 根据阈值判定产品是否合格

性能对比
--------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - 特性
     - 语义分割
     - 实例分割
   * - 输出粒度
     - 类别级别
     - 实例级别
   * - 区分个体
     - 否
     - 是
   * - 计算复杂度
     - 中等
     - 较高
   * - 适用场景
     - 场景理解、区域分类
     - 物体计数、个体追踪

常用类别集
----------

**城市街道场景 (Cityscapes)**

- road, sidewalk, building, wall, fence
- pole, traffic_light, traffic_sign
- vegetation, terrain, sky
- person, rider, car, truck, bus, train
- motorcycle, bicycle

**室内场景 (ADE20K)**

- wall, floor, ceiling, window, door
- table, chair, sofa, bed
- cabinet, shelf, lamp
- person, tv, computer

**医学影像**

- background, organ, tumor, vessel
- bone, soft_tissue

相关链接
--------

- :ref:`DaoAI World模型主页 <DaoAI World模型>`
- :ref:`实例分割模型 <daoai_world_instance_segmentation>` - 如需区分个体实例
- :ref:`分类模型 <daoai_world_classification>` - 如只需整体类别判断


