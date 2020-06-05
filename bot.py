import time
import json
import requests

Token = "<your-bot-token"
URL = "https://api.telegram.org/bot{}/".format(Token)

def get_url(url):
	response = requests.get(url)
	content = response.content.decode("utf8")
	return content


def get_json_from_url(url):
	content = get_url(url)
	js = json.loads(content)
	return js


def get_updates(offset = None):
	url = URL + "getUpdates"
	if offset:
		url += "?offset={}".format(offset)
	js = get_json_from_url(url)
	return js


def get_last_update_id(updates):
	update_ids = []
	for update in updates["result"]:
		update_ids.append(int(update["update_id"]))
	return max(update_ids)

 #int update = 0;
 #for(int i =0; i<len(updates["results"]); i++)
 #update_ids += update["results"]update[i]
	

def get_last_chat_id_and_text(updates):
	num_updates = len(updates["result"])
	last_update = num_updates - 1
	text = updates["result"][last_update]["message"]["text"]
	chat_id = updates["result"][last_update]["message"]["chat"]["id"]
	print(text)
	print(chat_id)
	return (text,chat_id)


def echo_all(updates):
	for update in updates["result"]:
			text = update["message"]["text"]
			chat = update["message"]["chat"]["id"]
			send_message(text,chat)


def send_message(text,chat_id):
	url = URL + "sendMessage?text={}&chat_id={}".format(text,chat_id)
	get_url(url)

# text,chat = get_last_chat_id_and_text(get_updates())
# send_message(text, chat)

def main():
	last_update_id = None
	while True:
		updates = get_updates(last_update_id)
		if len(updates["result"]) > 0:
			last_update_id = get_last_update_id(updates) + 1
			echo_all(updates)
			print("getting updates")
		time.sleep(0.5)


if __name__=='__main__':
	main()
