.. _模型对比显示:

模型对比显示
==================

简介
----

Visualize the difference between two models' detections.

输入 / 输出
-----------

- 输入：图像 + 两组检测结果
- 输出：对比可视化图像

参数
----

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - 参数
     - 说明
     - 默认值
   * - layout
     - 布局方式（并排/叠加）
     - side-by-side
   * - show_diff
     - 是否显示差异
     - true

使用步骤
--------

1. 在工作流编辑器中添加本模块。
2. 选择布局方式。
3. 点击保存。

注意事项
--------

- 用于比较两个模型的检测结果差异。

