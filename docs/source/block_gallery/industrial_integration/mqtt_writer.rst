.. _MQTT Writer:

MQTT Writer
===========

简介
----

向 MQTT Broker 发布消息。

输入 / 输出
-----------

- 输入：消息负载（文本/JSON）
- 输出：发送状态

参数
----

.. list-table::
   :header-rows: 1
   :widths: 24 52 24

   * - 参数
     - 说明
     - 示例/ ``默认值``
   * - 节点名称
     - 工作流中该节点的名称。
     - ``mqtt_writer_1``
   * - 备注
     - 可选备注信息，记录用途。
     - ``留空``
   * - Broker 地址
     - MQTT Broker 地址（含端口）。
     - ``mqtt://localhost:1883``
   * - 主题
     - 发布的 Topic。
     - ``/daoai/topic``
   * - QoS
     - 服务质量等级 0/1/2。
     - ``0``
   * - 保留消息
     - 是否设置 retain 标志。
     - ``False``
   * - 用户名
     - 可选认证用户名。
     - ``留空``
   * - 密码
     - 可选认证密码。
     - ``留空``


