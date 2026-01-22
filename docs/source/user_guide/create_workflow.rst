创建您的第一个工作流
=====================

本节将带您在 DaoAI 天眼平台中，从零开始创建并运行您的第一个工作流。
通过一个完整示例，您将了解如何在可视化界面中连接各个功能模块，
并运行一条从数据输入到模型推理再到业务输出的完整 AI 视觉流程。

.. contents::
   :local:
   :depth: 2


前提条件
--------

在开始之前，请确保已完成以下准备工作：

- 已成功登录 DaoAI 天眼平台。
- 已准备好可用于推理的模型（目标检测 / 分类 / 分割模型，可为平台内置或自训练模型）。
- 已准备好至少一组测试数据，例如单张图片、本地文件夹、视频文件或 RTSP 摄像头流。


步骤 1：创建新工作流
---------------------

1. 打开 DaoAI 天眼平台 ``http://<your_server_ip>:38080/dashboard`` 。
2. 在上方导航栏中点击 **“工作流 (Workflows)”**。
3. 进入工作流管理页面后，点击 **“创建工作流”**，系统将进入工作流编辑画布界面。。
4. 输入工作流名称，例如 ``新工作流``。
5. 点击保存。

    .. only:: zh

        .. image:: images/workflow_overview.png
            :alt: DaoAI 天眼工作流概览
            :width: 80%

    .. only:: en

        .. image:: images/workflow_overview.png
            :alt: DaoAI Video Analysis Platform workflow overview
            :width: 80%


步骤 2：添加模型推理模块
-------------------------

1. 点击添加模型，添加一个 **模型推理模块**：

    可以选择：
    - DaoAI World 模型， 选择一个从DaoAI World 训练并导出的模型：

        - 目标检测模型模块（Object Detection）
        - 分类模型模块（Classification）
        - 视力分割模型模块（Instance Segmentation）
        - 关键点检测模型模块（Keypoint Detection）
        - 语义分割模型模块（Segmentation）
        - 混合模型模块（Mixed Model）
        - OCR 模型模块（OCR Model）

    - 通用检测模型模块（General Detection）

本示例中，我们选择 **通用检测模型（General Detection）** 模块进行演示。
该模型支持使用英文自然语言描述目标类别，
系统将基于智能多模态模型自动完成目标识别与定位。

    .. image:: images/add_model_1.png
        :alt: Add Model in Workflow
        :width: 80%

添加后，配置模型的标签，使用英文自然语言输入需要识别的目标类别，例如 ``person`` 、 ``car`` 、 ``truck`` 等。

    .. image:: images/add_model_2.png
        :alt: Add Model in Workflow
        :width: 80%

模型模块将在工作流运行时对视频流的每帧图像数据进行实时推理，并输出预测结果。

步骤 3：添加业务逻辑与可视化模块
--------------------------------

1. 根据业务需求，添加 **逻辑/规则模块**，例如：

   - 检测过滤模块: 按照标签，置信度，等条件过滤检测结果；这里我们设置过滤person标签；
      .. image:: images/filter_module.png
         :alt: Filter Module
         :width: 60%

   - 条件判断模块: 根据配置的条件语句进行判断，并触发对应的分支逻辑；这里我们设置当检测到person数量大于5时触发报警；
      .. image:: images/condition_module.png
         :alt: Condition Module
         :width: 60%

4. 继续添加 **可视化模块**，用于在图像上叠加绘制检测结果，并在条件判断模块中将 ``下一步`` 参数配置为对应的可视化模块，使工作流在条件满足后继续执行该可视化节点

   - 边界框可视化模块： 在图像上绘制目标检测的边界框； ``预测显示`` 参数选择模型模块的输出结果；
   - 标签可视化模块： 在图像上显示目标类别标签和置信度； ``预测显示`` 参数选择模型模块的输出结果；
   - 仪表盘显示模块： 在监控大屏中显示可视化结果。

      .. image:: images/add_vis_nodes.png
         :alt: Visualization Module
         :width: 60%

步骤 4：添加事件保存模块
---------------------

根据业务需求，添加 **事件保存模块**，用于记录和存储检测到的事件。

   - 输入事件类型
   - 选择要展示的可视化输入，作为图片保存内容
   - 是否保存视频：选择保存视频时，系统会将事件发生的前后15秒的视频片段和事件一同保存。
   - 最大视频时长：事件发生时，单个视频文件的最大时长，单位为秒，默认30秒，也就是事件发生前后15秒，总共30秒的视频片段。
   
   .. image:: images/event_saver_node.png
      :width: 60%



步骤 5：保存并运行工作流
-------------------------

