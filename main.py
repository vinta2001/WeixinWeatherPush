import random
from time import localtime
from requests import get, post
from datetime import datetime, date
from zhdate import ZhDate
import sys
import os


def get_color():
    # 获取随机颜色
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    color_list = get_colors(100)
    return random.choice(color_list)


def get_access_token():
    # appId
    app_id = config["app_id"]
    # appSecret
    app_secret = config["app_secret"]
    post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
                .format(app_id, app_secret))
    try:
        access_token = get(post_url).json()['access_token']
    except KeyError:
        print("获取access_token失败，请检查app_id和app_secret是否正确")
        os.system("pause")
        sys.exit(1)
    # print(access_token)
    return access_token


def get_weather():
    with open('config.txt', encoding='utf-8') as f:
        config = eval(f.read())
        # print(config)
        API = config['weather_key']
    url = 'https://apis.tianapi.com/tianqi/index?key={}&&city=西安&type=1'.format(API)
    # print(url)
    headers = {'Content-Length': '59',
               'Content-Type': ' application/x-www-form-urlencoded'}
    data = get(url).json()['result']
    weather = data['weather']
    maxTemp = data['highest']
    minTemp = data['lowest']
    realTemp = data['real']
    wind = data['wind']
    weather_tips = data['tips']
    return weather, realTemp, maxTemp, minTemp, wind, weather_tips


def get_birthday(birthday, year, today):
    birthday_year = birthday.split("-")[0]
    # 判断是否为农历生日
    if birthday_year[0] == "r":
        r_mouth = int(birthday.split("-")[1])
        r_day = int(birthday.split("-")[2])
        # 获取农历生日的今年对应的月和日
        try:
            birthday = ZhDate(year, r_mouth, r_day).to_datetime().date()
        except TypeError:
            print("请检查生日的日子是否在今年存在")
            os.system("pause")
            sys.exit(1)
        birthday_month = birthday.month
        birthday_day = birthday.day
        # 今年生日
        year_date = date(year, birthday_month, birthday_day)

    else:
        # 获取国历生日的今年对应月和日
        birthday_month = int(birthday.split("-")[1])
        birthday_day = int(birthday.split("-")[2])
        # 今年生日
        year_date = date(year, birthday_month, birthday_day)
    # 计算生日年份，如果还没过，按当年减，如果过了需要+1
    if today > year_date:
        if birthday_year[0] == "r":
            # 获取农历明年生日的月和日
            r_last_birthday = ZhDate((year + 1), r_mouth, r_day).to_datetime().date()
            birth_date = date((year + 1), r_last_birthday.month, r_last_birthday.day)
        else:
            birth_date = date((year + 1), birthday_month, birthday_day)
        birth_day = str(birth_date.__sub__(today)).split(" ")[0]
    elif today == year_date:
        birth_day = 0
    else:
        birth_date = year_date
        birth_day = str(birth_date.__sub__(today)).split(" ")[0]
    return birth_day


