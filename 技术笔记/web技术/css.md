# css

## 布局



三个主要影响布局的属性：

1. position
2. float
3. display



### float属性



最初是用来让图片浮动到文字的左侧的设计

功能就是让元素浮动在父元素(parent container)之中

并且不计入渲染流，意味着因为浮动影响的其他的元素的排布虽然改变，但是属性没有改变



### position定位技术

* 静态定位

  默认位置

* 相对定位

  相对默认的移动

* 绝对定位

  移除正常布局流，放入单独图层

  找到一个祖先元素，定位和它的位置关系

* 固定定位

  相对电脑屏幕的绝对定位



### 行内元素和块级元素

* #### 块级元素：block element

  块级元素默认占一整行

* #### 行内元素：inline element

  也叫**内联元素、内嵌元素**，横向排列，直到换行

  没有固定高度和宽度

### 弹性盒子

1. 容器的display属性：

   ```css
   .box{
       display: flex;
   }
   //行内元素
   .box{
       display: inline-flex;
   }
   ```

   定义之后，子元素的flaot、clear、vertical-align失效

2. 主轴方向：

   ```css
   .box {
       flex-direction: row | row-reverse | column | colum-reverse;
   }
   ```

3. flex-wrap 换行属性

   ```css
   .box {
       flex-wrap: nowarp | wrap | wrap-reserve;
   }
   ```

4. flex-flow = 主轴方向 和 换行属性

5. justify-content 在主轴上的分布方式

   ```css
   .box {
       justify-content: flex-start | flex-end | center | space-between | space-around;
   }
   ```

6. align-items 如何根据主轴对齐

   * flex-start | flex-end | center | baseline | stretch

7. align-content 如果存在多条主轴，与容器元素的对齐方式

   * flex-startt
   * flex-end
   * center
   * space-between
   * space-around
   * stretch

8. flex-grow 主轴占比属性

   flex-shrink 主轴缩比属性

   flex-basis  主轴占长度属性

   flex 上面三个合起来







# 文件思想数目为16个 文件单位思想为0.8370260955194485