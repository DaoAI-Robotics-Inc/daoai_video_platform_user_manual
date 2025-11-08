.. _边界框显示:

边界框显示
==================

简介
----

边界框显示节点用于在图像中检测到的对象周围绘制矩形框，是最常用的可视化方式之一。该节点支持多种颜色方案、自定义样式和灵活的配置选项，可以清晰地展示目标检测、实例分割等模型的预测结果。

适用场景
--------

- **目标检测可视化**：显示检测到的物体位置和类别
- **监控系统**：实时标注监控画面中的目标
- **质量检测**：标注产品缺陷位置
- **数据标注验证**：验证模型预测结果的准确性
- **演示和报告**：生成可视化结果用于展示
- **调试分析**：辅助开发者理解模型输出

输入 / 输出
-----------

- **输入**：
  
  - 图像（来自上游节点或工作流输入）
  - 检测结果（包含边界框坐标、类别、置信度等信息）

- **输出**：
  
  - 绘制了边界框的可视化图像

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
     - ``bounding_box_visualization_1``
   * - **Comments**
     - 可选的备注信息，用于描述该步骤的用途
     - 留空
   * - **Input Image**
     - 指定输入图像的来源，可以是上游节点的输出或工作流的输入参数
     - ``input.image``
   * - **Copy Image**
     - 是否创建输入图像的副本进行可视化，启用后不会修改原始图像
     - ``True(推荐)``
   * - **Predictions Display**
     - 要可视化的模型预测结果，选择检测模型的输出
     - 从下拉菜单选择
   * - **Color Palette**
     - 颜色调色板方案，用于为不同类别分配颜色
     - ``DEFAULT``
   * - **Palette Size**
     - 调色板中的颜色数量，适用于使用自定义或Matplotlib调色板时
     - ``10``
   * - **Custom Colors**
     - 自定义颜色列表，使用HEX格式定义边界框颜色
     - ``["#FF0000", "#00FF00", "#0000FF"]``
   * - **Color Axis**
     - 颜色分配的依据，通常基于类别（CLASS）来着色
     - ``CLASS``
   * - **Bounding Box Thickness**
     - 边界框线条的粗细（像素）
     - ``2``
   * - **Corner Roundness**
     - 边界框角的圆角半径，0表示直角
     - ``0``

参数详细说明
------------

**Copy Image（复制图像）**

- **True**：创建图像副本，原始图像保持不变，可用于后续其他可视化
- **False**：直接在原图上绘制，节省内存但会修改原图

**Color Palette（颜色调色板）**

支持多种调色板方案：

- ``DEFAULT``：系统默认配色方案
- ``MATPLOTLIB``：使用Matplotlib的颜色方案
- ``CUSTOM``：使用自定义颜色列表（需配置Custom Colors参数）

**Custom Colors（自定义颜色）**

当选择自定义颜色时，使用HEX格式定义颜色列表：

.. code-block:: json

   ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF"]

颜色会按顺序分配给不同的类别。

**Color Axis（颜色轴）**

- ``CLASS``：根据物体类别着色，同类物体使用相同颜色
- ``INDEX``：为每个物体分配不同颜色
- ``TRACK``：待定

**Bounding Box Thickness（边界框粗细）**

- 建议值：1-5像素
- 小图像：1-2像素
- 大图像：3-5像素
- 演示用途：4-6像素

**Corner Roundness（圆角半径）**

- ``0``：标准直角矩形
- ``0.5``：轻微圆角，更柔和
- ``1.0``：明显圆角，更美观

使用步骤
--------

1. **添加节点**
   
   在工作流编辑器中，从可视化模块面板拖拽"边界框显示"节点到画布。

2. **连接输入**
   
   - 在 **Input Image** 中指定输入图像来源
   - 在 **Predictions Display** 中选择检测模型的输出

