.. _OPC UA Writer Sink:

OPC UA Writer Sink
==================

简介
----

将数据写入 OPC UA 服务端节点。

输入 / 输出
-----------

- 输入：待写入的数据
- 输出：写入状态

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
     - ``opc_ua_writer_sink_1``
   * - 备注
     - 可选备注信息，记录用途。
     - ``留空``
   * - 服务器地址
     - OPC UA Server 地址。
     - ``opc.tcp://localhost:4840``
   * - 节点ID
     - 目标写入的 NodeId。
     - ``ns=2;s=MyNode``
   * - 写入数据
     - 要写入的值来源。
     - 选择上游数据
   * - 用户名
     - 可选认证用户名。
     - ``留空``
   * - 密码
     - 可选认证密码。
     - ``留空``


