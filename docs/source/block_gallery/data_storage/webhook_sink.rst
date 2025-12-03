.. _Webhook接收:

Webhook接收
==================

简介
----

向远程 API 发送带有工作流结果的请求

输入 / 输出
-----------

- 输入：任意数据
- 输出：HTTP响应

参数
----

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - 参数
     - 说明
     - 默认值
   * - url
     - Webhook URL
     - 无
   * - method
     - HTTP方法（POST/PUT）
     - POST
   * - headers
     - 自定义请求头
     - {}

使用步骤
--------

1. 在工作流编辑器中添加本模块。
2. 配置Webhook URL和HTTP方法。
3. 点击保存。

注意事项
--------

- 支持自定义请求头和认证。

