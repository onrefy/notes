# Vue.js

## Vue实例

### 数据和方法

所有Vue示例中的data的属性都是响应式的

```javascript
var data = { a:1 }

var vm = new Vue({
    data: data
})

vm.a == data.a
//true

vm.a = 2
data.a // 3

//反之亦然

data.a = 3
vm.a // 3
```



注意必须是实例化中的data数据会被双向绑定！

使用`Object.freeze()`会锁定实例对象从而防止修改现有的属性



### 生命周期钩子（类似python的魔法方法）

`created`创建一个实例被创建之后执行的代码：

```javascript
new Vue ({
    data: {
        a: 1
    },
    created: function (){
        console.log('a is ' + this.a);
    }
})
```

注意：最好不要使用箭头函数！因为this会出现问题

**图例**

![Vue 实例生命周期](https://cn.vuejs.org/images/lifecycle.png)

## 模板语法

### 插值

#### 文本插值

```html
<span>Message: {{msg}}</span>
```

#### 解读原始html

```html
<p>
    Using v-html directly:<span v-html:"rawhtmlj"></span>
</p>
```

注意：容易导致XSS攻击

#### 附加到html特性上

```html
<div v-bind:id="dynamicId"></div>
<button v-bind:disabled="isButtonDisabled">
    Button
</button>
```

#### 使用JavaScript表达式

```html
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div v-bind:id="'list-' + id"></div>
```



注意：**只能是单个表达式**



### 指令

```html
<p v-if="seen">
    现在
</p>
```

使用seen的值来派出p元素



#### 绑定参数

```html
<a v-bind:href="url"></a>
<a v-on:click="doSomething">...</a>
//这里的参数是监听的事件名
```

#### 动态参数

使用方括号来表示一个指定的参数：

```html
<a v-bind:[attributeName]="url"></a>
```

这里的attribute会使用data中的某一个参数

### 缩写

```html
<!-- 完整语法 -->
<a v-bind:href="url">...</a>

<!-- 缩写 -->
<a :href="url">...</a>


<!-- 完整语法 -->
<a v-on:click="doSomething">...</a>

<!-- 缩写 -->
<a @click="doSomething">...</a>
```



## 计算属性

就是一个computed生命周期钩子：

```html
<div id="example">
  <p>Original message: "{{ message }}"</p>
  <p>Computed reversed message: "{{ reversedMessage }}"</p>
</div>
```

```javascript
var vm = new Vue({
  el: '#example',
  data: {
    message: 'Hello'
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  }
})
```

这种方法和使用methods的方法的区别在于这个当原来的变量改变的一瞬间就开始变化，而方法则是在函数调用之后才被调用

## 侦听属性

一下两组代码完全相同，体会之：

```html
<div id="demo">{{ fullName }}</div>
```

```javascript
var vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar',
    fullName: 'Foo Bar'
  },
  watch: {
    firstName: function (val) {
      this.fullName = val + ' ' + this.lastName
    },
    lastName: function (val) {
      this.fullName = this.firstName + ' ' + val
    }
  }
})
```

```javascript
var vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar'
  },
  computed: {
    fullName: function () {
      return this.firstName + ' ' + this.lastName
    }
  }
})
```

#### 计算属性的setter：

```javascript
//...
computed: {
  fullName: {
    // getter
    get: function () {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {
      var names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
//...
```

