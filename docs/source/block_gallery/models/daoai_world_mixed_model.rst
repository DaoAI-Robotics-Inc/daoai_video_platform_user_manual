.. _daoai_world_mixed_model:

混合模型 (Mixed Model)
=======================

.. note::
   本页面介绍DaoAI World模型的混合模型类型。返回 :ref:`DaoAI World模型主页 <DaoAI World模型>`

模型简介
--------

混合模型结合了多种计算机视觉任务，可以在一次推理中同时执行多个任务，如同时进行目标检测、分类和关键点检测等。这种模型适用于需要多维度信息的复杂应用场景，既能提高效率，又能保证不同任务之间的信息一致性。

**支持的任务组合：**

- 检测 + 分类
- 检测 + 关键点
- 检测 + 分割
- 分类 + 分割
- 检测 + 分类 + 关键点
- 其他自定义组合

适用场景
--------

混合模型适用于需要综合多种信息的复杂场景：

- **智能零售**：商品检测 + 品牌分类 + 价格标签OCR
- **智能安防**：人员检测 + 身份识别 + 姿态分析
- **自动驾驶**：车辆检测 + 车型分类 + 关键部位定位
- **工业质检**：缺陷检测 + 缺陷分类 + 缺陷区域分割
- **体育分析**：运动员检测 + 动作分类 + 姿态关键点
- **医疗诊断**：病灶检测 + 类型分类 + 区域分割
- **智能农业**：作物检测 + 成熟度分类 + 病虫害分割

输出格式
--------

混合模型的输出包含多个任务的结果，具体格式取决于组合的任务类型：

**示例1：检测 + 分类 + 关键点**

.. code-block:: json

   {
     "instances": [
       {
         "detection": {
           "class": "person",
           "confidence": 0.95,
           "bbox": {
             "x": 100,
             "y": 50,
             "width": 200,
             "height": 400
           }
         },
         "classification": {
           "attributes": [
             {"name": "gender", "value": "male", "confidence": 0.88},
             {"name": "age_group", "value": "adult", "confidence": 0.92},
             {"name": "clothing", "value": "formal", "confidence": 0.85}
           ]
         },
         "keypoints": [
           {"name": "head", "x": 200, "y": 100, "confidence": 0.96},
           {"name": "left_shoulder", "x": 170, "y": 180, "confidence": 0.93},
           {"name": "right_shoulder", "x": 230, "y": 180, "confidence": 0.94}
         ],
         "instance_id": 1
       }
     ],
     "count": 1
   }

**示例2：检测 + 分割**

.. code-block:: json

   {
     "instances": [
       {
         "detection": {
           "class": "car",
           "confidence": 0.92,
           "bbox": {"x": 300, "y": 200, "width": 250, "height": 180}
         },
         "segmentation": {
           "mask": {
             "type": "polygon",
             "points": [[310, 210], [540, 210], [550, 380], [300, 380]]
           },
           "area": 42500
         },
         "instance_id": 1
       }
     ],
     "count": 1
   }

**示例3：检测 + 分类（质检场景）**

.. code-block:: json

   {
     "results": [
       {
         "detection": {
           "class": "product",
           "confidence": 0.96,
           "bbox": {"x": 150, "y": 100, "width": 300, "height": 250}
         },
         "quality_classification": {
           "result": "defect",
           "confidence": 0.89,
           "defect_types": [
             {"type": "scratch", "confidence": 0.92},
             {"type": "dent", "confidence": 0.78}
           ]
         },
         "instance_id": 1
       }
     ],
     "overall_quality": "fail"
   }

配置示例
--------

**智能安防：人员检测+属性分析**

.. code-block:: json

   {
     "step_name": "person_analysis",
     "image": "camera.frame",
     "model_type": "mixed",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "person": 0.7
     }
   }

**工业质检：缺陷检测+分类**

.. code-block:: json

   {
     "step_name": "defect_inspection",
     "image": "product.image",
     "model_type": "mixed",
     "confidence": 0.8,
     "label_confidence_thresholds": {
       "defect": 0.85,
       "scratch": 0.9,
       "crack": 0.9,
       "dent": 0.85
     }
   }

**零售分析：商品识别+属性**

.. code-block:: json

   {
     "step_name": "product_recognition",
     "image": "shelf.camera",
     "model_type": "mixed",
     "confidence": 0.7,
     "label_confidence_thresholds": {
       "product": 0.75,
       "brand": 0.7,
       "category": 0.7
     }
   }

**体育分析：运动员检测+动作识别**

.. code-block:: json

   {
     "step_name": "sports_analysis",
     "image": "match.frame",
     "model_type": "mixed",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "player": 0.7,
       "action": 0.65
     }
   }

使用技巧与最佳实践
------------------

1. **任务优先级设置**
   
   - 为不同任务设置不同的置信度阈值
   - 关键任务使用更高的阈值以确保准确性
   - 辅助任务可以使用较低的阈值

2. **性能优化**
   
   - 混合模型比分别运行多个模型更高效
   - 共享特征提取可减少计算量
   - 建议使用GPU加速

3. **任务相关性利用**
   
   - 检测结果可以指导分类和分割的区域
   - 分类结果可以优化检测的置信度
   - 关键点可以辅助姿态分类

4. **结果一致性**
   
   - 混合模型保证了不同任务看到的是同一特征
   - 避免了多次推理可能带来的不一致

