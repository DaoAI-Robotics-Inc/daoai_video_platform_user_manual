视频（9 项）
================

处理视频流中的对象跟踪、计数和分析。

.. toctree::
   :maxdepth: 1
   :hidden:

   buffer
   byte_tracker
   detections_stabilizer
   identify_changes
   identify_outliers
   line_counter
   path_deviation
   time_in_zone
   velocity

.. list-table::
   :header-rows: 0
   :widths: 33 34 33
   :class: block-cards

   * - :ref:`缓冲区`

       返回传递给它的最后 'length' 个值的数组
     - :ref:`字节追踪器`

       通过 ByteTrack 跟踪并更新视频帧中的对象位置
     - :ref:`检测稳定器`

       对对频帧应用平滑算法以减少噪声间隔
   * - :ref:`识别更改`

       通过较入问数识别与先前数据的差异
     - :ref:`异常检测`

       识别与先前数据相比的异常数入向量
     - :ref:`线条计数`

       统计穿过线条的检测数量
   * - :ref:`路径偏移`

       计算对象与参考路径之间的距离或距离
     - :ref:`区域内存在时间`

       在区域内跟踪对象时间
     - :ref:`速度`

       计算跟踪对象的速度和速度，并进行平滑处理和单位转换

