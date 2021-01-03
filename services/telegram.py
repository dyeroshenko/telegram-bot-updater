import requests

def send_telegram_message(message):
    bot_token = "###YOUR BOT TOKEN###"
    chat_id = "###YOUR CHAT ID###"
    send = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    requests.get(send)

