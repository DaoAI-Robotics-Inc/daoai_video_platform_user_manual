.. _通用检测模型(快):

通用检测模型(快)
=================

简介
----

这是一个轻量、加速推理的通用目标检测模型模板，适用于对实时性有较高要求的场景（例如监控、移动端预筛查等）。本页为模型说明模板，包含输入/输出定义、示例场景、配置参数说明与推荐使用场景。

输入/输出
--------

- 输入（Input）:
	- 图像（单帧）: RGB 或 BGR 格式，常见尺寸为 `640x480`、`1280x720` 等。建议先统一缩放到模型训练时的输入尺寸并进行归一化。
	- 可选元数据: 相机 ID、时间戳（用于后端关联）。

- 输出（Output）:
	- `detections`: 检测到的目标列表，每个条目包含 `label`、`score`、`bbox`。其中 `bbox` 推荐格式为 `[x_min, y_min, x_max, y_max]`（像素坐标）。
	- `inference_time_ms`（可选）: 单张图片推理耗时（毫秒）。

场景示例
--------

示例 1 — 摄像头实时预警：

- 摄像头采集 → 图像预处理（resize、normalize）→ 模型推理 → 后处理（NMS、score filtering）→ 报警规则触发。

示例 2 — 批量视频帧离线分析：

- 从视频抽帧 → 并行推理（批处理）→ 聚合检测结果并保存为 CSV/JSON。

配置参数详解
------------

下面列出模板中常见的配置参数与含义，实际字段名请与项目中的配置文件或推理服务对齐。

- `model_name` (string): 模型标识，例如 `general_detection_fast_v1`。
- `input_size` (list[int]): 模型输入尺寸，[width, height]，例如 `[640, 480]`。
- `score_threshold` (float): 置信度阈值，低于该值的检测将被过滤，默认 `0.3`。
- `nms_iou_threshold` (float): NMS 的 IoU 阈值，默认 `0.45`。
- `max_detections` (int): 每张图像的最大返回检测数，默认 `100`。
- `preprocessing` (dict): 预处理流程说明，例如 `resize`, `normalize`（提供均值/方差）。

示例配置片段（YAML/JSON 风格）::

		model_name: "general_detection_fast_v1"
		input_size: [640, 480]
		score_threshold: 0.35
		nms_iou_threshold: 0.45
		max_detections: 50
		preprocessing:
			resize: "stretch"  # 可选: shortest, crop, stretch
			normalize:
				mean: [0.485, 0.456, 0.406]
				std: [0.229, 0.224, 0.225]

使用建议 & 注意事项
------------------

- 推理性能: 对延迟敏感的部署请优先使用 `input_size` 较小的模型变体，或在推理端使用 TensorRT/ONNX Runtime 的优化。
- 颜色通道顺序: 明确模型期望的通道顺序（RGB vs BGR），在预处理阶段统一。
- NMS 与后处理: 对于密集目标场景，适当降低 `score_threshold` 并调低 `nms_iou_threshold` 以减少漏检。

示例快速开始（伪代码）
---------------------

.. code-block:: python

		# 加载模型（伪示例）
		model = load_model("general_detection_fast_v1")

		# 单张图像推理
		img = read_image("frame.jpg")
		pre = preprocess(img, size=(640,480))
		outs = model.predict(pre)
		dets = postprocess(outs, score_thr=0.35, nms_iou=0.45)

常见问题（FAQ）
--------------

- 为什么检测结果有大量重复框？

	可能是 NMS 阈值过大或模型锚框配置与输入尺寸不匹配，请检查 `nms_iou_threshold` 与 `input_size` 是否与训练参数一致。

- 模型在某些类别上表现差，如何调优？

	尝试增加训练数据、使用类别级别的置信度阈值，或在后处理时加入类别白名单/黑名单策略。

参考链接
------

- 模型训练规范请参考对应训练仓库的 README（若存在）。