5. **置信度策略**
   
   - 主任务（如检测）使用标准阈值
   - 子任务（如属性分类）可以使用较低阈值
   - 综合多个任务的置信度做最终决策

常见问题
--------

**Q: 混合模型比分别运行多个单一模型有什么优势？**

A: 
   - **性能优势**：共享特征提取，计算量大幅减少，速度更快
   - **一致性**：所有任务基于相同的特征，结果更一致
   - **准确性**：任务之间可以相互增强，提高整体准确度
   - **便捷性**：一次推理获得所有结果，简化工作流

**Q: 如何理解混合模型的置信度？**

A: 混合模型通常为每个任务输出独立的置信度：
   
   - ``detection.confidence``: 检测任务的置信度
   - ``classification.confidence``: 分类任务的置信度
   - 可以为不同任务设置不同的阈值

**Q: 混合模型的训练需要什么样的数据？**

A: 需要同时包含多个任务标注的数据集。例如检测+分类模型需要：
   
   - 物体边界框标注
   - 物体类别标注
   - 物体属性标注（如果需要）

**Q: 所有任务都必须成功才输出结果吗？**

A: 不是。每个任务独立输出结果。某个任务失败（置信度过低）不影响其他任务的输出。

**Q: 如何选择合适的任务组合？**

A: 基于应用需求选择：
   
   - **需要位置和类别** → 检测 + 分类
   - **需要精确轮廓** → 检测 + 分割
   - **需要姿态信息** → 检测 + 关键点
   - **需要综合分析** → 检测 + 分类 + 关键点/分割

应用案例
--------

**案例1：智能零售 - 商品识别系统**

检测货架上的商品，识别品牌和类别，统计库存。

.. code-block:: json

   {
     "step_name": "retail_product_analysis",
     "model_type": "mixed",
     "confidence": 0.7,
     "label_confidence_thresholds": {
       "product": 0.75,
       "brand": 0.7,
       "category": 0.7,
       "sku": 0.8
     }
   }

**输出示例：**

.. code-block:: json

   {
     "products": [
       {
         "detection": {"bbox": [...], "confidence": 0.88},
         "classification": {
           "brand": "Coca-Cola",
           "category": "beverage",
           "sku": "COKE-500ML",
           "confidence": 0.85
         }
       }
     ]
   }

**案例2：工业质检 - 多维度缺陷检测**

检测产品缺陷，分类缺陷类型，分割缺陷区域。

.. code-block:: json

   {
     "step_name": "comprehensive_qc",
     "model_type": "mixed",
     "confidence": 0.85,
     "label_confidence_thresholds": {
       "defect": 0.9,
       "scratch": 0.92,
       "crack": 0.95,
       "dent": 0.90
     }
   }

**决策逻辑：**

1. 检测：是否存在缺陷区域
2. 分类：缺陷属于哪种类型
3. 分割：精确的缺陷范围
4. 计算缺陷面积，判定产品等级

**案例3：智能健身 - 动作指导**

检测人员，识别动作类型，分析姿态是否标准。

.. code-block:: json

   {
     "step_name": "fitness_coach",
     "model_type": "mixed",
     "confidence": 0.7,
     "label_confidence_thresholds": {
       "person": 0.75,
       "action": 0.7
     }
   }

**分析流程：**

1. 检测人体位置
2. 识别动作类型（深蹲、俯卧撑等）
3. 检测关键点，计算关节角度
4. 判断动作是否标准，给出反馈

**案例4：自动驾驶 - 车辆综合分析**

检测车辆，分类车型，定位关键部位（车灯、车牌等）。

.. code-block:: json

   {
     "step_name": "vehicle_analysis",
     "model_type": "mixed",
     "confidence": 0.75,
     "label_confidence_thresholds": {
       "vehicle": 0.8,
       "vehicle_type": 0.75,
       "plate": 0.85
     }
   }

**应用价值：**

- 检测：定位车辆
- 分类：识别车型（轿车、卡车、公交等）
- 关键点：定位车牌、车灯位置，用于进一步分析

任务组合对比
------------

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - 任务组合
     - 应用场景
     - 性能特点
   * - 检测 + 分类
     - 物体识别、质检、零售
     - 速度快，信息丰富
   * - 检测 + 分割
     - 精确定位、抠图、测量
     - 精度高，计算量中等
   * - 检测 + 关键点
     - 姿态分析、动作识别
     - 信息详细，实时性好
   * - 检测 + 分类 + 分割
     - 综合质检、医疗诊断
     - 全面分析，计算量大

性能优势
--------

**单一模型 vs 混合模型**

假设需要同时进行检测、分类、关键点三个任务：

**分别运行三个模型：**

- 检测模型：100ms
- 分类模型：80ms  
- 关键点模型：120ms
- **总耗时：300ms**

**使用混合模型：**

- 混合模型：150ms
- **总耗时：150ms**
- **速度提升：50%**

相关链接
--------

- :ref:`DaoAI World模型主页 <DaoAI World模型>`
- :ref:`目标检测模型 <daoai_world_object_detection>`
- :ref:`分类模型 <daoai_world_classification>`
- :ref:`实例分割模型 <daoai_world_instance_segmentation>`
- :ref:`关键点检测模型 <daoai_world_keypoint_detection>`




