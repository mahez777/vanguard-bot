from telethon import TelegramClient
import asyncio
import sys
import time

api_id = 29045250
api_hash = 'adf9a9e453457738a73fa8065d902fab'
session_name = 'forward_vanguard'
client = TelegramClient(session_name, api_id, api_hash)

source_channel = 'Vanguard_production'

target_groups = [
    'JAKELPM', 'LPMJAZEL', 'lpm_cari_pacar_abang_rp', 'LPMWIDIELYS', 'FreelanceLpm',
    'LpmZura', 'freelancesewawhastapp', 'IrohaLpm', 'lpmzhen', 'LPMB0SS', 'MEHLPM',
    'IDFreelancers', 'LPMCHEY', 'LPMRUSHEEL', 'LPM_FREELANCEE', 'DAVIDOLPM', 'sewa_waa',
    'lapakcarikerjaan', 'PEJUANG_RUPIAH46', 'lpmrpps', 'agenjasonid', 'lpmcarikerjadanasiten',
    'LPM_FREELANCE2', 'sewawabadakmu', 'grup_pencari_uang', 'LPMRAWR', 'waappe24',
    'promoterpps', 'sewawadragon', 'lpmsalzoya', 'LpmNiveyie', 'jasebmahez'
]

async def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r⏳ Delay: {i} detik...")
        sys.stdout.flush()
        time.sleep(1)
    print("\r▶️ Lanjut kirim...\n")

async def forward_loop():
    await client.start()
    print("🔁 Bot mulai... Forward pesan setiap 1 menit (60 detik)\n")

    while True:
        try:
            message = await client.get_messages(source_channel, limit=1)
            if message and message[0]:
                msg = message[0]
                print(f"\n📨 Forwarding: {msg.text[:30]}...\n") if msg.text else print("📨 Forwarding: [Non-text Message]")

                for group in target_groups:
                    try:
                        await client.forward_messages(group, msg)
                        print(f"✅ Sukses ke @{group}")
                        await asyncio.sleep(1)
                    except Exception as e:
                        print(f"❌ Gagal ke @{group} | {str(e)}")
            else:
                print("⚠️ Tidak ada pesan ditemukan di channel.")

        except Exception as e:
            print(f"⚠️ Error utama: {str(e)}")

        await asyncio.to_thread(countdown, 60)

with client:
    client.loop.run_until_complete(forward_loop())
