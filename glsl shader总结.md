# glsl shader总结

1. shader的核心思路就是它是对每一个点进行的操作，它的难点在于对每一个点的操作是如何变为形状的。

2. `smoothstep(startValue, endValue,indexValue）`

   当startValue和endValue十分相近的时候相当于通过这个值做一个阶梯

   `smoothstep-smoothstep`

   当两个十分相近的时候相当于做一个峰值

3. 每一个参数左加右减、下加上减

4. 颜色中使用1-表示反向