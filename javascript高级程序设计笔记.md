# JavaScript高级程序设计

## 第5章：引用类型

### 5.5 Function类型

1.foo.call(this, arg1,arg2,arg3) == foo.apply(this, arguments)==this.foo(arg1, arg2, arg3)

2.bind方法，将函数与所在域绑定

```javascript
var module = {
  x: 42,
  getX: function() {
    return this.x;
  }
}

var unboundGetX = module.getX;
console.log(unboundGetX()); // The function gets invoked at the global scope
// expected output: undefined

var boundGetX = unboundGetX.bind(module);
console.log(boundGetX());
// expected output: 42
```



### 5.6 基本包装类型

#### 5.6.4 String类型

2. 字符串的操作方法
   * concat(string0, string1, string2...)
   * slice/substring(startIndex, endIndex)
   * substr(startIndex, number)
   * 当只有一个参数的时候，都是将字符串末尾作为结束位置
   * 当参数为负数时：
     * slice: 会将负数与字符串长度相加
     * substr：第一个参数和字符串长度相加，第二个参数变为0
     * substring: 所有负数变为0
   * 注意所有方法都没有改变原来的字符串
3. 字符串的位置方法
   * indexOf() & lastIndexOf() 都是从字符串中查找一个字符串并且返回位置，没有找到则返回-1
   * indexOf从头开始找，lastIndexOf从尾巴开始找
   * 都可以接受第二个参数，表示从哪里开始查找
4. trim()
   * 功能：返回一个删除字符串前和后的空格后的副本
   * ⚠️：没有改变原来字符串
5. 大小写
   * toUpperCase() & toLowerCase()
6. 匹配方法
   * match：返回一个数组
   * search：返回从头开始的第一个符合匹配的索引，否则返回-1
   * repalce：替换❓❓❓涉及正则表达式

### 5.7 单体内置对象

#### 5.7.1 Global对象

兜底儿对象

* uri是什么？和url有什么区别？

  uri在网页中指的是网页的唯一编码，就像人的身份证，而url是uri的一种，但是它是通过地址的形式进行的记录，就像人的家庭地址

* eval方法：

  eval(string):直接将字符串解析为代码，所以提供了外部输入代码（又叫代码注入）的可能

  * 严格模式下外部无法访问eval中的变量函数
  * eval中的变量函数不会被提升

* window对象是global对象在js中的对应，但是有更多的功能

#### 5.7.2 Math对象

1. Math对象的属性

   | 属性       | 含义     |
   | ---------- | -------- |
   | Math.E     | 自然对数 |
   | Math.LN10  | 10对数   |
   | Math.SQRT2 | 根号二   |
   | Math.PI    | pi       |
   |            |          |

