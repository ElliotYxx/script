import json
import requests
import config
import logging

headers = {"Content-Type": "application/x-www-form-urlencoded"}


# 获取汇率
def get_exchangerate(currFrom: str = 'AUD', currTo: str = 'CNY'):
    params = {'from': currFrom, 'to': currTo, 'version': '2', 'key': config.EXCHANGE_RATE_API_KEY}
    response = requests.post("http://op.juhe.cn/onebox/exchange/currency",
                             data=params, headers=headers)

    # 如果获取失败
    if response.status_code != 200:
        logging.info("request error")
        return 0
    return response.json()['result']


# 发送
def send_email(msg: str):
    if config.PUSH_TOKEN is None:
        return
    title = '汇率价格通知'  # 改成你要的标题内容
    content = msg  # 改成你要的正文内容
    url = 'http://www.pushplus.plus/send'
    r = requests.get(url, params={'token': config.PUSH_TOKEN,
                                  'title': title,
                                  'content': content})
    logging.info(f'通知推送结果：{r.status_code, r.text}')


def main():
    data = get_exchangerate()
    if len(data) == 0:
        return
    exchange = float(data[0]['exchange'])
    if exchange < config.AUD_EXCHANGE_ALERT_VALUE:
        send_email(f'AUD -> CNY 汇率: {exchange}')


if __name__ == '__main__':
    main()
