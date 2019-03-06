# glsl shader总结

1. shader的核心思路就是它是对每一个点进行的操作，它的难点在于对每一个点的操作是如何变为形状的。

2. `smoothstep(startValue, endValue,indexValue）`

   当startValue和endValue十分相近的时候相当于通过这个值做一个阶梯

   `smoothstep-smoothstep`

   当两个十分相近的时候相当于做一个峰值

3. 每一个参数左加右减、下加上减

4. 颜色中使用1-表示反向

5. 直接使用函数构造形状的会导致函数值是零为中心的渐变；使用smoothstep可以将渐变变为阶梯。

6. 使用for循环进行颜色差值处理：

   ```glsl
   vec3 c;
   float t;
   for (int i=0;i<3;i++){
   	t += interval;
       c[i] = f(t);
   }
   ```



### glsl 函数

1. glsl中的函数必须提前声明

2. 函数不可以使用递归

3. 参数为数组的情况：

   ```glsl
   void particles(vec3 values[30]){
       
   }
   ```

4. 函数声明参数的时候可以有标识符去对参数进行特殊的使用

   * in：默认参数的使用方法，复制参数
   * out：参数不能读入，只能写入
   * inout：参数可以读入，也可以写入

5. 