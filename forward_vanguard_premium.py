from telethon.sync import TelegramClient
import asyncio
import time
import sys

# === KONFIGURASI ===
api_id = 29045250
api_hash = 'adf9a9e453457738a73fa8065d902fab'
sumber_channel = 'Vanguard_production'
nomor_hp = '+6287882313667'

# === DAFTAR GRUP TARGET ===
targets = [
    '@JAKELPM',
    '@LPMJAZEL',
    '@lpm_cari_pacar_abang_rp',
    '@LPMWIDIELYS',
    '@FreelanceLpm',
    '@LpmZura',
    '@freelancesewawhastapp',
    '@IrohaLpm',
    '@lpmzhen',
    '@LPMB0SS',
    '@MEHLPM',
    '@IDFreelancers',
    '@LPMCHEY',
    '@LPMRUSHEEL',
    '@LPM_FREELANCEE',
    '@DAVIDOLPM',
    '@sewa_waa',
    '@lapakcarikerjaan',
    '@PEJUANG_RUPIAH46',
    '@lpmrpps',
    '@agenjasonid',
    '@lpmcarikerjadanasiten',
    '@LPM_FREELANCE2',
    '@sewawabadakmu',
    '@grup_pencari_uang',
    '@LPMRAWR',
    '@waappe24',
    '@promoterpps',
    '@sewawadragon',
    '@lpmsalzoya',
    '@LpmNiveyie',
    '@jasebmahez'
]

client = TelegramClient('session_loop', api_id, api_hash)

async def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r⏳ Delay: {i} detik...")
        sys.stdout.flush()
        await asyncio.sleep(1)
    print("\r✅ Delay selesai!                     ")

async def loop_forward():
    await client.start(phone=nomor_hp)
    last_msg_id = None

    while True:
        try:
            async for message in client.iter_messages(sumber_channel, limit=1):
                if message.id != last_msg_id:
                    print(f"\n📥 Forward pesan ID: {message.id}")
                    for i, target in enumerate(targets, start=1):
                        try:
                            await client.forward_messages(target, message.id, from_peer=sumber_channel)
                            print(f"✅ {i}. Forward ke {target}")
                        except Exception as e:
                            print(f"❌ {i}. Gagal ke {target} | {e}")
                        await asyncio.sleep(1)  # Delay antar grup
                    last_msg_id = message.id
                else:
                    print("⚠️ Belum ada pesan baru.")
                break

            print("\n⏱️ Tunggu 40 detik untuk cek ulang...")
            await countdown(40)

        except Exception as e:
            print(f"❗ Error utama: {e}")
            await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(loop_forward())
