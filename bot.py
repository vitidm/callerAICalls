from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.channels import GetFullChannelRequest

apiKey = "PeOYzvwJU6rhfLhuNDxIVkjhu"
apikeySecret = "pert2FTGRSI5ojCdmHWq3lLF50JVin4jCTjKqcmeEB9UwT1r3Z"

accessToken = "1481599432315613185-QQO0oGLptYYpch50fWpqFekCw5jIs1"
accessTokenSecret = "OhMSodujsMRc8AMFQvHMGG2Aq26XtcEvTJ8QLEg7AfuvM"

print("Authentication successfully")

google_calendar = "https://calendar.google.com/calendar/u/0?cid=bWFzdGVyY2FsbHNvZmZpY2lhbEBnbWFpbC5jb20"
hastag = "#shitcoin #memecoin #cryptogem #bscgems #bscgem #fairlaunch #100xCoin #100xgem #ToTheMoon"

WORDS_FAIR_LAUNCH = ['OUR FAIR LAUNCH', "OUR STEALTH LAUNCH", "OUR GROUP",
                        "OUR LAUNCH", "OUR PROJECT", "OUR STEALTH", "OUR LAUNCH","OUR NEXT PROJECT", "OUR PRIVATE SALE", "OUR PRESALE", "OUR GEM", 
                            "OUR NEXT PLAY", "OUR FIRST", "OUR NEW LAUNCH", "OUR FIRST DEGEN COIN", "OUR BIG LAUNCH", 
                                "I'M WORKING", "IN FEW DAYS", "I HAVE WORKED", "I'M GOING TO LAUNCH", "WE ARE DOING", "WE ARE GOING TO LAUNCH", 
                                    "MY PROJECT", "WE HAVE WORKED", "MY NEXT PROJECT", "WE ARE PREPARING", "NEXT PLAY",
                                        "MY NEXT FAIR LAUNCH", "TOMORROW", "THIS WEEK", "UPCOMING LAUNCH", "LAUNCHING SOON",
                                         "FAIRLAUNCH", "BSC FAIRLAUNCH", "LAUNCHING TODAY", "FAIR LAUNCHING", "STEALTH LAUNCH", "LAUNCHING ANY MOMENT",
                                            "LAUNCH ANY TIME", "LAUNCH ANY MINUTE", "SLOWER BUYERS WAIT FOR A DIP", "SLOW BUYERS", "SLOWER BUYERS", "SLOWER BUYERS WAIT FOR A DIP",
                                                "OUR FIRST LAUNCH", "LAUNCHING THIS", "LAUNCHING ON", "DEV SHOULD BE SAFE", "WE ARE ALMOST READY", "WE ARE READY", "MINS LEFT", "LAUNCH ON",
                                                    "TG LINK INVITE", "MINUTES FROM NOW", "WILL LAUNCH ANY MINUTE", "ANY MINUTE FROM NOW", "TG INVITE LINK", "PYTHAGORAS PROJECT", "WILL CREATE TG"
                                                        "TG SHORTLY", "IS THE TOKEN NAME", "MAKE THE TG NOW", "PUBLIC TG"]

WORDS_DEVS_PROJECT = ["DEV CALL GROUP", "CALL GROUP"]

WORDS_EXCLUDED = ["POOCOIN", "WHITELIST", "WL", "GIVEAWAY", "SPOTS", "PRESALE", "DEXTOOLS", "0X", "LAUNCHED", "JUST", "AMA", "STEALTH LAUNCHED"]

print("Starting...")

# Telegram

APP_ID = 18838067
API_HASH = "649dcacf3c66e15b07456d5e44c82788"
FROM_ = ["https://t.me/EZMoneyCalls", "https://t.me/brenthewolfcalls", "https://t.me/lowtaxethx", "https://t.me/mad_apes_call", "https://t.me/thorshammergems", "https://t.me/Caesars_Calls", "https://t.me/dr_crypto_channel", "https://t.me/InApeWeTrust", "https://t.me/PowsGemCalls", "https://t.me/luffysgemscalls", "https://t.me/VirusCalls", "https://t.me/TWOSICCsPICKS", "https://t.me/maythouscalls", "https://t.me/goobygambles", "https://t.me/DobbysGems", "https://t.me/Kingdom_X100_CALLS" ,"https://t.me/yourowntest"]
TO_ = ["https://t.me/CAIcalls"]

FROM = [str(i) if 'https' in i else int(i) for i in FROM_]
TO = [str(i) for i in TO_]

