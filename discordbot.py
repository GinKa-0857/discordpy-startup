import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ハロー。観測儀ラプラス、起動しました。')

@client.event
async def on_member_join(member):
    message.channel.send(f'{message.author.display_name}'s join has been confirmed.
Welcome to the Discord Crisis Countermeasures Organization.

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if  'Laplace' in message.content:
        await message.channel.send(f'Hello,{message.author.display_name}.\nWhat do you need?')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
