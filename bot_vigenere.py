import telebot

TOKEN = "8545083111:AAHC4b47jRYOXYyk4IDq-tCOEsVG2puXuuE"
bot = telebot.TeleBot(TOKEN)

# Funzione per cifrare
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0

    for c in plaintext:
        if c.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            p = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += p
            key_index += 1
        else:
            ciphertext += c

    return ciphertext

# Funzione per decifrare
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_index = 0

    for c in ciphertext:
        if c.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            p = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            plaintext += p
            key_index += 1
        else:
            plaintext += c

    return plaintext


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
        "Puoi usare due formati:\n\n"
        "🔐 Per CIFRARE:\n"
        "TESTO=...\n"
        "CHIAVE=...\n\n"
        "🔓 Per DECIFRARE:\n"
        "CRITTO=...\n"
        "CHIAVE=...\n"
    )

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    text = message.text.strip().upper()

    try:
        parts = text.split("\n")
        
        # CIFRATURA
        if parts[0].startswith("TESTO=") and parts[1].startswith("CHIAVE="):
            plaintext = parts[0].replace("TESTO=", "").strip()
            key = parts[1].replace("CHIAVE=", "").strip()
            cipher = vigenere_encrypt(plaintext, key)
            bot.reply_to(message, "🔐 Testo cifrato:\n" + cipher)

        # DECIFRATURA
        elif parts[0].startswith("CRITTO=") and parts[1].startswith("CHIAVE="):
            ciphertext = parts[0].replace("CRITTO=", "").strip()
            key = parts[1].replace("CHIAVE=", "").strip()
            plain = vigenere_decrypt(ciphertext, key)
            bot.reply_to(message, "🔓 Testo decifrato:\n" + plain)

        else:
            bot.reply_to(message,
                "Formato non valido.\n\n"
                "👉 Per cifrare:\nTESTO=...\nCHIAVE=...\n\n"
                "👉 Per decifrare:\nCRITTO=...\nCHIAVE=...\n"
            )

    except:
        bot.reply_to(message,
            "Errore nel formato!\n"
            "Usa TESTO=... oppure CRITTO=... con CHIAVE=..."
        )


print("BOT AVVIATO (CIFRA + DECIFRA)…")
bot.infinity_polling()