try:
    BotzHubUser = TelegramClient('testBot', APP_ID, API_HASH)
    BotzHubUser.start()
    print("Connected succesfully")

except Exception as ap:

    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(chats=FROM))

async def sender_bH(event):
    
    channel_full_info  = await BotzHubUser(GetFullChannelRequest(channel=event.chat.id))
    channel_extra_info = await BotzHubUser.get_entity(event.chat.id)

    participants_count = str(channel_full_info.full_chat.participants_count)
    username = channel_extra_info.username
    group_link = "t.me/"+ username
    for i in TO:

        title_fromchat = event.chat.title
        
        try:

            if ("DEXTOOLS" not in event.message.message.upper()) and ("POOCOIN" not in event.message.message.upper()) and ("WHITELIST" not in event.message.message.upper()) and ("WL" not in event.message.message.upper()) and ("GIVEAWAY" not in event.message.message.upper()) and ("SPOTS" not in event.message.message.upper()) and ("PRESALE" not in event.message.message.upper()) and ("LAUNCHED" not in event.message.message.upper()) and ("JUST" not in event.message.message.upper()) and ("AMA" not in event.message.message.upper()) and ("0X" not in event.message.message.upper()) and ("STEALTH LAUNCHED" not in event.message.message.upper()) and ("DYOR" in event.message.message) and any(word in event.message.message.upper() for word in WORDS_FAIR_LAUNCH):

                completed_message = f"⚠️**TYPE: DYOR, NEXT LAUNCH                👥MEMBERS: {participants_count}**\n" + f"🗣__GROUP: {title_fromchat}      🔗LINK: {group_link}__\n" + "----------------------\n" + event.message.message

                await BotzHubUser.send_message(
                    i,
                    completed_message
                )

                #result = api.update_status(status = f"⚠️TYPE: DYOR, NEXT LAUNCH\n" + f"FROM TG GROUP: {group_link}\n" +  f"MEMBERS: {participants_count}\n" + " \n" + f"🗣SEE THE MESSAGE: {message_id}\n" + " \n" + "Google Calendar:\n" + f"{google_calendar}\n"+ " \n" + f"{hastag}")

            
            elif ("DEXTOOLS" not in event.message.message.upper()) and ("POOCOIN" not in event.message.message.upper()) and ("WHITELIST" not in event.message.message.upper()) and ("WL" not in event.message.message.upper()) and ("GIVEAWAY" not in event.message.message.upper()) and ("SPOTS" not in event.message.message.upper()) and ("PRESALE" not in event.message.message.upper()) and ("LAUNCHED" not in event.message.message.upper()) and ("JUST" not in event.message.message.upper()) and ("AMA" not in event.message.message.upper()) and ("0X" not in event.message.message.upper()) and ("STEALTH LAUNCHED" not in event.message.message.upper()) and any(word in event.message.message.upper() for word in WORDS_FAIR_LAUNCH):

                completed_message = f"‼️**TYPE: NEXT LAUNCH                  👥MEMBERS: {participants_count}**\n" + f"🗣__GROUP: {title_fromchat}      🔗LINK: {group_link}__\n" + "----------------------\n" + event.message.message

                await BotzHubUser.send_message(
                    i,
                    completed_message
                )

                #result = api.update_status(status = f"‼️TYPE: DYOR, NEXT LAUNCH\n" + f"FROM TG GROUP: {group_link}\n" +  f"MEMBERS: {participants_count}\n" + " \n" + f"🗣SEE THE MESSAGE: {message_id}\n" + " \n" + "Google Calendar:\n" + f"{google_calendar}\n"+ " \n" + f"{hastag}")

            elif any(word in event.message.message.upper() for word in WORDS_DEVS_PROJECT):
                
                completed_message = f"‼️**TYPE: DEV GROUP                       👥MEMBERS: {participants_count}**\n" + f"🗣__GROUP: {title_fromchat}      🔗LINK: {group_link}__\n" + "----------------------\n" + event.message.message

                await BotzHubUser.send_message(
                    i,
                    completed_message
                )

            elif "DEXTOOLS" in event.message.message.upper() or "DEXSCREENER" in event.message.message.upper():
                completed_message = f"‼️**TYPE: CALL                      👥MEMBERS: {participants_count}**\n" + f"🗣__GROUP: {title_fromchat}      🔗LINK: {group_link}__\n" + "----------------------\n\n" + event.message.message

                await BotzHubUser.send_message(
                    i,
                    completed_message
                )
   

            else:
                
                print(group_link + '          *')
            
        except Exception as e:

            print(e)

print("Bot has started.")

BotzHubUser.run_until_disconnected()
