import requests
from telethon import TelegramClient, events

# Configurações do Telegram
API_ID = "SEU_API_ID"
API_HASH = "SEU_API_HASH"
BOT_TOKEN = "SEU_BOT_TOKEN"
ID_DO_GRUPO_DO_SINAL = -1001234567890  # Substituir pelo ID real

# Configuração da Blaze
BASE_URL_BLAZE = "https://blaze.com/api/"
TOKEN_BLAZE = "SEU_TOKEN_BLAZE"

# Inicializando o bot do Telegram
client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(chats=ID_DO_GRUPO_DO_SINAL))
async def handle_signal(event):
    mensagem = event.message.message.lower()

    if "sinal:" in mensagem:
        cor = "branco" if "branco" in mensagem else "vermelho" if "vermelho" in mensagem else "preto"
        print(f"Recebido sinal para apostar em {cor}")

        # Simulação de aposta na Blaze
        response = requests.post(BASE_URL_BLAZE + "bet", json={"color": cor, "amount": 10}, headers={"Authorization": f"Bearer {TOKEN_BLAZE}"})

        if response.status_code == 200:
            print(f"Aposta realizada com sucesso em {cor}")
        else:
            print("Erro ao realizar a aposta")

client.start()
client.run_until_disconnected()
