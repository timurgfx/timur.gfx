from telethon.sync import TelegramClient
from time import sleep
import requests

# ======= SOZLAMALAR =======
api_id = 24596818           # <-- o'zingizning API ID
api_hash = '2104ee72b40178bd6e6889bc8c3a5ff9'     # <-- o'zingizning API HASH
target_username = '@brouniverse'  # <-- kuzatilayotgan username

bot_token = '7966482767:AAFZzQ2W5weqj1zwYh3cEfgi7oVknCAkgA8'   # <-- @BotFather dan olingan token
chat_id = 7298807378       # <-- o'zingizning Telegram ID'ingiz
# ==========================

client = TelegramClient('online_session', api_id, api_hash)

def send_to_bot(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)

async def main():
    print(f"{target_username} kuzatilyapti...")
    old_status = None
    while True:
        try:
            user = await client.get_entity(target_username)
            current_status = user.status

            if str(current_status) != str(old_status):
                if 'UserStatusOnline' in str(current_status):
                    print(f"📢 {target_username} hozir ONLINE!")
                    send_to_bot(f"📢 {target_username} hozir ONLINE!")
                else:
                    print(f"⏳ {target_username} hozir OFFLINE.")
                    send_to_bot(f"⏳ {target_username} hozir OFFLINE.")
                old_status = current_status

        except Exception as e:
            print("Xatolik:", e)

        await sleep(10)

with client:
    client.loop.run_until_complete(main())
