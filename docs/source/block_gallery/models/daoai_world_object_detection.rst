.. _daoai_world_object_detection:

目标检测模型 (Object Detection)
=================================

.. note::
   本页面介绍DaoAI World模型的目标检测类型。返回 :ref:`DaoAI World模型主页 <DaoAI World模型>`

模型简介
--------

目标检测模型用于识别图像中的物体，并为每个检测到的物体输出：

- **边界框坐标** (x, y, width, height)
- **类别标签** (如：car, person, dog等)
- **置信度分数** (0~1之间的浮点数)

适用场景
--------

目标检测模型适用于以下场景：

- **安防监控**：检测人员、车辆、异常物体
- **智能交通**：车辆计数、车型识别、违章检测
- **工业质检**：产品缺陷检测、零件识别
- **零售分析**：商品识别、货架检测、客流分析
- **农业应用**：作物病虫害检测、成熟度判断

输出格式
--------

目标检测模型的输出为JSON格式，包含检测到的所有物体信息：

.. code-block:: json

   {
     "detections": [
       {
         "class": "car",
         "confidence": 0.95,
         "bbox": {
           "x": 100,
           "y": 150,
           "width": 200,
           "height": 150
         }
       },
       {
         "class": "person",
         "confidence": 0.88,
         "bbox": {
           "x": 350,
           "y": 200,
           "width": 80,
           "height": 180
         }
       }
     ],
     "count": 2
   }

**字段说明：**

- ``class``: 检测到的物体类别
- ``confidence``: 检测置信度（0~1）
- ``bbox``: 边界框坐标
  
  - ``x``, ``y``: 边界框左上角坐标
  - ``width``, ``height``: 边界框宽度和高度

- ``count``: 检测到的物体总数

配置示例
--------

**基础配置**

.. code-block:: json

   {
     "step_name": "vehicle_detection",
     "image": "input.image",
     "model_type": "detection",
     "confidence": 0.5
   }

**多类别不同阈值**

针对不同类别设置不同的置信度阈值，适用于某些类别需要更高精度的场景：

.. code-block:: json

   {
     "step_name": "traffic_detection",
     "image": "camera.frame",
     "model_type": "detection",
     "confidence": 0.3,
     "label_confidence_thresholds": {
       "car": 0.5,
       "truck": 0.6,
       "person": 0.7,
       "bicycle": 0.4
     }
   }

使用技巧与最佳实践
------------------

1. **置信度阈值调整**
   
   - 初始建议值：0.5
   - 高精度场景（如工业质检）：0.7-0.9
   - 高召回场景（如安防监控）：0.3-0.5

2. **性能优化**
   
   - 对于高分辨率图像，建议启用GPU加速
   - 批量处理时可调整batch size以提高吞吐量
   - 实时应用建议使用较小的模型以降低延迟

3. **处理重叠物体**
   
   - 模型会自动进行NMS（非极大值抑制）去除重复检测
   - 如需调整NMS阈值，可在高级设置中配置

4. **提高检测精度**
   
   - 确保训练数据包含足够的样本多样性
   - 使用数据增强提高模型泛化能力
   - 针对特定场景调整置信度阈值

常见问题
--------

**Q: 检测结果中出现很多误检怎么办？**

A: 可以提高 ``confidence`` 阈值来过滤低置信度的检测结果。建议从0.5开始逐步调整。

**Q: 小物体检测效果不好？**

A: 小物体检测是目标检测的难点。建议：
   
   - 使用更高分辨率的输入图像
   - 在训练时增加小物体样本
   - 降低该类别的置信度阈值

**Q: 边界框坐标是相对坐标还是绝对坐标？**

A: 边界框坐标为绝对像素坐标，与输入图像的分辨率对应。

**Q: 如何统计特定类别的数量？**

A: 可以在下游节点中对 ``detections`` 数组进行过滤和计数，或使用专门的统计节点。

应用案例
--------

**案例1：车辆计数系统**

使用目标检测模型识别道路上的车辆，结合跟踪算法实现车流量统计。

.. code-block:: json

   {
     "step_name": "vehicle_counter",
     "model_type": "detection",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "car": 0.6,
       "truck": 0.65,
       "bus": 0.7
     }
   }

**案例2：人员安全监控**

检测工作区域内的人员和安全装备，确保作业安全。

.. code-block:: json

   {
     "step_name": "safety_monitor",
     "model_type": "detection",
     "confidence": 0.5,
     "label_confidence_thresholds": {
       "person": 0.7,
       "helmet": 0.6,
       "safety_vest": 0.6
     }
   }

相关链接
--------

- :ref:`DaoAI World模型主页 <DaoAI World模型>`
- :ref:`实例分割模型 <daoai_world_instance_segmentation>` - 如需更精确的物体轮廓
- :ref:`分类模型 <daoai_world_classification>` - 如只需判断图像类别