3. **配置颜色方案**
   
   - 选择 **Color Palette**（推荐使用DEFAULT或自定义）
   - 如果使用自定义颜色，在 **Custom Colors** 中定义颜色列表
   - 设置 **Color Axis** 为 CLASS（按类别着色）

4. **调整样式**
   
   - 设置 **Bounding Box Thickness**（建议2-4）
   - 设置 **Corner Roundness**（0为直角，1为圆角）

5. **保存配置**
   
   确认 **Copy Image** 为True（推荐），点击保存按钮。

常见问题
--------

**Q: 边界框没有显示出来？**

A: 检查以下几点：
   
   - 确认 **Predictions Display** 已正确选择模型输出
   - 检查检测模型是否有输出结果（置信度是否过滤）
   - 确认输入图像正确传递
   - 查看边界框颜色是否与背景颜色接近

**Q: 如何为特定类别设置固定颜色？**

A: 使用自定义颜色列表：
   
   1. 设置 **Color Palette** 为 CUSTOM
   2. 在 **Custom Colors** 中按类别顺序定义颜色
   3. 颜色会按照模型定义的类别顺序分配

**Q: Copy Image设置为True和False有什么区别？**

A: 
   - **True**：创建图像副本，原图不变，适合后续还需要使用原图的场景
   - **False**：直接修改原图，节省内存，但原图会被改变

**Q: 边界框太细看不清怎么办？**

A: 增加 **Bounding Box Thickness** 值，建议根据图像分辨率调整：
   
   - 小图（<720p）：2-3像素
   - 中图（720p-1080p）：3-4像素
   - 大图（>1080p）：4-6像素

**Q: 可以只显示特定类别的边界框吗？**

A: 边界框显示节点会显示所有检测结果。如需过滤，应在检测模型或上游添加过滤节点。

**Q: 圆角边界框看起来不明显？**

A: 圆角效果在粗线条上更明显，尝试：
   
   - 增加 **Corner Roundness** 值（10-20）
   - 增加 **Bounding Box Thickness**（4-6）

应用案例
--------

**案例1：安防监控可视化**

实时标注监控画面中的人员和车辆。

.. code-block:: json

   {
     "step_name": "security_bbox_display",
     "input_image": "camera.feed",
     "predictions": "person_vehicle_detection.predictions",
     "copy_image": true,
     "color_palette": "CUSTOM",
     "custom_colors": [
       "#FF3B30",
       "#34C759"
     ],
     "color_axis": "CLASS",
     "thickness": 3,
     "corner_roundness": 0
   }

**效果**：红色标注人员，绿色标注车辆。

**案例2：工业质检可视化**

标注产品缺陷位置，使用圆角矩形提升视觉效果。

.. code-block:: json

   {
     "step_name": "qc_bbox_display",
     "input_image": "inspection.image",
     "predictions": "defect_detection.predictions",
     "copy_image": true,
     "color_palette": "CUSTOM",
     "custom_colors": [
       "#FF9500",
       "#FF3B30",
       "#AF52DE"
     ],
     "color_axis": "CLASS",
     "thickness": 4,
     "corner_roundness": 12
   }

**分类**：橙色=轻微缺陷，红色=严重缺陷，紫色=污渍。

**案例3：多模型对比**

在同一图像上显示两个模型的检测结果进行对比。

.. code-block:: json

   {
     "step_name": "model_a_bbox",
     "input_image": "input.image",
     "predictions": "model_a.predictions",
     "copy_image": true,
     "color_palette": "CUSTOM",
     "custom_colors": ["#FF0000"],
     "thickness": 3
   },
   {
     "step_name": "model_b_bbox",
     "input_image": "model_a_bbox.image",
     "predictions": "model_b.predictions",
     "copy_image": false,
     "color_palette": "CUSTOM",
     "custom_colors": ["#0000FF"],
     "thickness": 2
   }

**效果**：红色粗框=模型A结果，蓝色细框=模型B结果。

**案例4：零售商品识别**

