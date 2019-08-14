# js canvas学习

### 基本用法

```html
<canvas id='test' width='150' height='150'></canvas>
```

* 如果没有设置初始的长与宽，那么canvas会自动设置为300pixels宽和150pixels高
* 可以被css调整长和宽，但是调整的过程中如果不尊重比率就会有形变。
* 所以如果要调整canvas的长和宽，最好不要使用css



### 当canvas不被支持的时候

```html
<canvas id="stockGraph" width="150" height="150">
  current stock price: $3.15 + 0.15
</canvas>

<canvas id="clock" width="150" height="150">
  <img src="images/clock.png" width="150" height="150" alt=""/>
</canvas>
```



### 坐标系统

和p5一样

### 绘图系统

#### 基础形状只有矩形

`fillRect(x, y, width, height)`画矩形

`strokeRect()`

`clearRect()` 清理矩形空间

#### path形状

1. `beginPath()`

2. `Path methods`

3. `closePath()`

   使用一条直线来连接起始点和终点。

4. `stroke()`

5. `fill()`

#### Path Methods

* moveTo()

* lineTo()

* arc(cx, cy, radius, startAngle, endAngle, anticlockwise)

* arcTo(x1, y1, x2, y2, radius)

  arc中的角度都是弧度制

* quadraticCurveTo(cp1x, cp1y, x, y)

  贝塞尔二级曲线

* bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)

* rect在绘制路径的时候添加，自动有一个moveTo(x,y)



#### Path2d: 用来存储一个路径

```javascript
function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');

    var rectangle = new Path2D();
    rectangle.rect(10, 10, 50, 50);

    var circle = new Path2D();
    circle.moveTo(125, 35);
    circle.arc(100, 35, 25, 0, 2 * Math.PI);

    ctx.stroke(rectangle);
    ctx.fill(circle);
  }
```

#### 也可以与svg沟通

```javascript
var p = new Path2D('M10 10 h 80 h -80 Z');
```

### 样式系统

#### 颜色

使用

* fillStyle
* strokeStyle
* 默认是'#000000'

``` javascript
ctx.fillStyle = 'orange';
ctx.fillStyle = '#ffa500';
ctx.fillStyle = 'rgb(255, 165, 0)';
ctx.fillStyle = 'rgba(255, 165, 0, 1)';
```



#### 透明度

`globalAlpha =  transparencyValue`设置全局的透明度



#### 线条样式

* lineWidth = value

* lineCap = type

  * butt

    正方角，不过头

  * round

    圆角

  * sqaure

    正方角，过头

* lineJoin = type

  * round

    圆倒角

  * bevel

    方倒角

  * miter

    延长曲线倒角

* miterLimit = value 

  控制倒角的最大范围

* 虚线：

  1. getLineDash()

     返回一个代表虚线的非负数序列

     比如说[4,2]代表当前画线长4，间隔2

  2. setLineDash(segments)

     设置当前虚线样式

     ```javascript
     ctx.setLineDash([4,2]);
     ```

     

  3. lineDashOffset = value

     设置虚线位移



#### 渐变

1. 生成渐变对象

   ```javascript
   createLinearGradient(x1, y1, x2, y2)
   createRadialGradient(x1, y1, r1, x2, y2, r2)
   ```

   [**??? 为什么radial gradient需要两个中心？？？**]()

2. 设置渐变控制点：

   ```javascript
   addColorStop(position, color);
   ```

   其中color代表了css颜色的字符串

3. 最后使用`fillStyle`来调整样式

   ```javascript
   var g = ctx.createLinearGradient(0, 0, 0, 150);
   g.addColorStop(.5, 'white');
   ctx.fillStyle = g;
   ```

   ​		

   

   

#### 图案

1. 创建图案对象

   `createPattern(image, type)`

   其中`image`指的是`CavasImageSource`可以是图片、视频、甚至是其他canvas

   type:

   * repeat
   * repeat-x
   * repeat-y
   * no-repeat



#### 阴影

注意，阴影只能够设置全局，所以我认为这个功能挺鸡肋的

* shadowoffsetX = float
* shadowOffsetY = float
* shdowBlur = float
* shadowColor = color



#### 填充规则

但使用`fill`或者`clip`或者`isPointPath`有两种选择计算是否fill，

两套规则的本质是判断哪里是曲线的内部，哪里是曲线的外部

* "non-zero"

  从一个点作射线，去到若干个相交点，如果这个点在曲线中是顺时针，则+1，逆时针则-1，最终和为0，则这个点在外部，否则在内部。

* "even-odd"

  假设曲线的区域中有一个点，从曲线作射线，数相交的点的个数，如果这个个数是奇数，那么这个点在内部，如果这个个数是偶数，那么这个点在外部。

  

### 文字

1. 基础用法

   ```javascript
   fillText(text, x, y [, maxWidth]);
   strokeText(text, x, y, [, maxWidth]);
   ```

2. 文字样式

   * font = value

   * textAlign = value

     * start
     * end
     * left
     * right
     * center

   * textBaseLine = value

     * top
     * hanging
     * middle
     * alphabetic
     * ideographic
     * bottom

     默认是`alphabetic`

3. 测量文字长度

   `measureText()`返回一个`TextMetrics`对象，其中有属性`width`代表文字的真实的pixel长度



### 图片

