import discord
from discord.ext import commands
import asyncio
import random

# MASUKKAN TOKEN BARU KAMU DI SINI (Setelah ganti password)
TOKEN = "OTk2MzQyOTMyNDM1MTIwMTU5.GbYdze.gBCpqDsQ20ptoNlp5cdmaI91cWimEdsZkFHi7Q" 
# MASUKKAN ID CHANNEL TEMPAT OWO (Klik kanan channel > Copy ID)
CHANNEL_ID = 1073820520056889395 

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    print("Script Auto Hunt & Battle dimulai...")
    bot.loop.create_task(owo_loop())

async def owo_loop():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)

    if channel is None:
        print("Error: ID Channel tidak ditemukan!")
        return

    while True:
        try:
            # Command Hunt
            print("Mengirim: owo hunt")
            await channel.send("owoh")
            await asyncio.sleep(random.uniform(2, 5)) # Jeda kecil antar command

            # Command Battle
            print("Mengirim: owo battle")
            await channel.send("owob")

            # Jeda waktu tunggu cooldown OwO (biasanya 15-20 detik)
            # Kita gunakan random agar tidak terbaca bot oleh sistem anti-cheat
            wait_time = random.randint(16, 25)
            print(f"Menunggu {wait_time} detik untuk sesi berikutnya...\n")
            await asyncio.sleep(wait_time)

        except Exception as e:
            print(f"Terjadi error: {e}")
            await asyncio.sleep(60) # Tunggu 1 menit jika ada error

bot.run(TOKEN)
