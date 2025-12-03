高级（17 项）
================

高级功能和工具模块。

.. toctree::
   :maxdepth: 1
   :hidden:

   cache_get
   cache_set
   cosine_similarity
   detections_classes_replacement
   detections_stitch
   dimension_collapse
   dynamic_zone
   environment_secrets_store
   expression
   first_non_empty_or_default
   image_slicer
   json_parser
   perspective_correction
   property_definition
   stitch_ocr_detections
   vlm_as_classifier
   vlm_as_detector

.. list-table::
   :header-rows: 0
   :widths: 33 34 33
   :class: block-cards

   * - :ref:`缓存获取`

       从缓存条目中获取之前存储的值
     - :ref:`缓存设置`

       将值存储在缓存条目中以便后续检索
     - :ref:`余弦相似度`

       计算两个嵌入向量之间的余弦相似度
   * - :ref:`检测类别替换`

       用单独分类模型预测的类别替换检测到的类别
     - :ref:`检测拼接`

       将对于多类输入图像的检测结果合并为某一检测结果
     - :ref:`维度折叠`

       将嵌套数据聚合为每个别列或位置组
   * - :ref:`动态区域`

       简化多边形，使其几何上方凸，并且仅包含所有需数据的顶点
     - :ref:`环境密钥存储`

       从环境变量中获取密钥
     - :ref:`表达式`

       根据定义的输入变量和配置的规则创建特定输出
   * - :ref:`首先非空或默认值`

       取第一个非空数据元素或默认值
     - :ref:`图像切片`

       将输入图像分割为一系列较小的图像以进行小物体检测
     - :ref:`JSON解析器`

       将原始字符串解析为 JSON
   * - :ref:`透视校正`

       将检测变换从多边形定义的平面图察到指定宽度和高度的直角平面
     - :ref:`属性定义`

       从模型预测中定义变量，例如类别名称、置信度或检测数量
     - :ref:`拼接OCR检测`

       通过按空间对位置组织检测结果，将OCR检测结果组合成连串的文本字符串
   * - :ref:`VLM分类器`

       将原始字符串解析为分类预测
     - :ref:`检测器VLM`

       将原始字符串解析为对象检测预测结果
     -

