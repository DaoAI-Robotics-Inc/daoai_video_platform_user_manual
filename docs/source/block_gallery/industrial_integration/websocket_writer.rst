.. _WebSocket数据发送:

WebSocket数据发送
==================

简介
----

向远程 WebSocket Server 发送请求/消息。

输入 / 输出
-----------

- 输入：消息负载（文本/JSON）
- 输出：发送状态或响应

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
     - ``websocket_writer_1``
   * - 备注
     - 可选备注信息，记录用途。
     - ``留空``
   * - WebSocket 地址
     - 目标 WebSocket 服务器地址。
     - ``ws://localhost:8080/ws``
   * - 消息数据
     - 要发送的文本或 JSON。
     - 选择上游数据
   * - 认证信息
     - 可选 Token/账号。
     - ``留空``


