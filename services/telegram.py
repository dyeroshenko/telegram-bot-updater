import requests

def send_telegram_message(message):
    bot_token = "###YOUR BOT TOKEN###"
    chat_id = "###YOUR CHAT ID###"
    bot_message = message
    
    send_to_me = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_to_me)

