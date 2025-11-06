.. _DaoAI World模型:

DaoAI World模型
==================

简介
----

使用DaoAI World训练的模型对图像进行预测。

输入 / 输出
-----------

- 输入：视频帧 / 图像
- 输出：检测结果 / 分类结果

参数
----

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - 参数
     - 说明
     - 默认值
   * - model_id
     - DaoAI World 模型 ID
     - 无
   * - confidence
     - 置信度阈值（0~1）
     - 0.5

使用步骤
--------

1. 在工作流编辑器中添加本模块。
2. 选择已训练的 DaoAI World 模型。
3. 调整置信度阈值，点击保存。

注意事项
--------

- 需要确保模型已在 DaoAI World 平台完成训练。

