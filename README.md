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
GET /posts?id=_id&date=_date

_id:贴子的id,默认为0

_date:文章的日期,默认为2000年1月1日0点0分0秒(具体格式再定)
