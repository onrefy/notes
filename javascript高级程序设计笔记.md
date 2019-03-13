# JavaScript高级程序设计

## 第4.5章：正则表达式与模板字符串

### 1.正则表达式的构造

* 使用斜杠产生：

  ```javascript
  const regex = /ab+c/
  
  const regex = /^[a-zA-Z]+[0-9]*\W?_$/gi;
  ```

* 或者调用RegExp对象的构造函数：

  ```javascript
  let regex = new RegExp("ab+c");
  
  let regex = new RegExp(/^[a-zA-Z]+[0-9]*\W?_$/,"gi");
                         
  let regex = new RegExp("^[a-zA-Z]+[0-9]*\W?_$","gi");
  ```

### 2.特殊字符含义规则

| 字符                                                         | 含义                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`\`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-backslash) | 这是一个字符边界，有特殊含义                                 |
| [`^`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-caret) | 匹配字符的开始                                               |
| [`$`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-dollar) | 匹配字符的结束                                               |
| [`*`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-asterisk) | 匹配前一个表达式0次或多次，等价于{0,}                        |
| [`+`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-plus) | 匹配前面一个表达式1次或者多次。等价于 {1,}                   |
| [`?`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-questionmark) | 匹配前面一个表达式0次或者1次。等价于 {0,1}。                 |
| [`.`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-dot) | （小数点）匹配除换行符之外的任何单个字符。                   |
| [`(x)`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-capturing-parentheses) | 匹配 'x' 并且记住匹配项，就像下面的例子展示的那样。括号被称为 *捕获括号*。模式`/(foo) (bar) \1 \2/`中的 '(foo)' 和 '(bar)' 匹配并记住字符串 "foo bar foo bar" 中前两个单词。模式中的 \1 和 \2 匹配字符串的后两个单词。注意 \1、\2、\n 是用在正则表达式的匹配环节。在正则表达式的替换环节，则要使用像 $1、$2、$n 这样的语法，例如，'bar foo'.replace( /(...) (...)/, '$2 $1' )。 |
| [`(?:x)`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-non-capturing-parentheses) | 匹配 'x' 但是不记住匹配项。这种叫作非捕获括号，使得你能够定义为与正则表达式运算符一起使用的子表达式。来看示例表达式 /(?:foo){1,2}/。如果表达式是 /foo{1,2}/，{1,2}将只对 ‘foo’ 的最后一个字符 ’o‘ 生效。如果使用非捕获括号，则{1,2}会匹配整个 ‘foo’ 单词。 |
| [`x(?=y)`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-lookahead) | 匹配'x'仅仅当'x'后面跟着'y'.这种叫做正向肯定查找。例如，/Jack(?=Sprat)/会匹配到'Jack'仅仅当它后面跟着'Sprat'。/Jack(?=Sprat\|Frost)/匹配‘Jack’仅仅当它后面跟着'Sprat'或者是‘Frost’。但是‘Sprat’和‘Frost’都不是匹配结果的一部分。 |
| [`x(?!y)`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-negated-look-ahead) | 匹配'x'仅仅当'x'后面不跟着'y',这个叫做正向否定查找。例如，/\d+(?!\.)/匹配一个数字仅仅当这个数字后面没有跟小数点的时候。正则表达式/\d+(?!\.)/.exec("3.141")匹配‘141’而不是‘3.141’ |
| [`x|y`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-or) | 匹配‘x’或者‘y’。例如，/green\|red/匹配“green apple”中的‘green’和“red apple”中的‘red’ |
| [`{n}`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-quantifier) | n是一个正整数，匹配了前面一个字符刚好发生了n次。             |
| [`{n,m}`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-quantifier-range) | n 和 m 都是整数。匹配前面的字符至少n次，                     |
| [`[xyz\]`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-character-set) | 一个字符集合。匹配方括号中的任意字符，包括[转义序列](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Grammar_and_types)。你可以使用破折号（-）来指定一个字符范围。对于点（.）和星号（*）这样的特殊符号在一个字符集中没有特殊的意义。他们不必进行转义，不过转义也是起作用的。例如，[abcd] 和[a-d]是一样的。他们都匹配"brisket"中的‘b’,也都匹配“city”中的‘c’。/[a-z.]+/ 和/[\w.]+/与字符串“test.i.ng”匹配。 |
| [`[^xyz\]`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-negated-character-set) | 一个反向字符集。也就是说， 它匹配任何没有包含在方括号中的字符。你可以使用破折号（-）来指定一个字符范围。任何普通字符在这里都是起作用的。例如，[^abc] 和 [^a-c] 是一样的。他们匹配"brisket"中的‘r’，也匹配“chop”中的‘h’。 |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
| [`\d`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-digit) | 匹配一个数字`。``等价于[0-9]`。例如， `/\d/` 或者 `/[0-9]/` 匹配"B2 is the suite number."中的'2'。 |
| [`\D`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-non-digit) | 匹配一个非数字字符`。``等价于[^0-9]`。例如， `/\D/` 或者 `/[^0-9]/` 匹配"B2 is the suite number."中的'B' 。 |
| [`\f`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-form-feed) | 匹配一个换页符 (U+000C)。                                    |
| [`\n`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-line-feed) | 匹配一个换行符 (U+000A)。                                    |
| [`\r`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-carriage-return) | 匹配一个回车符 (U+000D)。                                    |
| [`\s`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-white-space) | 匹配一个空白字符，包括空格、制表符、换页符和换行符。等价于[ \f\n\r\t\v\u00a0\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]。例如, `/\s\w*/` 匹配"foo bar."中的' bar'。 |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
| [`\w`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-word) | 匹配一个单字字符（字母、数字或者下划线）。等价于`[A-Za-z0-9_]`。例如, `/\w/` 匹配 "apple," 中的 'a'，"$5.28,"中的 '5' 和 "3D." 中的 '3'。 |
| [`\W`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-non-word) | 匹配一个非单字字符。等价于`[^A-Za-z0-9_]`。例如, `/\W/` 或者 `/[^A-Za-z0-9_]/` 匹配 "50%." 中的 '%'。 |
| [`\*n*`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#special-backreference) | 在正则表达式中，它返回最后的第n个子捕获匹配的子字符串(捕获的数目以左括号计数)。比如 `/apple(,)\sorange\1/` 匹配"apple, orange, cherry, peach."中的'apple, orange,' 。 |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |

### 3.使用方式

#### RegExp

* exec:

  返回数组

  | 返回数组 |                                                              | 匹配到的字符串和所有被记住的子字符串。                       | `["dbbd", "bb"]` |
  | :------: | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------- |
  | `index`  | 在输入的字符串中匹配到的以0开始的索引值。                    | `1`                                                          |                  |
  | `input`  | 初始字符串。                                                 | `"cdbbdbsbz"`                                                |                  |
  |  `[0]`   | 匹配到的所有字符串（并不是匹配后记住的字符串）。注：原文"The last matched characters."，应该是原版错误。匹配到的最终字符。 | `"dbbd"`                                                     |                  |
  |  `myRe`  | `lastIndex`                                                  | 下一个匹配的索引值。（这个属性只有在使用g参数时可用在 [通过参数进行高级搜索](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#.E9.80.9A.E8.BF.87.E5.8F.82.E6.95.B0.E8.BF.9B.E8.A1.8C.E9.AB.98.E7.BA.A7.E6.90.9C.E7.B4.A2) 一节有详细的描述.) | `5`              |
  | `source` | 模式文本。在正则表达式创建时更新，不执行。                   | `"d(b+)d"`                                                   |                  |

* test:返回true or false

#### String

* march 
* replace
* search
* replace

### 通过标志进行高级搜索

* /g：全局搜索
* /i：不区分大小写



#### 如何搜索到全局的索引值？

```javascript
const exp = /a/g;
const str = 'aaa';
while (m = exp.exec(str)){
    console.log(m.index);
}
```



### 4.模板字符串

1. 基本使用方法：

   使用反引号代替单引号

   如果需要使用反引号，使用\转义

2. 多行字符串

   ```javascript
   console.log(`string text line 1
   string text line2`)
   ```

3. 插入表达式

   ```javascript
   var a = 5;
   var b = 10;
   console.log(`Fifteen is ${a + b} and 
   not ${2 * a + b}.`)
   ```

4. 嵌套模板

   ```javascript
   const classes = `header ${isLargeScreen ? '' : `icon-${item.isCollpsed ? 'expander' : 'collapser'}`}`;
   ```

   

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
   * repalce：替换



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



### 第7.5章 模块化

#### 1.导出变量

##### 导出变量的实质是让模块接口和内部变量有一个一一对应的关系



以下是错误示范：

```javascript
export 1;

