变换（12 项）
================

对图像和检测结果进行各种变换操作。

.. toctree::
   :maxdepth: 1
   :hidden:

   absolute_static_crop
   bounding_rectangle
   camera_calibration
   detection_offset
   detections_combine
   detections_merge
   detections_transformation
   dynamic_crop
   overlap_filter
   qr_code_generator
   relative_static_crop
   stitch_images

.. list-table::
   :header-rows: 0
   :widths: 33 34 33
   :class: block-cards

   * - :ref:`绝对静态裁剪`

       按固定座标裁剪图像
     - :ref:`边界框`

       找到检测的多边形周围的最小包围框
     - :ref:`相机标定`

       使用校准从图像中去除桶形机头变
   * - :ref:`检测偏移`

       在检测到的对象宽度和高度周围添加填充
     - :ref:`检测合并`

       将两个预测集合并为一个预测
     - :ref:`检测合并`

       将多个检测结果合并为一个边界框
   * - :ref:`检测变换`

       对检测到的边界框应用变换
     - :ref:`动态裁剪`

       使用检测模型的边界框裁剪图像
     - :ref:`重叠过滤`

       过滤与其他类叠加的对象
   * - :ref:`二维码生成器`

       从文本输入生成二维码图像
     - :ref:`相对静态裁剪`

       按比例（%）裁剪图像尺寸
     - :ref:`拼图图像`

       通过共同路径拼接两个图像

