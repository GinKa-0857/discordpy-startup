from discord.ext import commands
import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    CHANNEL_ID = 798522685042851850
    channel = client.get_channel(CHANNEL_ID)
    print('ハロー。観測儀ラプラス、起動しました。')
    await channel.send('Hello.\nConfiguration code updates have been confirmed.\nRestarting.')

@client.event
async def on_member_join(member):
    message.channel.send(f"{message.author.display_name}'s join has been confirmed.\nWelcome to the Discord Crisis Countermeasures Organization.")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.author.bot:
        return

    if  'Laplace' in message.content:
        await message.channel.send(f'Hello,{message.author.display_name}.\nWhat do you need?')

#オペレーター申請システム
@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.guild is None and ('Apply' in message.content or 'apply' in message.content):
        await message.author.send('Ok.\nYour operator application has been confirmed.\nPlease set up a code name in order to register it in the database.')

@commands.has_permissions(administrator=True)
    async def ban(self, ctx, user_id=None, reason=None):
        """Ban(管理者用)"""
        print(user_id)
        if user_id == None or user_id == ctx.author.id:
            await ctx.channel.send("BAN対象が正しくありません")
            return



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
