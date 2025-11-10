.. _DaoAI World模型:

DaoAI World模型
==================

简介
----

DaoAI World模型节点用于运行在DaoAI World平台训练的AI模型，支持多种类型的计算机视觉任务。通过该节点，您可以对图像或视频帧进行目标检测、分类、分割、关键点检测、OCR等推理操作。

输入 / 输出
-----------

- **输入**：图像（来自上游节点或工作流输入）
- **输出**：根据模型类型不同，输出检测框、分类结果、分割掩码、关键点坐标或文字识别结果等

配置参数详解
------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - 参数名称
     - 说明
     - 示例/默认值
   * - **Step Name**
     - 步骤名称，用于标识该节点的唯一标识符
     - ``daoai_world_model_1``
   * - **Comments**
     - 可选的备注信息，用于描述该步骤的用途
     - 留空
   * - **Image**
     - 指定输入图像的来源，可以是上游节点的输出或工作流的输入参数
     - ``input.image``
   * - **Model Type**
     - 选择模型类型，支持7种类型（详见下方模型类型章节）
     - ``detection``
   * - **Selected Model**
     - 选择已在DaoAI World平台训练完成的模型
     - 点击"Select Model"按钮选择
   * - **Confidence Threshold**
     - 全局置信度阈值，用于过滤低置信度的预测结果（0~1）
     - ``0.3``
   * - **Label Confidence Thresholds**
     - 为每个标签单独设置置信度阈值（JSON格式）
     - ``{"car": 0.5, "person": 0.7}``

支持的模型类型
--------------

DaoAI World模型节点支持以下7种模型类型，每种类型适用于不同的应用场景：

.. toctree::
   :maxdepth: 1
   :hidden:

   daoai_world_object_detection
   daoai_world_classification
   daoai_world_instance_segmentation
   daoai_world_keypoint_detection
   daoai_world_semantic_segmentation
   daoai_world_mixed_model
   daoai_world_ocr

.. list-table::
   :header-rows: 1
   :widths: 25 50 25

   * - 模型类型
     - 描述
     - 详细文档
   * - **Object Detection**
     - 目标检测，识别图像中的物体并输出边界框
     - :ref:`目标检测模型 <daoai_world_object_detection>`
   * - **Classification**
     - 图像分类，对整张图像进行分类
     - :ref:`分类模型 <daoai_world_classification>`
   * - **Instance Segmentation**
     - 实例分割，识别并分割图像中的每个物体实例
     - :ref:`实例分割模型 <daoai_world_instance_segmentation>`
   * - **Keypoint Detection**
     - 关键点检测，识别物体的关键点位置（如人体姿态）
     - :ref:`关键点检测模型 <daoai_world_keypoint_detection>`
   * - **Semantic Segmentation**
     - 语义分割，对图像中的每个像素进行分类
     - :ref:`语义分割模型 <daoai_world_semantic_segmentation>`
   * - **Mixed Model**
     - 混合模型，结合多种任务类型
     - :ref:`混合模型 <daoai_world_mixed_model>`
   * - **OCR**
     - 光学字符识别，识别图像中的文字
     - :ref:`OCR模型 <daoai_world_ocr>`

使用步骤
--------

1. **添加节点**
   
   在工作流编辑器中，从模块面板拖拽"DaoAI World Model"节点到画布。

2. **配置输入**
   
   在 **Image** 参数中，指定输入图像来源（如 ``input.image`` 或上游节点的输出）。

3. **选择模型类型**
   
   在 **Model Type** 下拉菜单中选择适合您任务的模型类型（如 ``detection``、``classification`` 等）。

4. **选择模型**
   
   点击 **Select Model** 按钮，在弹出的模型选择对话框中选择已训练好的模型。

5. **设置置信度阈值**
   
   - 调整 **Confidence Threshold** 设置全局阈值
   - （可选）在 **Label Confidence Thresholds** 中为特定标签设置独立阈值

6. **保存配置**
   
   配置完成后，点击保存按钮。

使用示例
--------

**示例1：目标检测**

.. code-block:: json

   {
     "step_name": "car_detection",
     "image": "input.image",
     "model_type": "detection",
     "confidence": 0.5
   }

**示例2：为不同标签设置不同阈值**

.. code-block:: json

   {
     "step_name": "multi_class_detection",
     "confidence": 0.3,
     "label_confidence_thresholds": {
       "car": 0.5,
       "person": 0.7,
       "bicycle": 0.4
     }
   }

注意事项
--------

- 模型必须在 DaoAI World 平台完成训练后才能使用
- 不同模型类型的输出格式不同，请根据下游节点的需求选择合适的模型类型
- ``Label Confidence Thresholds`` 中设置的标签阈值会覆盖全局的 ``Confidence Threshold``
- 置信度阈值设置过高可能导致漏检，设置过低可能导致误检，建议根据实际场景调整
- OCR模型的置信度阈值建议设置在0.5以上以获得更准确的识别结果

常见问题
--------

**Q: 如何查看可用的模型？**

A: 点击"Select Model"按钮会弹出模型选择对话框，显示所有已训练完成的模型列表。

**Q: Label Confidence Thresholds的格式是什么？**

A: 使用JSON格式，键为标签名称，值为0~1之间的浮点数。例如：``{"car": 0.5, "person": 0.7}``

**Q: 模型类型选错了怎么办？**

A: 更改模型类型后需要重新选择对应类型的模型，之前选择的模型会被清空。

相关链接
--------

- DaoAI World 平台文档
- 模型训练指南
- 工作流配置说明

