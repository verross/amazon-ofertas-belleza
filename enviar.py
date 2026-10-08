import requests
import json
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url_afiliado = "https://www.amazon.es/dp/B0FDVJ4BBK/?tag=verross-21"

boton = {
    "inline_keyboard": [
        [
            {
                "text": "🛒 Comprar en Amazon",
                "url": url_afiliado
            }
        ]
    ]
}

mensaje = """
🎁 ¡Oferta Amazon! 🎁

medicube Facial Cleanser Kojic Acid Turmeric Whip Cleanser

Antes: 14,5€
🔥 AHORA: 9,6€ (34% descuento)
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensaje,
        "reply_markup": json.dumps(boton)
    }
)
