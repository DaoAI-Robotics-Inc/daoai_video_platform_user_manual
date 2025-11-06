常见问题 
===========

.. contents::
    :local:

如何避免 GPU 进入低功耗模式导致推理变慢？
-------------------------------------------------------------

在某些设备上，如果连续使用模型推理，执行速度非常快（例如 10 毫秒以内）；但如果两个推理调用之间的间隔较长（例如超过 5 秒），则可能出现执行时间大幅变慢的情况（例如变成 100 毫秒以上 然后之后回到10ms以内）。

这是由于 GPU 进入低功耗状态导致的性能下降问题。

为了保证您的设备始终以高性能运行，建议您进行以下设置：

1. 在 NVIDIA 控制面板中设置： 
    - 打开 NVIDIA Control Panel → Manage 3D Settings。 
    - 找到 Power management mode，设置为 Prefer maximum performance。

2. 在系统电源管理中设置： 
    - 打开 控制面板 → 电源选项。 
    - 选择 高性能 电源计划。

设置示例如下图所示：

.. image:: images/nv_power.png
   :width: 600px

.. image:: images/ctrlpanel_power.png
   :width: 600px

通过上述设置，可以避免 GPU 进入节能模式，从而在长时间等待后保持推理性能。
