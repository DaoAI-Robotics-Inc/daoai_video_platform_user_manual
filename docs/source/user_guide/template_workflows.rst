典型工作流示例
======================

本页汇总 DaoAI 天眼系统内置的“模板工作流”示例。可在工作流编辑器中导入、查看并按需调整参数与区域配置。

.. contents::
    :local:
    :depth: 2


办公场景
------------------

人员离岗检测
~~~~~~~~~~~~~~~~~~~~~~~~~

- 用途：识别人员是否离开指定办公区域（离岗/值班空缺）。需在编辑器中配置“监控区域”坐标。
- 组成与流程：
    - 通用检测模型：标签输入 ``person`` 检测场景中的人员；
    - 检测过滤: 过滤出置信度低于0.5的检测结果；
    - 高速追踪：为检测到的对象分配并维护稳定的轨迹/ID，便于持续分析；
    - 区域内存在时间：统计在区域内或者外停留时长；
    - 属性定义: 提取区域内存在时间节点的 离开区域的时间值 ``time_out_of_zone``；
    - 条件继续：当停留时长 ``>= 15`` 秒时，进入后续步骤（可视化/事件保存）；
    - 可视化与事件保存:

        - 在图像上绘制“监控区域”多边形与半透明遮罩；
        - 在仪表盘中展示带标注的图像；
        - 保存事件与视频片段。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: primary

    .. literalinclude:: template_workflows/office/No_Staff.json
       :language: json
       :linenos:



人员聚集检测
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 用途：识别指定区域内的人员聚集/拥挤情况。
- 组成与流程：
    - 人员检测：标签输入 ``person`` 检测画面中的人员；
    - 区域过滤：在设定区域内筛选检测结果；
    - 条件继续：当区域内人数 ``>= 4`` 时，进入后续步骤；
    - 可视化与事件保存：叠加框与标签并保存事件。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: primary

    .. literalinclude:: template_workflows/office/crowded.json
       :language: json
       :linenos:

     

异常行为检测
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 用途：识别抽烟、打电话、玩手机、摔倒、睡岗、翻越围栏等异常/不当行为（需自训练对应模型）。
- 组成与流程：
    - 行为检测模型：输出异常行为类别与位置；
    - 类别过滤：仅保留目标异常类别；
    - 条件继续：当检测数量 ``>= 1`` 时，进入后续步骤；
    - 可视化与事件保存：绘制框与标签、保存事件并在仪表盘展示。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: primary

    .. literalinclude:: template_workflows/office/abnormal_behavior.json
       :language: json
       :linenos:


长时停留检测
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 用途：统计目标在指定区域内的停留时长，识别过长停留（如长时间玩手机）。
- 组成与流程：
    - 通用检测模型：检测场景中的目标对象；
    - 检测过滤：按需要在设定区域或类别上筛选用于跟踪的检测结果；
    - 目标跟踪：为检测到的对象分配并维护稳定的轨迹/ID；
    - 区域内存在时间：统计在区内停留时长；
    - 属性定义: 提取区域内存在时间节点的 离开区域的时间值 ``time_in_zone``；
    - 条件继续：当停留时间达到阈值（示例为 ``>= 1``，实际可在编辑器设定秒数）时，进入后续步骤（可视化/事件保存）；
    - 可视化与事件保存：叠加框与“Time In Zone”标签，保存事件与视频片段；

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: primary

    .. literalinclude:: template_workflows/office/Stay_Long.json
       :language: json
       :linenos:


Highway 场景
------------

交通拥堵检测
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 用途：结合车辆检测、跟踪与速度估计，识别道路拥堵程度（轻度/中度/重度），并输出事件类型与摘要。
- 组成与流程：
    - 目标检测：检测车、卡车、摩托等对象；
    - 目标跟踪：为车辆分配并维护稳定轨迹/ID；
    - 速度估计：依据标定多边形、方向点与边缘距离计算车速（km/h）；
    - 在区时长：统计车辆在指定区域的停留时间；
    - 拥堵综合分析：融合检测、轨迹、速度与停留信息，计算占用率与拥堵等级，并输出事件类型；
    - 逻辑判断：当拥堵条件为真时继续进入可视化与事件保存；
    - 可视化与事件保存：叠加事件标签、保存图像与视频片段，并可在仪表盘展示。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: warning

    .. literalinclude:: template_workflows/highway/highway_jam.json
       :language: json
       :linenos:


昼夜模型切换
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 用途：根据时间自动切换白天/夜间检测模型，适应光照变化，保证识别稳定性（需配置模型 UID）。
- 组成与流程：
    - 自定义 Python 模块：根据当前时间输出应使用的模型 UID，；
    - 通用检测：按动态 UID 选择并运行检测模型；
    - 目标跟踪、速度估计、在区时长：与拥堵检测一致，分别统计轨迹、速度与在区停留；
    - 违法/拥堵判定：输出是否违规/拥堵及事件类型；
    - 逻辑判断：当触发条件成立时进入可视化与事件保存；
    - 可视化与事件保存：绘制事件信息并保存图像/视频，支持仪表盘展示。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: warning

    .. literalinclude:: template_workflows/highway/day_night_shift.json
       :language: json
       :linenos:



车速与行驶轨迹检测
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 用途：实时检测车辆速度并分析行驶轨迹，用于识别超速、异常减速、逆行、频繁变道等行为，辅助交通安全监管。
- 组成与流程：
    - 目标检测：检测车、卡车、摩托等对象；
    - 目标跟踪：维护稳定的车辆轨迹/ID；
    - 速度估计：通过标定与方向点计算车速；
    - 在区时长：统计在指定车道或区域的停留时间；
    - 违规/轨迹分析：综合速度、轨迹与停留信息识别超速、逆行、异常变道等；
    - 逻辑判断：当违规条件为真时进入可视化与事件保存；
    - 可视化与事件保存：叠加事件标签，保存图像/视频，并可在仪表盘展示。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: warning

    .. literalinclude:: template_workflows/highway/speed&lane.json
       :language: json
       :linenos:



Construction Site 场景
-----------------------

工地热人数统计
~~~~~~~~~~~~~~~~

- 用途：统计画面中人员数量，便于了解现场人员密度与热度。
- 组成与流程：
    - 目标检测：检测人员；
    - 检测过滤：仅保留人员且置信度 >= 0.5；
    - 属性提取：计算检测数量用于事件类型或展示；
    - 可视化与事件保存：叠加框与标签，按人数保存事件与视频片段。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: success

    .. literalinclude:: template_workflows/construction site/People_count.json
       :language: json
       :linenos:


区域占用检测
~~~~~~~~~~~~~~

- 用途：检测指定区域是否被物体占用（车、卡车、摩托、大件物品等），需在编辑器配置区域坐标。
- 组成与流程：
    - 目标检测：检测目标类别；
    - 区域过滤：在目标区域筛选检测结果；
    - 目标跟踪：维护稳定轨迹与 ID；
    - 条件继续：当区域内存在目标（数量 >= 1）进入可视化与事件保存；
    - 可视化与事件保存：绘制框与标签并保存事件。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: success

    .. literalinclude:: template_workflows/construction site/Region_Occupied.json
       :language: json
       :linenos:


作业区人员距离检测
~~~~~~~~~~~~~~~~~~~~

- 用途：检测危险/作业区域是否有人员靠近，辅助安全管控；需在编辑器配置区域坐标。
- 组成与流程：
    - 目标检测：检测人员（staff）；
    - 区域过滤：在危险区域筛选检测结果；
    - 条件继续：当区域内存在人员（数量 >= 1）进入可视化；
    - 可视化与事件保存：绘制框与标签并保存事件与视频。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: success

    .. literalinclude:: template_workflows/construction site/staff_in_danger_region.json
       :language: json
       :linenos:



灭火器存在检测
~~~~~~~~~~~~~~~~

- 用途：检测特定区域是否存在灭火器；可用于发现灭火器缺失或被挪走。
- 组成与流程：
    - 目标检测：检测灭火器；
    - 目标跟踪与可视化：绘制框与标签；
    - 越界/在区时长：统计灭火器离开区域的时间并聚合；
    - 条件继续：当离区时长达到阈值（示例 3s）进入事件保存；
    - 事件保存与仪表盘：保存图片/视频并在仪表盘展示。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: success

    .. literalinclude:: template_workflows/construction site/fire_extinguisher_spevofic_area.json
       :language: json
       :linenos:


通用
--------

发送HTTP消息
~~~~~~~~~~~~~~~~~~~~~~

- 用途：当检测到目标（示例：人员）时，触发自定义 Python 生成消息并通过 Webhook 推送到外部系统。
- 组成与流程：
    - 目标检测：检测人员；
    - 条件继续：当检测数量 >= 1 时，进入后续步骤；
    - 自定义模块：生成文本消息；


.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: info

    .. literalinclude:: template_workflows/any_scene/send_message.json
       :language: json
       :linenos:


数据采集与标注
~~~~~~~~~~~~~~~~

 用途：检测目标并将统计结果通过 HTTP 协议发送到外部服务。
 组成与流程：
     - 目标检测：检测目标类别（car）。
     - 自定义模块：发送 HTTP 请求，载荷包含 "number_of_cars_detected" 统计结果；
     - 可视化：绘制检测框用于结果展示；

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: info

    .. literalinclude:: template_workflows/any_scene/data_upload.json
       :language: json
       :linenos:



多模型逻辑检测
~~~~~~~~~~~~~~~~

- 用途：并行/串行运行多模型，通过与/或逻辑组合实现复杂条件判定和结果融合（需替换具体模型 UID）。
- 组成与流程：
    - 检测模型 A：初始目标检测；
    - 条件筛选 + 动态裁剪：对指定目标生成裁剪区域；
    - 分类模型 B/C：对裁剪图进行分类；
    - 类别替换与融合：将检测与分类结果融合，替换类别并组合为最终输出；
    - 可视化：叠加框与标签用于展示。

.. dropdown:: 查看工作流 JSON
    :icon: code
    :color: info

    .. literalinclude:: template_workflows/uncertain/multi-model.json
       :language: json
       :linenos:





