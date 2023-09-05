import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def Merhaba(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def list(ctx):
    await ctx.send(f's1 - blackbay31\ns2 - Watrex\ns5 - 5747\ns6 - Burhan\ns7 - defne\ns8 - playtapus\ns9 - Vehbiefendi')
@bot.command()
async def s1(ctx):
    await ctx.send(f'Sonuc_Yok_Kayit Yok')

@bot.command()
async def s2(ctx):
    await ctx.send(f'Sonuc_Yok_Kayit Yok')


@bot.command()
async def s4(ctx):
    await ctx.send(f'İslemeleri_Tamamlandi')

@bot.command()
async def s5(ctx):
    await ctx.send(f'İslem_Yapiliyor')


@bot.command()
async def s6(ctx):
    await ctx.send(f'İslem_Yapilmadi')

@bot.command()
async def s7(ctx):
    await ctx.send(f'İslem_Yapilmadi')

@bot.command()
async def s8(ctx):
    await ctx.send(f'İslem_Yapilmadi')

@bot.command()
async def s9(ctx):
    await ctx.send(f'İslem_Yapilmadi')    

@bot.command()
async def kayit_vehebiefendi(ctx):
    await ctx.send(f'İletildi')
    print("vehebiefendi")

@bot.command()
async def kayit_playtapus(ctx):
    await ctx.send(f'İletildi')
    print("playtapus")

@bot.command()
async def kayit_karasosisiyt(ctx):
    await ctx.send(f'İletildi')
    print("karasosisiyt")


@bot.command()
async def kayit_huseyin(ctx):
    await ctx.send(f'İletildi')
    print("hüseyin")

@bot.command()
async def kayit_huseyun(ctx):
    await ctx.send(f'İletildi')
    print("huseyun")

@bot.command()
async def kayit_blackbay(ctx):
    await ctx.send(f'İletildi')
    print("blackbay")

@bot.command()
async def kayit_ariyan(ctx):
    await ctx.send(f'İletildi')
    print("ariyan")

@bot.command()
async def kayit_alperor(ctx):
    await ctx.send(f'İletildi')
    print("alperor")

async def kayit_orbay(ctx):
    await ctx.send(f'İletildi')
    print("orbay")

@bot.command()
async def kayit_defne(ctx):
    await ctx.send(f'İletildi')
    print("defne")

@bot.command()
async def kayit_burhan(ctx):
    await ctx.send(f'İletildi')
    print("burhan")

@bot.command()
async def kayit_5747(ctx):
    await ctx.send(f'İletildi')
    print("sacma_kullanici")

@bot.command()
async def kayit_ahmet(ctx):
    await ctx.send(f'İletildi')
    print("ahmet")



@bot.command()
async def msg_kayit(ctx):
    await ctx.send(f'@vehbiefendi @playtapus MagMAmen..1234,,#5747 @karasosisiyt @huseyun @hüseyin @blackbay isminiz/adiniz lazim')

@bot.command()
async def msg_wp(ctx):
    await ctx.send(f'@wartex @orbay @defne @burhan kursununzun whatsapp gurubunun adi ve kendi isminiz/adiniz lazim')


@bot.command()
async def ctdt(ctx):
    await ctx.send(f'Kayitlar_Tamamlandi')
    


@bot.command()
async def stop(ctx):
    print("stop")
    await ctx.send(f"admin_local_host_stop_services")
    await ctx.send(f"Bot Ve Sistemler Kapaniyor İyi Geceler Görüşrüz")
    exit()

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("TOKEN")