def get_ciba():
    cookies = {
        'sajssdk_2015_cross_new_user': '1',
        '__utma': '183787513.1581383011.1688745359.1688745359.1688745359.1',
        '__utmc': '183787513',
        '__utmz': '183787513.1688745359.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '183787513.1.10.1688745359',
        'csrftoken': '0138c003ccb7b7aa43c6e5276bfa7222',
        '_ga': 'GA1.2.1581383011.1688745359',
        '_gat': '1',
        'auth_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI0NDU3OTM3LCJleHAiOjE2ODk2MDk2ODksImV4cF92MiI6MTY4OTYwOTY4OSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJRcV9iNzFlZDc4MmJjOGFlNGRlIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiJkNWVkMzdiMDFjZGUxMWVlYTNkOWUyZWFkMDc3YWU0MyJ9.B9_2ZvZFWjoL1nrBwKQRbAa8czRWqBHOroJsNtTX4tU',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22drussp%22%2C%22%24device_id%22%3A%22189311135361159-08d6e2b1a0dc69-26031d51-1327104-18931113537e1c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%7D%2C%22first_id%22%3A%22189311135361159-08d6e2b1a0dc69-26031d51-1327104-18931113537e1c%22%7D',
    }

    headers = {
        'authority': 'apiv3.shanbay.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'sajssdk_2015_cross_new_user=1; __utma=183787513.1581383011.1688745359.1688745359.1688745359.1; __utmc=183787513; __utmz=183787513.1688745359.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=183787513.1.10.1688745359; csrftoken=0138c003ccb7b7aa43c6e5276bfa7222; _ga=GA1.2.1581383011.1688745359; _gat=1; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI0NDU3OTM3LCJleHAiOjE2ODk2MDk2ODksImV4cF92MiI6MTY4OTYwOTY4OSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJRcV9iNzFlZDc4MmJjOGFlNGRlIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiJkNWVkMzdiMDFjZGUxMWVlYTNkOWUyZWFkMDc3YWU0MyJ9.B9_2ZvZFWjoL1nrBwKQRbAa8czRWqBHOroJsNtTX4tU; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22drussp%22%2C%22%24device_id%22%3A%22189311135361159-08d6e2b1a0dc69-26031d51-1327104-18931113537e1c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%7D%2C%22first_id%22%3A%22189311135361159-08d6e2b1a0dc69-26031d51-1327104-18931113537e1c%22%7D',
        'origin': 'https://web.shanbay.com',
        'pragma': 'no-cache',
        'referer': 'https://web.shanbay.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-csrftoken': '0138c003ccb7b7aa43c6e5276bfa7222',
        'x-referrer-app': 'client/web',
    }

    response = get('https://apiv3.shanbay.com/weapps/dailyquote/quote/', cookies=cookies, headers=headers)
    data = response.json()
    content = data['content']
    translation = data['translation']
    return content, translation


def lucky():
    with open('config.txt', encoding='utf-8') as f:
        config = eval(f.read())
        # print(config)
        API = config['weather_key']
    url = 'https://apis.tianapi.com/star/index?key={}&astro=libra'.format(API)
    # print(url)
    headers = {'Content-Length': '59',
               'Content-Type': ' application/x-www-form-urlencoded'}
    data = get(url).json()['result']['list']
    return [data[0]['content'], data[3]['content'], data[4]['content'],
            data[5]['content'], data[6]['content'], data[8]['content']]


def health():
    with open('config.txt', encoding='utf-8') as f:
        config = eval(f.read())
        # print(config)
        API = config['weather_key']
    url = 'https://apis.tianapi.com/healthskill/index?key={}'.format(API)
    # print(url)
    headers = {'Content-Length': '59',
               'Content-Type': ' application/x-www-form-urlencoded'}
    data = get(url).json()
    # print(data)
    num = int(random.random() * 10)
    # print(num)
    data = data["result"]["list"][num]['content']
    return data


def morning():
    with open('config.txt', encoding='utf-8') as f:
        config = eval(f.read())
        # print(config)
        API = config['weather_key']
    url = 'https://apis.tianapi.com/zaoan/index?key={}'.format(API)
    # print(url)
    headers = {'Content-Length': '59',
               'Content-Type': ' application/x-www-form-urlencoded'}
    data = get(url).json()['result']['content']
    return data


