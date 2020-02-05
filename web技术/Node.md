# Node.js

### npm

#### package.json

* dependencies 依赖包的安装
* repository 包代码存放的类型 git / svn
* main 定义了程序的主入口文件，require('moduleName')会加载这个文件。默认是index.js
* keywords 关键字

#### 创建模块

```terminal
npm init
npm adduser
//在npm资源库中注册用户
npm publish
```

#### 版本号

X.Y.Z 主版本号.次版本号.补丁版本号

* 修复bug，更新Z
* 增加功能，向下兼容，更新Y
* 大变动，向下不兼容，更新X



### 事件

```javascript
// 引入 events 模块
var events = require('events');
// 创建 eventEmitter 对象
var eventEmitter = new events.EventEmitter();
```

eventEmiiter — 与事件炒作有关，同时是事件触发器和事件观察者

```javascript
// 观察事件
eventEmitter.on('eventName', eventHandler);
// 触发事件
eventEmitter.emit('eventName');
```

同时emit可以给喂参数：

```javascript
//event.js
var events = require('events');
var emitter = new events.EventEmitter();
emitter.on('someEvent', function(arg1, arg2){
  console.log('listener1', arg1, arg2);
});
emitter.on('someEvent', function(arg1, arg2){
  console.log('listener2', arg1, arg2);
})
emitter.emit('someEvent', arg1, arg2);
```

同时对于观察者列表，如果触发事件，按照顺序依次发生。

常用方法：

* on(event, listener)

   常规注册监听器

* once(event, listener)

  单次监听器

* 







# 文件思想数目为9个 文件单位思想为0.6591957811470006