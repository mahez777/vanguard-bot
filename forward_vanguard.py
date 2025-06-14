from telethon.sync import TelegramClient, events
import asyncio

api_id = 29045250
api_hash = 'adf9a9e453457738a73fa8065d902fab'
nomor_hp = '+6287882313667'

sumber_channel = 'Vanguard_production'

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
    '@jasebmahez',
    '@Vanguard_production',
    '@jasebvanguard2',
    '@jasebvanguardsallery'
]

client = TelegramClient('session_forward', api_id, api_hash)

@client.on(events.NewMessage(chats=sumber_channel))
async def handler(event):
    pesan = event.raw_text
    print(f"\n🚀 Pesan baru dari @{sumber_channel}:\n{pesan}\n")

    for target in targets:
        try:
            await client.send_message(target, pesan)
            print(f"✅ Terkirim ke {target}")
        except Exception as e:
            print(f"❌ Gagal ke {target} | {e}")
        await asyncio.sleep(1)  # Delay ringan antar target

    print("⏳ Menunggu 2 menit sebelum siap terima pesan baru...")
    await asyncio.sleep(120)

with client:
    print(f"📡 Bot aktif. Menunggu pesan dari @{sumber_channel}...\n")
    client.run_until_disconnected()