def send_message(to_user, access_token, greet, health, total, luck, health_index, color, num, total_index, region_name, weather,
                 realTemp, maxTemp, minTemp, wind, weather_tips, note_ch, note_en):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    week = week_list[today.isoweekday() % 7]
    # 获取在一起的日子的日期格式
    love_year = int(config["love_date"].split("-")[0])
    love_month = int(config["love_date"].split("-")[1])
    love_day = int(config["love_date"].split("-")[2])
    love_date = date(love_year, love_month, love_day)
    # 获取在一起的日期差
    love_days = str(today.__sub__(love_date)).split(" ")[0]
    # 获取所有生日数据
    birthdays = {}
    for k, v in config.items():
        if k[0:5] == "birth":
            birthdays[k] = v
    data = {
        "touser": to_user,
        "template_id": config["template_id"],
        "url": "http://weixin.qq.com/download",
        "topcolor": "#FF0000",
        "data": {
            "date": {
                "value": "{} {}".format(today, week),
                "color": get_color()
            },
            "region": {
                "value": region_name,
                "color": get_color()
            },
            "health": {
                "value": health,
                "color": get_color()
            },
            "total": {
                "value": total,
                "color": get_color()
            },
            "luck": {
                "value": luck,
                "color": get_color()
            },
            "health_": {
                "value": health_index,
                "color": get_color()
            },
            "total_": {
                "value": total_index,
                "color": get_color()
            },
            "tips": {
                "value": weather_tips,
                "color": get_color()
            },
            "greet": {
                "value": greet,
                "color": get_color()
            },
            "weather": {
                "value": weather,
                "color": get_color()
            },
            "temp": {
                "value": realTemp,
                "color": get_color()
            },
            "max_temperature": {
                "value": maxTemp,
                "color": get_color()
            },
            "min_temperature": {
                "value": minTemp,
                "color": get_color()
            },
            "wind_dir": {
                "value": wind,
                "color": get_color()
            },
            "love_day": {
                "value": love_days,
                "color": get_color()
            },
            "note_en": {
                "value": note_en,
                "color": get_color()
            },
            "note_ch": {
                "value": note_ch,
                "color": get_color()
            }
        }
    }
    for key, value in birthdays.items():
        # 获取距离下次生日的时间
        birth_day = get_birthday(value["birthday"], year, today)
        if birth_day == 0:
            birthday_data = "今天{}生日哦，祝{}生日快乐！".format(value["name"], value["name"])
        else:
            birthday_data = "距离{}的生日还有{}天".format(value["name"], birth_day)
        # 将生日数据插入data
        data["data"][key] = {"value": birthday_data, "color": get_color()}
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = post(url, headers=headers, json=data).json()
    if response["errcode"] == 40037:
        print("推送消息失败，请检查模板id是否正确")
    elif response["errcode"] == 40036:
        print("推送消息失败，请检查模板id是否为空")
    elif response["errcode"] == 40003:
        print("推送消息失败，请检查微信号是否正确")
    elif response["errcode"] == 0:
        print("推送消息成功")
    else:
        print(response)


if __name__ == "__main__":
    try:
        with open("config.txt", encoding="utf-8") as f:
            config = eval(f.read())
    except FileNotFoundError:
        print("推送消息失败，请检查config.txt文件是否与程序位于同一路径")
        os.system("pause")
        sys.exit(1)
    except SyntaxError:
        print("推送消息失败，请检查配置文件格式是否正确")
        os.system("pause")
        sys.exit(1)

    # 获取accessToken
    accessToken = get_access_token()
    # 接收的用户
    users = config["user"]
    # 传入地区获取天气信息
    region = config["region"]
    weather, realTemp, maxTemp, minTemp, wind, weather_tips = get_weather()
    health = health()
    greet = morning()
    luckys = lucky()
    total = luckys[0]
    luck = luckys[1]
    health_ = luckys[2]
    color = luckys[3]
    num = luckys[4]
    total_ = luckys[5]
    note_ch = config["note_ch"]
    note_en = config["note_en"]
    if note_ch == "" and note_en == "":
        # 获取扇贝单词每日一句
        note_ch, note_en = get_ciba()
        # print(note_ch, note_en)
    # 公众号推送消息
    for user in users:
        send_message(user, accessToken, greet, health, total, luck, health_, color, num, total_, region, weather,
                     realTemp, maxTemp, minTemp, wind, weather_tips, note_en, note_ch)
    os.system("pause")
