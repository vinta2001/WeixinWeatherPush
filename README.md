# daily_reminder
给女朋友做的微信天气推送

教程链接

https://www.coolapk.com/feed/38579891?shareKey=NGI3ZGZlZTM4MDBjNjMwMzdlM2M~&shareUid=3198334&shareFrom=com.coolapk.app_4.10




网址1   http://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index
网址2   https://id.qweather.com/


模板内容如下：

今天是：{{date.DATA}} 

下面开始为宝贝播报{{region.DATA}}的天气(#^.^#) 
今日天气：{{weather.DATA}} 
最低气温：{{min_temperature.DATA}} ℃ 
最高气温：{{max_temperature.DATA}} ℃ 
当前气温：{{temp.DATA}} ℃ 
今日风向：{{wind_dir.DATA}} 

今日穿衣建议：{{tips.DATA}} 

今日星座运势：
综合指数:{{total.DATA}}
财运指数:{{luck.DATA}}
健康指数:{{health_.DATA}}
今日概述:{{total_.DATA}}

今天我们在一起{{love_day.DATA}}天啦 

*{{birthday1.DATA}} 
*{{birthday2.DATA}} 

EN: {{note_en.DATA}} 
CN: {{note_ch.DATA}}



天气key生成教程
![image](https://raw.githubusercontent.com/limoest/daily_reminder/main/%E5%92%8C%E9%A3%8E%E5%A4%A9%E6%B0%94key%E7%94%9F%E6%88%90.png)


可以去天行数据申请各种各样的接口用来推送  
![image](https://raw.githubusercontent.com/limoest/daily_reminder/main/others/Snipaste_2022-08-24_12-13-19.png)
![image](https://raw.githubusercontent.com/limoest/daily_reminder/main/others/Snipaste.png)



有别的建议欢迎留言
