.. _通用分类模型:

通用分类模型
============

简介
----

Zero-shot 图像分类，支持为每个标签提供多个提示/描述词，无需训练即可输出类别及置信度。

输入/输出
--------

- 输入（Input）:
  - 图像（来自上游节点或工作流输入）

- 输出（Output）:
  - 预测的类别标签及置信度
  - Top-K 排序结果（按置信度降序）

配置参数详解
------------

.. list-table::
   :header-rows: 1
   :widths: 22 48 30

   * - 参数
     - 说明
     - 示例/ ``默认值``
   * - 节点名称
     - 工作流中该节点的名称。
     - ``general_classification_1``
   * - 备注
     - 可选备注信息，记录用途。
     - ``留空``
   * - 图像
     - 指定输入图像来源。
     - ``input.image``
   * - 分类标签
     - 使用 JSON 配置，每个标签可给出多个提示/描述词。描述越具体（外观、材质、用途等）分类越准确。
     - 见下方示例
   * - 模型大小
     - base=最快，medium=平衡，large=最准确。
     - ``base``
   * - 推理精度
     - FP32（32位浮点）更准确；FP16（16位浮点）更快但精度略低。
     - ``fp32``
   * - 置信度阈值
     - 过滤低于阈值的预测。
     - ``0.3``
   * - Top-K
     - 返回置信度最高的前 K 个结果。
     - ``5``

分类标签示例
------------

.. code-block:: json

   {
     "car": [
       "A modern, road-legal passenger car with a wide and well-proportioned body, recognizable brand logo, complex headlights, full-size wheels, and high-quality automotive design."
     ],
     "e-bike": [
       "A lightweight electric scooter with a small frame, simple plastic body panels, thin wheels, and a pedal-free design, typically used as an e-bike in China."
     ],
     "bus": [
       "A large city bus with multiple rows of seats, wide windows, and a destination display on the front."
     ]
   }