1. 点击画布右上角的 **“保存”** 按钮保存工作流配置。
2. 上传一张图片，点击 **“运行 / 测试”** 开始执行工作流：
3. 运行完成后，您可以查看输出的json结果。以及可视化结果。

    .. image:: images/test_workflow.png
        :alt: Workflow Result
        :width: 80%
    .. image:: images/test_workflow2.png
        :alt: Workflow Result
        :width: 80%

示例：基础检测工作流
---------------------

下面示例展示了一个最常见的工作流结构，
实现“目标检测 → 结果可视化 → 输出保存”的完整流程：

.. only:: zh

    .. code-block:: text

       [数据输入]
            ↓
       [目标检测模型]
            ↓
       [业务逻辑判断]
            ↓
       [可视化显示]
            ↓
       [事件保存]

.. only:: en

    .. code-block:: text

       [Data Input]
            ↓
       [Object Detection Model]
            ↓
       [Business Logic]
            ↓
       [Visualization]
            ↓
       [Event Saver]

运行工作流的多种方式
------------------------------------------

您的工作流现已保存至 DaoAI 天眼系统服务器。这意味着您可以通过多种方式运行它，包括：

- 在平台中完成相机配置后直接运行；
- 通过 HTTP API 进行调用与集成。

详情请阅读下一章 :ref:`运行工作流`

用于快速复现的工作流定义
---------------------------------------------------------------

为便于复现与分享，下面提供一份可直接复制到 UI 编辑器中的工作流定义。

   .. image:: images/share_workflow.png
      :alt: Workflow Definition
      :width: 60%

将Json的内容复制后，在工作流的左下角打开高级编辑器，粘贴内容并保存即可。