var m = 1;
export m;
```

因为都是直接使用原来模块中的变量值，这是没有意义的

正确示范：

```javascript
export var m = 1;

var m = 1;
export {m};

var n = 1;
export {n as m};
```



##### 这种绑定是一种动态关系，通过接口可以拿到模块内部的实时值。



#### 2.读入

##### import的变量都是只读的，不允许改变接口。

import具有提升效果

#### 3.加载

```javascript
// circle.js

export function area(radius){
    return Math.PI * radius * radius;
}

export function circumference(radius) {
    return 2 * Math.PI * radius;
}
```

```javascript
//main.js
import { area, circumference } from './circle';

console.log(area(4));
console.log(circumference(14));
```

上面是逐一加载，下面是整体加载

```javascript
import * as circle from './circle';

console.log(circle.area(4));
console.log(circle.circumference(14));
```

#### 4.默认输出

```javascript

```



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









## 第17章 错误处理

#### 1. try-catch语句

```javascript
try{
    window.someNonexistentFuntion();
} catch (e){
    alert('An error happened!');
    alert(e.message);
}
```

#### 2. finnally语句

无论try、catch语句中是什么都会执行，甚至是return

```javascript
function testFinally(){
    try {
        return 2;
    } catch (e) {
        return 1;
    } finally {
        return 0;
    }
}
```

#### 3.错误类型

* Error：

  基类型，主要用于开发者抛出自定义错误

* EvalError：

  给eval赋值，没有将其当作函数使用

  ```javascript
  new eval();//Throw evalError
  eval = foo;//Throw evalError
  ```

  

* RangeError:

  数值超出相应范围

  ```javascript
  var items1 = new Array(-20);
  var items2 = new Array(Number.MAX_VALUE);
  ```

  

* ReferenceError:

  找不到对象错误，熟知的“object expected”错误

* SyntaxError

  语法错误

* TypeError

  操作特定于类型的操作时，变量的类型并不符合要求

* URIError

  使用encodeURI和decodeURI发生错误



#### 利用错误的属性类型进行操作

```javascript
try{
    someFunction();
} catch(e) {
    if (e instanceof TypeError){
        
    } else if (e instanceof ReferenceError){
        
    } else {};
}
```

