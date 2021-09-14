# vex功能整理

这篇技术笔记注重的是vex的实用知识，以问题为导向来阐述vex功能

## 1. 基本结构

1. 如何定义结构体？

## 2. 获取数据

1. @ 适用于vex作用的单位之上

2. 如何得到点的数据？

   point(<geometry>,  <attribName>, <point>)

   pointattrib(<geometry>,<attribName>, <point>, <&success>)

   

   注意：

   在vex中临时定义的属性没有办法通过这种办法找到。

   

3. 如何得到prim(vertex)的数据？

   prim || primattrib  和 point部分一样

4. 如何得到点周围的点？

   nearpoints()

5. 如何得到一个点相邻的点？

   neighbours()

6. 如何得到一个prim上的点？

   primpoints()

7. 如何得到一个prim上点的个数？

8. 如何得到一个geometry上的点？

   npoints(<geometry>)

9. 如何得到一个group上的点？

   expandpointgroup(<geometry>, <name>)

## 3. 操作点线面

1. 如何生成一个点？

   int addpoint(<geometry>, <pointPos>)

   int addpoint(<geometry>, <point>)

2. 删除一个点？

   int removepoint(<gemometry>, <point>)

3. 如何删除一个点的同时但是不影响不受这个点影响的面的存在？（或者相反）

   int removepoint(<geometry>, <points>, <是否需要删除这些面，是1，不是0>)

4. 如何修改一个点的属性？

   int setpointattrib(<geometry>,<attribName>,<point>,<value>,<mode='set'>)

5. 如何设置一个点的group？

   setpointgroup()

6. 如何生成一条线？

   int addprim(<geometry>,<type='polyline'>,<point>,<point>...)

7. 如何生成一个面？

   将addprim中的type=poly即可

## 4. 操作数据

1. 如何快速找到两个向量之间的比例向量？

   lerp


# 文件思想数目为17个 文件单位思想为1.0495626822157436