识别货架上的商品并用不同颜色标注不同品类。

.. code-block:: json

   {
     "step_name": "product_bbox_display",
     "input_image": "shelf.camera",
     "predictions": "product_detection.predictions",
     "copy_image": true,
     "color_palette": "CUSTOM",
     "custom_colors": [
       "#FF3B30",
       "#FF9500",
       "#FFCC00",
       "#34C759",
       "#007AFF",
       "#5856D6",
       "#AF52DE",
       "#FF2D55"
     ],
     "color_axis": "CLASS",
     "thickness": 3,
     "corner_roundness": 6
   }

颜色方案参考
------------

**常用配色方案**

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - 方案名称
     - HEX颜色代码
     - 适用场景
   * - 高对比度
     - #FF0000, #00FF00, #0000FF, #FFFF00
     - 演示、教学
   * - iOS风格
     - #FF3B30, #FF9500, #FFCC00, #34C759, #007AFF
     - 现代应用
   * - 安防标准
     - #FF0000, #FFA500, #FFFF00, #00FF00
     - 监控系统
   * - 柔和配色
     - #E57373, #81C784, #64B5F6, #FFB74D
     - 报告、文档

**预定义调色板**

- ``DEFAULT``：系统默认的均衡配色
- ``VIRIDIS``：从紫到黄的渐变（如果支持）
- ``RAINBOW``：彩虹色系（如果支持）
- ``PASTEL``：柔和的粉彩色系（如果支持）

性能参考
--------

边界框绘制是轻量级操作，对性能影响很小：

- **640×480图像**：<1ms
- **1920×1080图像**：<3ms
- **4K图像**：<10ms

影响因素：

- 边界框数量：每增加100个框约增加1-2ms
- 线条粗细：粗线条略微增加绘制时间
- 圆角处理：圆角矩形比直角略慢（约10-20%）

相关节点
--------

**可视化节点系列**

- :ref:`标签显示` - 在边界框旁显示类别标签和置信度
- :ref:`掩码显示` - 显示分割掩码
- :ref:`多边形显示` - 使用多边形轮廓显示
- :ref:`关键点显示` - 显示关键点和骨架
- :ref:`颜色显示` - 用颜色填充检测区域

**组合使用**

典型的可视化工作流：

1. 边界框显示（本节点）- 标注物体位置
2. 标签显示 - 添加类别名称
3. 置信度显示 - 显示检测置信度

**注意事项**

- 多个可视化节点叠加时，确保正确设置 **Copy Image** 参数
- 按照可视化顺序连接节点
- 最后一个节点可以设置 **Copy Image** 为False以节省内存

故障排查
--------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - 问题现象
     - 解决方案
   * - 边界框没有显示
     - 检查Predictions Display是否正确连接；检查检测模型是否有输出
   * - 边界框颜色不对
     - 确认Color Palette和Custom Colors配置；检查类别顺序
   * - 图像变黑或变白
     - 检查输入图像格式；确认Copy Image设置
   * - 性能下降明显
     - 减少边界框数量；降低线条粗细；禁用圆角
   * - 圆角不显示
     - 增加Corner Roundness值；增加线条粗细

注意事项
--------

- 边界框显示是最常用的可视化方式，适合快速查看检测结果
- 对于高分辨率图像，建议相应增加边界框粗细以确保可见性
- 自定义颜色时，确保颜色数量足够覆盖所有类别
- 在暗色背景上避免使用深色边界框，亮色背景上避免使用浅色边界框
- 多个可视化节点叠加时注意图像传递的正确性
- 边界框只显示矩形框，不包含标签文字，需要配合标签显示节点使用

技术说明
--------

边界框数据格式通常包含：

- ``x``, ``y``：左上角坐标
- ``width``, ``height``：框的宽度和高度
- ``class``：类别标签
- ``confidence``：置信度（0-1）

节点会自动读取这些信息并绘制相应的矩形框。

