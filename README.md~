

#学院小助手后台开发文档(协议)

包括以下功能:
- **主页**
- **校内新闻**
- **院系通知**
- **失物招领**
- **吐槽水贴**
- **个人信息**
- **其他**


----------

主页
--

http://hustcomputerapp.com （暂定）
<h3>获取主页图片</h3>
GET /news_img                         	 **获取新闻图片**

GET /notification_img             	 **获取通知图片**

GET /lostandfound_img                    **获取失物招领图片**

GET /posts_img                           **获取帖子图片**


----------

校内新闻
----
获取学院新闻:

GET /news?id=_id&date=_date

_id:文章的id,默认为0

_date:文章的日期,默认为2000年1月1日0点0分0秒(具体格式再定)

<h4>return(返回为json字符串):</h4>
```
{
	"id":xxx,
	"date":xxxx,
	"title":xxxx,
	"article":xxxx,
	"zan":xxx,
	"review":xxxx

}
```
文章(article)部分已经结构化:
```
[
  {
    "type": "text",
    "body": "123",
    "style": {}            这里提供字体等格式,具体分为"b"(加
                           粗),"font"(字体),"size"(字的大
                           小),"color"(字的颜色),"a"(超链接)
  },
  {
    "type": "image",
    "src": "xxx.jpg",      这里将提供图片的url
    "style": {}            这里提供图片的具体格式,和前端格式相同
  }
]
```
评论(review)部分已经结构化:
```
[
	"id":xxx,
	"portrait":xxx/img,    这里将提供图片的url
	"date":xxxx,
	{
		"type":"text",
		"body":"123",
		"style":{}         这里同上
	},
	{
		"type":"emoji",
		"body":{:4_885:}
	}

]
```

----------

院系通知
----

获取学院的通知:

GET /notification?id=_id&date=_date

_id:通知的id,默认为0

_date:通知的日期,默认为2000年1月1日0点0分0秒(具体格式再定)

<h4>return(返回为json字符串):</h4>
```
{
	"id":xxx,
	"date":xxxx,
	"title":xxxx,
	"article":xxxx
}
```
文章(article)的结构化同校内新闻版块


----------
失物招领
----

获取失物招领信息:

GET /lostandfound?id=_id&date=_date

_id:通知的id,默认为0

_date:失物招领的日期,默认为2000年1月1日0点0分0秒(具体格式再定)

<h4>return(返回为json字符串):</h4>
```
{
	"id":xxx,
	"date":xxxx,
	"title":xxxx,
	"article":xxxx,
	"found":x              这里是数字,1为失主认领,0为未认领,默认为0         
}
```
文章(article)的结构化同校内新闻版块


----------

吐槽水贴
----

<h3>1.获取贴子内容:</h3>

GET /posts?id=_id&date=_date

_id:贴子的id,默认为0

_date:文章的日期,默认为2000年1月1日0点0分0秒(具体格式再定)

<h4>return(返回为json字符串):</h4>
```
{
	"id":xxx,
	"date":xxxx,
	"title":xxxx,
	"writer":xxxx,
	"portrait":xxx/img,    这里将提供楼主的头像url
	"posts":xxxx
	    
}
```
贴子(posts)部分已经结构化:
```
[
	{
		"floor":xxx,        这里是第几楼
		"user_id":xxxx,     发贴人的id   
		"portrait":xxx/img, 这里将提供发贴人头像的url
		"article":xxxx,
		"zan":xxx,          赞的数量
		"review":xxx,
		"date":xxx
	},
	{
		"floor":xxx,        这里是第几楼
		"user_id":xxxx,     发贴人的id   
		"portrait":xxx/img, 这里将提供发贴人头像的url
		"article":xxxx,
		"review":xx,
		"date":xxx
	}
	    
]
```
在posts中:
article部分的结构化和校内新闻的一样,可以协商简化
review部分结构化如下:
```
[
	{
		"user_id":xxx,      回复者的id
		"reviewed_id":xxx,  被回复者的id
		{
		"type":"text",
		"body":"123",
		"style":{}         
		},
		{
		"type":"emoji",
		"body":{:4_885:}
		}
		
	}
]
```

<h3>2.发表贴子有关内容:</h3>

<h4>(1)发布主题(贴子)</h4>

POST格式:
```
POST http://hustcomputerapp.com/posts HTTP/1.1 
Content-Type: application/json;charset=utf-8

{
	"user_id":xxx,
	"date":xxx,
	"article":xxx,
	"security_code":xxx     这里是验证码
}
```
json表单的article字段和校内新闻的一样,可以协商简化

<h4>(2)发布楼层</h4>

POST格式:(请求的url里面包括贴子的id)
```
POST http://hustcomputerapp.com/posts/(\d+) HTTP/1.1 
Content-Type: application/json;charset=utf-8

{
	"floor":xxx,
	"user_id":xxx,
	"date":xxx,
	"article":xxx,
	"security_code":xxx     这里是验证码
}
```
json表单的article字段同上

<h4>(3)发表楼层中回复</h4>
POST格式:(请求的url里面包括贴子的id)
```
POST http://hustcomputerapp.com/posts/(\d+) HTTP/1.1 
Content-Type: application/json;charset=utf-8

{
	"floor":xxx,
	"review":xxx,
	"date":xxx,
	"security_code":xxx     这里是验证码
}
```
其中的review字段见"获取贴子内容"

<h4>(4)点赞</h4>
POST格式:(请求的url里面包括贴子的id)
```
POST http://hustcomputerapp.com/posts/(\d+) HTTP/1.1 
Content-Type: application/json;

{
	"zan_id":xxx,           赞的id
	"floor":xxx
}
```

<h3>3.修改贴子有关内容:</h3>

<h4>(1)删除楼层</h4>
POST格式:(请求的url里面包括贴子的id)
```
POST http://hustcomputerapp.com/posts/(\d+) HTTP/1.1 
Content-Type: application/json;

{
	"delete_id":xxx,        服务器端会进行一次匹配
	"floor":xxx             如果为1的话,则删除贴子
}
```
<h4>(2)取消赞</h4>
POST格式:(请求的url里面包括贴子的id)
```
POST http://hustcomputerapp.com/posts/(\d+) HTTP/1.1 
Content-Type: application/json;

{
	"cancel_id":xxx,        取消赞的id
	"floor":xxx
}
```

至于为什么没有删回复功能是因为百度贴吧好像也没有删回复的功能23333


----------

个人信息
----
这里的post应该加密
<h3>1.登录:</h3>

POST格式:
```
POST https://hustcomputerapp.com/user HTTP/1.1 
Content-Type: application/json;charset=utf-8

{
	"user_id":xxx,
	"password":xxx,         密码
}
```

<h3>2.注册:</h3>

POST格式:
```
POST https://hustcomputerapp.com/user HTTP/1.1 
Content-Type: application/json;charset=utf-8

{
	"user_id":xxx,
	"stu_id":xxx,           学号
	"sex":x,                数字,0为女性,1为男性
	"introduction":xxx,     自我介绍
	"security_code":xxx     这里是验证码
}
```
