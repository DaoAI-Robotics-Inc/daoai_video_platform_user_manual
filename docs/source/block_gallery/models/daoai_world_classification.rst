.. _daoai_world_classification:

分类模型 (Classification)
==========================

.. note::
   本页面介绍DaoAI World模型的图像分类类型。返回 :ref:`DaoAI World模型主页 <DaoAI World模型>`

模型简介
--------

分类模型用于对整张图像进行类别判断，为图像分配一个或多个类别标签及其对应的置信度分数。与目标检测不同，分类模型不输出物体的位置信息，而是对整体图像内容进行识别。

适用场景
--------

图像分类模型适用于以下场景：

- **质量检测**：良品/不良品分类、缺陷类型识别
- **医疗影像**：病症分类、X光片诊断辅助
- **内容审核**：图片内容分类、不当内容识别
- **场景识别**：室内/室外、白天/夜晚等场景分类
- **产品识别**：产品型号识别、品牌识别
- **动植物识别**：物种分类、品种鉴定

输出格式
--------

分类模型的输出为JSON格式，包含预测的类别及置信度：

**单标签分类输出：**

.. code-block:: json

   {
     "predictions": [
       {
         "class": "cat",
         "confidence": 0.95
       },
       {
         "class": "dog",
         "confidence": 0.03
       },
       {
         "class": "bird",
         "confidence": 0.02
       }
     ],
     "top_class": "cat",
     "top_confidence": 0.95
   }

**多标签分类输出：**

.. code-block:: json

   {
     "predictions": [
       {
         "class": "outdoor",
         "confidence": 0.92
       },
       {
         "class": "sunny",
         "confidence": 0.88
       },
       {
         "class": "mountain",
         "confidence": 0.75
       }
     ],
     "active_labels": ["outdoor", "sunny", "mountain"]
   }

**字段说明：**

- ``predictions``: 所有类别的预测结果（按置信度降序排列）
- ``class``: 类别名称
- ``confidence``: 该类别的置信度（0~1）
- ``top_class``: 置信度最高的类别（单标签分类）
- ``top_confidence``: 最高置信度值（单标签分类）
- ``active_labels``: 超过阈值的所有标签（多标签分类）

配置示例
--------

**基础单标签分类**

.. code-block:: json

   {
     "step_name": "product_classifier",
     "image": "input.image",
     "model_type": "classification",
     "confidence": 0.5
   }

**多标签分类配置**

.. code-block:: json

   {
     "step_name": "scene_attributes",
     "image": "camera.frame",
     "model_type": "classification",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "outdoor": 0.7,
       "indoor": 0.7,
       "sunny": 0.5,
       "rainy": 0.5,
       "night": 0.6
     }
   }

**质量检测应用**

.. code-block:: json

   {
     "step_name": "quality_check",
     "image": "inspection.image",
     "model_type": "classification",
     "confidence": 0.8,
     "label_confidence_thresholds": {
       "defect": 0.9,
       "good": 0.7
     }
   }

使用技巧与最佳实践
------------------

1. **置信度阈值设置**
   
   - **单标签分类**：建议0.5-0.7，可直接使用top_class
   - **多标签分类**：建议0.6-0.8，避免过多误判标签
   - **质量检测**：建议0.8-0.95，确保高精度

2. **处理不确定结果**
   
   - 当top_confidence < 0.5时，建议标记为"不确定"或进行人工复核
   - 可设置多个置信度区间，执行不同的后续操作

3. **类别不平衡处理**
   
   - 对少数类别降低阈值以提高召回率
   - 对关键类别提高阈值以确保精确度

4. **性能优化**
   
   - 分类模型通常比检测模型更快，适合实时应用
   - 批量处理可显著提升吞吐量

5. **图像预处理**
   
   - 确保输入图像质量良好（清晰度、光照）
   - 保持与训练数据相似的图像风格和分辨率

常见问题
--------

**Q: 分类结果的所有类别置信度加起来等于1吗？**

A: 对于单标签分类（使用softmax），所有类别置信度之和为1。对于多标签分类（使用sigmoid），每个类别独立计算，总和不一定为1。

**Q: 如何判断模型对结果的确定程度？**

A: 查看 ``top_confidence`` 值：
   
   - > 0.9：高度确定
   - 0.7-0.9：较为确定
   - 0.5-0.7：中等确定
   - < 0.5：不确定，建议复核

**Q: 图像中有多个物体时，分类结果是什么？**

A: 分类模型对整张图像进行分类，通常会输出最显著物体的类别或整体场景的类别。如需识别多个物体，建议使用目标检测模型。

**Q: 可以同时输出多个类别吗？**

A: 可以。这取决于模型训练方式：
   
   - **单标签分类**：只选择置信度最高的一个类别
   - **多标签分类**：可输出多个超过阈值的类别

应用案例
--------

**案例1：工业质检**

对生产线产品进行良品/不良品分类，并识别缺陷类型。

.. code-block:: json

   {
     "step_name": "defect_classifier",
     "model_type": "classification",
     "confidence": 0.85,
     "label_confidence_thresholds": {
       "good": 0.8,
       "scratch": 0.9,
       "crack": 0.9,
       "dent": 0.9
     }
   }

工作流逻辑：

- 如果输出为 "good" 且 confidence > 0.8，则通过检测
- 如果输出为缺陷类型且 confidence > 0.9，则标记为不良品
- 如果所有 confidence < 0.8，则转人工复核

**案例2：场景识别**

识别图像中的多个场景属性（多标签分类）。

.. code-block:: json

   {
     "step_name": "scene_analyzer",
     "model_type": "classification",
     "confidence": 0.6,
     "label_confidence_thresholds": {
       "outdoor": 0.7,
       "urban": 0.6,
       "daytime": 0.5,
       "crowded": 0.65
     }
   }

输出示例：``["outdoor", "urban", "daytime", "crowded"]``

**案例3：医疗影像辅助诊断**

对医学影像进行病症分类，辅助医生诊断。

.. code-block:: json

   {
     "step_name": "xray_diagnosis",
     "model_type": "classification",
     "confidence": 0.9,
     "label_confidence_thresholds": {
       "normal": 0.85,
       "pneumonia": 0.95,
       "fracture": 0.95
     }
   }

.. warning::
   医疗应用需要设置极高的置信度阈值，且结果仅供参考，不能替代专业医生诊断。

相关链接
--------

- :ref:`DaoAI World模型主页 <DaoAI World模型>`
- :ref:`目标检测模型 <daoai_world_object_detection>` - 如需定位物体位置
- :ref:`混合模型 <daoai_world_mixed_model>` - 结合分类和检测