1. 获得图片

   * `HTMLImageElement`

     可以通过`Image()`来创建，也可以直接通过<img>元素来获得

   * `SVGImageElement`

     通过<image>元素来获得

   * `HTMLVideoElement`

     通过<video>元素来获得

   * `HTMLCanvasElement`

     通过<canvas>元素来获得

   * 使用同一个页面的图片

     * document.images获得页面内全部的图片的序列
     * document.getElementById()

   * 使用本地文件

     ```javascript
     c
     ```
     
     注意需要加载完才用drawImage();
   
2. 绘制图片

   `drawImage(image, x, y)`

   `drawImage(image, x, y, width, height)`

   `drawImage(image, sliceX, sliceY, sliceWidth, sliceHeight, positionX, positionY, width, height)`

3. 是否对图片使用平滑渲染

   imageSmoothingEnabled = true



### 变换

1. 存储状态和复原状态

   * 状态包括有：
     * 基础样式：strokeStyle, fillStyle, linWidth, lineCap, lineJoin, miterLimit, lineDashOffset
     * 阴影：shadow balabala
     * 字体：font, textAlign, textBaseLine
     * 全局样式：globalAlpha, globalCompositeOperation, direction, imageSmoothingEnabled
     * 变换
   * 使用save()来存储当前的状态，使用restore()来回到上一个save的状态

2. translate(x, y)

   和p5一样

3. rotate(angle)

   中心始终是原点

4. scale(x, y)

   大于1放大，小于1缩小

5. transform(a, b, c, d, e, f)

   线性变换，abcd决定平面形变，ef决定平移矩阵为
   $$
   {
   \left[ \begin{array}{ccc}
   a & c & e\\
   b & d & f\\
   0 & 0 & 1
   \end{array} 
   \right ]}
   $$



### 动画

`requestAnimationFrame()`

```javascript
function draw(){
  //draw something
  window.requestAnimationFrame(draw);
}
draw();
```





### 操作像素

1. ImageData对象

   属性：

   * width

   * height

   * data:

     这是一个Uint8ClampedArray存储了图片的像素信息，有`height` * `width` * 4 bytes个data，序列就是0到`height` * `width` * 4 - 1

     * 所以如果需要获得第200行，50列的蓝色通道数据，那么index就是

       ( 200 * ImageData.width + 50 ) * 4 + 2

2. 创建ImageData：

   ```javascript
   var myImageData = ctx.createImageData(width, height)
   ```

   利用现有的ImageData的维度创建新的ImgeData，注意这个操作并不会复制ImageData，只是有一样的维度

   ```javascript
   var newImageData = ctx.createImageData(myImageData)
   ```

3. 获得当前canvas的pixels：

   ```javascript
   var myImageData = ctx.getImageData(left, top, width, height)
   ```

   注意使用超出canvas边界的数据都会返回0

4. 获取某一个点的pixel：

   ```javascript
   function pick(event) {
     var x = event.layerX;
     var y = event.layerY;
     var pixel = ctx.getImageData(x, y, 1, 1);
     var data = pixel.data;
     var rgba = 'rgba(' + data[0] + ',' + data[1] +
                ',' + data[2] + ',' + (data[3] / 255) + ')';
     color.style.background =  rgba;
     color.textContent = rgba;
   }
   ```

   

5. 使用ImageData设置canvas

   ```javascript
   ctx.putImageData(myImageData, x, y)
   ```

6. 下载图片

   ```javascript
   var url = canvas.toDataURL('image/png')
   var url = canvas.toDataURL('image/jpeg', quality)
   ```

   其中默认的png为96dpi

   而jpeg的quality属性处于0到1之间0最低，1最高

   ```javascript
   var img = canvas.toDataURL('image/png');
   document.write('<img src="' + img + '"/>');
   ```

   或者

   ```html
   <a href = 'javascript:canvas.toDataURL('image/jpeg)' download = 'download'>Download as jpeg</a>
   ```

   或者

   ```javascript
   var download = function(){
     var link = document.createElement('a');
     link.download = 'filename.png';
     link.href = canvas.toDataURL();
     link.click();
   }
   ```



### 加速渲染的技巧

1. 将重复性的渲染工作先用一个offscreenCanvas存储，然后直接调用这个canvas

   ```javascript
   myCanvas.offscreenCanvas = document.createElement('canvas');
   myCanvas.offscreenCanvas.width = myCanvas.width;
   myCanvas.offscreenCanvas.height = myCanvas.height;
   
   myCanvas.getContext('2d').drawImage(myCanvas.offsecreenCanvas, 0, 0);
   ```

2. 尽量使用整数

3. 最好不要缩放图片

4. 使用多个canvas重合在一起，减少渲染量

   ```html
   <div id = 'stage'>
     <canvas id = 'ui-layer' width = '300' height = '100'></canvas>
     <canvas id = 'game-layer' width = '300' height = '100'></canvas>
     <canvas id = 'bg-layer' width = '300' height = '100'></canvas>
   </div>
   <style>
     #stage {
       width: 300px;
       height: 100px;
       position: relative;
       border: 2px solid black;
     }
     
     canvas { position: absolute; }
     #ui-layer { z-index: 3; }
     #game-layer { z-index: 2; }
     #bg-layer { z-index: 1; }
   </style>
   ```

   

5. 使用css，因为css通过gpu运算

6. 关闭alpha通道：

   ```javascript
   var ctx = canvas.getContext('2d', { alpha: false } );
   ```

7. 多个操作绑定在一起

8. 尽量避免shadowBlur

9. 尽量避免text rendering