2. min() & max()可以接受任意多的数值

   * 使用max找到数组最大值：

     ```javascript
     Math.max.apply(Math,Array);
     ```

   * 上面的操作也可以使用…[展开操作符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

     等价于

     ```javascript
     Math.max(...Array);
     ```

3. * ceil向上取整
   * floor向下取整
   * round四舍五入

4. 其他方法：

   * sin(), cos(), tan()
   * asin(x), acos(x), atan(y, x)



## 第5.5章 [MV*模式的发展](https://github.com/livoras/blog/issues/11)

#### GUI程序的问题与解决方案

1. 图形界面中 人的行为触发应用逻辑(applicatoin logic)触发业务逻辑(business logic)

2. 职责分离(Seperation of Duty):

   * View: 管理用户界面的层次
   * Model: 应用程序的数据

3. Smalltalk-80 MVC

   用户通过View操作，View操作被捕捉后移交Controller处理、调用Model的接口

   当Model发生改变的时候，**观察者模式**通知View，之后View向Model请求数据

   ⚠️：Controlller没有对View进行操作的能力，View的更新是自己通过观察者模式进行的更新

   **这样的好处在于当存在多个View的时候View自己更新会更加好控制**

   * 优点：
     1. Swappable Controller: 更换应用逻辑时只需要更换一个Controller就可以了。
     2. 多View同时更新

   * 缺点：

     1. 很难测试Controller，当没有UI状态下很难测试Controller，当Model更新的时候，无法对断定View的更新是否和Controller相关。

     2. View由于通过观察者模式依赖Model，所以没有办法组件化。

4. MVC Model 2/JSP Model 2/Model 2

   可以理解为MVC在服务器环境下的特殊用途

   客户端发出请求，服务器接受后通过路由交给特殊的Controller，Controller对Model进行操作，之后使用数据渲染模板，返回客户端

   ⚠️：其中**观察者模式**被取消所以Model 2并不能称为严格的MVC

5. MVP

   Controller变为Presenter，其中观察者模式的功能从View到Model变为Presenter到Model，并且由Presenter调用View的接口进行操作。

   * 优点

     基本上就是MVC缺点反过来

   * 缺点

     Presenter臃肿难以维护

6. MVVM

   VM即View Model，可以简单理解为一个View的抽象，VM使用一个Binder来将View和Model进行绑定，即Tow-way data-binding双向数据绑定。





## 第6章 面向对象的程序设计

#### attribute特性

1. 数据属性

* [[Configuration]]修改数据属性，能否删除数据

* [[Enumerable]]是否可迭代

* [[Writable]]是否可修改

* [[Value]]是否有键值对

* 修改属性，Object.defineProperty(对象，属性，{键值对})

  ```javascript
  var person = {};
  Object.defineProperty(person, "name", {
      configurable: false,
      value: "zyz"
  });
  alert(person.name);
  delete(person.name);
  alert(person.name);
  ```

2. 访问器属性
   * [[Get]]: 在读取属性的时候调用的函数
   * [[Set]]: 在写入属性的时候调用的函数
   * 其中Vue.js使用了访问器属性的这个性质，使Model被改变的时候和写入的时候能够影响View

3. 定义多个属性的特性

   Object.defineProperties()

4. 读取属性的特性

   Object.getOwnPropertyDescriptior()

   ```javascript
   var book = {};
   
   Object.defineProperties(book, {
       _year: {
           value: 2004
       },
       
       edition: {
           value: 1
       },
       
       year: {
           get: function(){
               return this._year;
           },
           
           set: function(newValue){
               if (newValue > 2004) {
                   this._year = newValue;
                   this.edition += newValue - 2004;
               }
           }
       }
   })
   
   
   var description = Object.getOwnPropertyDescriptor(book, "_year");
   alert(description.value);
   ```

   

#### 创建对象

1. 允许在对象中直接使用变量名，相当于变量名变为属性名字，变量值变为属性的值

   ```javascript
   var foo = 'bar'
   var baz = {foo}
   //相当于{foo: 'bar'}
   
   //另一个例子
   function f(x,y) {
       return {x, y};
   }
   //相当于
   function f(x, y){
       return(x: x, y: y);
   }
   ```

   2.方法也可以简写：

   ```javascript
   //原来
   var o = {
       method: function() {
           return "Hello!";
       }
   }
   
   //Now
   var o = {
       method(){
           return "Hello!";
       }
   }
   ```

   可能会有一些奇怪的效果：

   ```javascript
   var obj = {
       class () {}
   };
   //等同于
   var obj = {
       'class': function() {}
   }
   ```

   如果方法是一个Generator，前面需要加入一个*

   ```javascript
   var obj = {
       *m() {
           yield 'hello world';
       }
   }
   ```

   #### Class基本语法

   *这里着重研究ES6中的class用法，对原来的prototype用法不再深究*

   1. 取值函数和存值函数，`get` 和`set` 关键字，拦截属性的存取行为

      ```javascript
      class MyClass {
        constructor() {
          // ...
        }
        get prop() {
          return 'getter';
        }
        set prop(value) {
          console.log('setter: '+value);
        }
      }
      
      let inst = new MyClass();
      
      inst.prop = 123;
      // setter: 123
      
      inst.prop
      // 'getter'
      ```

   2. class不会被提升

   3. 属性的名字可以使用表达式

   4. 静态方法：这个方法不会被实例继承：

      ```javascript
      class Foo {
        static classMethod() {
          return 'hello';
        }
      }
      
      Foo.classMethod() // 'hello'
      
      var foo = new Foo();
      foo.classMethod()
      // TypeError: foo.classMethod is not a function
      
      ```

      但是可以被子类继承：

      ```javascript
      class Foo {
        static classMethod() {
          return 'hello';
        }
      }
      
      class Bar extends Foo {
      }
      
      Bar.classMethod() // 'hello'
      ```

   5. 属性的新写法：

      可以将属性直接写到类的最顶层：

      ```javascript
      class foo {
        bar = 'hello';
        baz = 'world';
      
        constructor() {
          // ...
        }
      }
      ```

   6. class a

      a === a.prototype.constructor

      new.target === a



## 第7章 函数表达式

#### 7.0 函数提升

```javascript
//会有变量提升
function sayHi(){
    alert('Hi!');
}

//不会有变量提升
var sayHi = function(){
    alert('Hi!');
}
```

* 函数外面加上括号的含义

  ```javascript
  (function f(){})//这里就是立即执行
  var f = (function f(){})//这里就是立即返回函数
  ```

  

#### 7.1递归

一个小问题：

```javascript
function factorial(num){
    if (num <= 1){
        return 1;
    } else {
        return num * factorial(num - 1);
    }
}

var newFactorial = factorial;
factorial = null;
newFactorial(8);//ERROR!
```

原因在于函数中使用的是`factorial(num - 1)`

* 解决方案1，使用arguments.callee

  arguments.callee指向的是当前运行的函数

  ```javascript
  function factorial(num){
      ...
      return num * arguments.callee(num - 1);
  }
  ```

  ⚠️：严格模式下argumetns.callee是被禁用的

* 解决方案2，使用匿名函数立即执行

  ```javascript
  var factorial = (function f(num){
      if (num <= 1){
          return 1;
      } else {
          return num * f(num - 1);
      }
  });
  ```



#### 7.2 闭包

指的是有权访问另一个函数作用域中的变量的函数。

1. 通常的实现形式：

   ```javascript
   funcition fOut(num){
       return function(num2){
           return num2 *  num;
       }
   }
   ```

   这样的话即使函数在外部也可以访问num变量。

2. 实现形式：通过作用域链来达到目的

   同时意味着：闭包只能去的包含函数中任何变量的最后一个值

   ```javascript
   function f1(){
       var result = new Array();
       
       for (var i=0; i < 10; i++){
           result[i] = function(){
               return i;
           }
       }
   }
   //但是实际上result[1]...result[10]返回的都是10
   ```

   可以通过构造另一个匿名函数来强行达到目的

   ```javascript
   function f1(){
       var result = new Array();
       
       for (var i=0; i < 10; i++){
           result[i] = function(num){
               return function(){
                  return num; 
               }(i);
           }
       }
       
       return result;
   }
   ```

   

#### 7.3 模仿块级作用域

使用(function (){代码块})()来达到私有作用域的作用



#### 7.4 私有变量



#### ...

### 第13章 事件

#### 13.1 事件流

定义：从页面接受事件的顺序

* 事件冒泡：从具体到不具体
* 事件捕获：反上

尽量使用事件冒泡



## 第15章 canvas绘图

#### 15.1 基本设置

```javascript
var drawing = document.getElementById('canvas');

if (drawing.getContext){
    var context = drawing.getContext('2d');
}
```

#### 15.2 形状绘制

* Property
  * fillStyle
  * strokeStyle
  * lineWidth
  * lineCap
    * butt
    * round
    * square
  * lineJoin
    * round
    * bevel
    * miter
* method
  * fillRect()
  * strokeRect()
  * clearRect()

#### 15.3 path绘制









