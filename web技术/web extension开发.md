# 应用扩展





## 是什么



应用扩展有两种，一种是browser action，另一种是page action,区别在与action是否和页面的类型有关 



### 包括了

- manifest文件 * 1 
- html文件 1+ 
- 可选js等其他文件 



### 最后

所有文件打包到一个crx压缩文件中，使用Chrome Developer Dasher自动生成.crx文件 



### 如何引用文件

``` 
chrome-extension://<extensionID>/<pathToFile>
```

其中extensionID是每一个应用程序扩展自己生成的唯一ID

### manifest.json

``` json
"name": "My Extension",
"version": "2.1",
"description": "Gets information from Google.",
"icons": { "128": "icon_128.png" },
"background_page": "bg.html",
"permissions": ["http://*.google.com/", "https://*.google.com/"],
"browser_action": {
"default_title": "",
"default_icon": "icon_19.png",
"default_popup": "popup.html"
}
```

###background.html

作为主页的存在

### popup.html

作为分页面的存在







# 文件思想数目为-1个 文件单位思想为0.0