工作流定义
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
   "version": "1.0",
   "inputs": [
      {
         "type": "WorkflowImage",
         "name": "image"
      }
   ],
   "steps": [
      {
         "type": "daoai/general_obj_det@v1",
         "name": "general_object_detection_1",
         "comments": null,
         "images": "$inputs.image",
         "classes": [
         "person",
         "car",
         "truck"
         ],
         "confidence_threshold": 0.8,
         "label_confidence_thresholds": null,
         "max_detections": 100
      },
      {
         "type": "core/detections_filter@v1",
         "name": "detections_filter_1",
         "comments": null,
         "predictions": "$steps.general_object_detection_1.predictions",
         "image": "$inputs.image",
         "operations": [
         {
            "type": "DetectionsFilter",
            "filter_operation": {
               "type": "StatementGroup",
               "statements": [
               {
                  "type": "BinaryStatement",
                  "left_operand": {
                     "type": "DynamicOperand",
                     "operations": [
                     {
                        "type": "ExtractDetectionProperty",
                        "property_name": "class_name"
                     }
                     ]
                  },
                  "comparator": {
                     "type": "in (Sequence)"
                  },
                  "right_operand": {
                     "type": "StaticOperand",
                     "value": [
                     "person"
                     ]
                  }
               }
               ]
            }
         }
         ],
         "uistate": {
         "operations": {
            "filterBy": "class_confidence",
            "parentClassName": "",
            "objectClassEnabled": true,
            "objectClassType": "include",
            "objectClasses": "person",
            "attributeEnabled": false,
            "attributeType": "include",
            "attributes": "",
            "confidenceEnabled": false,
            "confidenceOperator": ">=",
            "confidenceValue": 0.5,
            "imageInput": "$inputs.image",
            "detectionSizeOperator": "<=",
            "detectionSizeValue": 5,
            "detectionLocation": "in",
            "detectionReferencePoint": "center",
            "zoneDefinition": "Define in Editor",
            "zonePoints": [],
            "zoneJson": "[]"
         }
         }
      },
      {
         "type": "core/continue_if@v1",
         "name": "continue_if_1",
         "comments": null,
         "condition_statement": {
         "type": "StatementGroup",
         "statements": [
            {
               "type": "BinaryStatement",
               "left_operand": {
               "type": "DynamicOperand",
               "operand_name": "left",
               "operations": [
                  {
                     "type": "SequenceLength"
                  }
               ]
               },
               "comparator": {
               "type": "(Number) >="
               },
               "right_operand": {
               "type": "StaticOperand",
               "value": 1
               }
            }
         ],
         "operator": "and",
         "uistate": {
            "leftOperand": "$steps.detections_filter_1.predictions",
            "detectionsEvaluationProperty": "detection_count",
            "selectedFilterType": "not_selected",
            "isClassFilteringActive": false,
            "isAttrFilteringActive": false,
            "isConfidenceFilteringActive": false,
            "classSetInclusionMode": "include",
            "classList": [],
            "attrList": [],
            "attrSetInclusionMode": "include",
            "confidenceThreshold": 0.5,
            "confidenceOperator": ">=",
            "referenceImage": null,
            "sizeThreshold": 5,
            "sizeThresholdOperator": "<=",
            "zoneOperator": "in",
            "zonePoints": [],
            "detectionReferencePoint": "center",
            "isZoneStatic": true,
            "dynamicZone": null,
            "runtimeParameter": null,
            "parentClassName": "",
            "confidenceAggregationMode": "max",
            "confidenceAggregationOperator": ">=",
            "confidenceAggregationThreshold": 0.5,
            "comparator": "(Number) ==",
            "comparisonType": "Statically",
            "comparisonValue": "0",
            "detectionsNumberOperator": "(Number) >=",
            "detectionsNumberThreshold": 1,
            "extractedImageProperty": "height",
            "propertyValueOperator": ">=",
            "referenceValue": 1,
            "isReferenceValueStatic": true,
            "nonImageInputOperation": "(Number) ==",
            "isMultiLabel": false,
            "multiLabelOperation": "==",
            "isFilteringEnabled": false
         }
         },
         "evaluation_parameters": {
         "left": "$steps.detections_filter_1.predictions"
         },
         "image": "$inputs.image",
         "next_steps": [
         "$steps.bounding_box_visualization_1"
         ]
      },
      {
         "type": "core/bounding_box_visualization@v1",
         "name": "bounding_box_visualization_1",
         "comments": null,
         "image": "$inputs.image",
         "copy_image": true,
         "predictions": "$steps.detections_filter_1.predictions",
         "color_palette": "DEFAULT",
         "palette_size": 10,
         "custom_colors": [],
         "color_axis": "CLASS",
         "thickness": 2,
         "roundness": 0
      },
      {
         "type": "core/label_visualization@v1",
         "name": "label_visualization_1",
         "comments": null,
         "image": "$steps.bounding_box_visualization_1.image",
         "copy_image": true,
         "predictions": "$steps.detections_filter_1.predictions",
         "color_palette": "DEFAULT",
         "palette_size": 10,
         "custom_colors": [],
         "color_axis": "CLASS",
         "text": "Class and Confidence",
         "text_position": "TOP_LEFT",
         "text_color": "WHITE",
         "text_scale": 1,
         "text_thickness": 1,
         "text_padding": 10,
         "border_radius": 0
      },
      {
         "type": "daoai/dashboard_visualization@v1",
         "name": "dashboard_visualization_1",
         "comments": null,
         "image": "$steps.label_visualization_1.image"
      },
      {
         "type": "daoai/event_saver@v1",
         "name": "event_saver_1",
         "comments": null,
         "event_type": "High foot traffic",
         "image": "$steps.label_visualization_1.image",
         "original_image": "$inputs.image",
         "save_video": true,
         "video_length_seconds": 30,
         "cooldown_seconds": 20,
         "cooldown_session_key": null,
         "per_type_cooldown_seconds": 30
      }
   ],
   "outputs": [
      {
         "type": "JsonField",
         "name": "general_object_detection_1_1",
         "coordinates_system": "own",
         "selector": "$steps.general_object_detection_1.predictions"
      },
      {
         "type": "JsonField",
         "name": "detections_filter_1_1",
         "coordinates_system": "own",
         "selector": "$steps.detections_filter_1.predictions"
      },
      {
         "type": "JsonField",
         "name": "bounding_box_visualization_1_1",
         "coordinates_system": "own",
         "selector": "$steps.bounding_box_visualization_1.image"
      },
      {
         "type": "JsonField",
         "name": "label_visualization_1_1",
         "coordinates_system": "own",
         "selector": "$steps.label_visualization_1.image"
      },
      {
         "type": "JsonField",
         "name": "event_saver_1_1",
         "coordinates_system": "own",
         "selector": "$steps.event_saver_1.error_status"
      },
      {
         "type": "JsonField",
         "name": "event_saver_1_2",
         "coordinates_system": "own",
         "selector": "$steps.event_saver_1.throttling_status"
      },
      {
         "type": "JsonField",
         "name": "event_saver_1_3",
         "coordinates_system": "own",
         "selector": "$steps.event_saver_1.message"
      },
      {
         "type": "JsonField",
         "name": "event_saver_1_4",
         "coordinates_system": "own",
         "selector": "$steps.event_saver_1.image_url"
      },
      {
         "type": "JsonField",
         "name": "event_saver_1_5",
         "coordinates_system": "own",
         "selector": "$steps.event_saver_1.video_url"
      }
   ]
   }

