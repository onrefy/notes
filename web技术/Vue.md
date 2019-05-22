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

所以总结一下，计算属性只有在需要本身数据计算交互的时候使用。



### 绑定class和style

### 绑定class

```html
<div v-bind:class="{ active: isActive }"></div>
```

绑定总是使用对象语法：active是否存在取决于isActive



也可以使用变量去代替

```html
<div v-bind:class="classObject"></div>
```

```javascript
data: {
  classObject: {
    active: true,
    'text-danger': false
  }
}
```

那么变量可以写到计算属性之中：

```javascript
data: {
  isActive: true,
  error: null
},
computed: {
  classObject: function () {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
```

#### 使用数组语法绑定多个class

```html
<div v-bind:class="[activeClass, errorClass]"></div>
```

```javascript
data: {
  activeClass: 'active',
  errorClass: 'text-danger'
}
```

### 绑定style

```html
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

```javascript
data: {
  activeColor: 'red',
  fontSize: 30
}
```

数组语法和class相同

**注意：JavaScript中的truly不等于true，truly是经过转换后未true的值**

## 条件渲染

### v-if v-else v-else-if

v-if直接决定一个元素是否被渲染

```html
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
```



#### 使用template来打包渲染

```html
<template v-if="ok">
  <h1>Title</h1>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</template>
```

#### vue会高度利用重复的元素来加快渲染，可以通过key来管理

```html
<template v-if="loginType === 'username'">
  <label>Username</label>
  <input placeholder="Enter your username">
</template>
<template v-else>
  <label>Email</label>
  <input placeholder="Enter your email address">
</template>
```

上面代码中重新输出input不会改变已有内容，因为vue会重复利用input元素，而input元素只是修改了placeholder属性。

如果不想让vue利用重复元素加快渲染，可以使用key属性：

```html
<template v-if="loginType === 'username'">
  <label>Username</label>
  <input placeholder="Enter your username" key="username-input">
</template>
<template v-else>
  <label>Email</label>
  <input placeholder="Enter your email address" key="email-input">
</template>
```



### v-show

v-show仅仅修改的是元素的display属性



### v-show 和 v-if

v-if 切换开销大

v-show初始渲染开销大

