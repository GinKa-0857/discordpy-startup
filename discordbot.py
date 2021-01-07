import discord
import os
import traceback

bot = commands.Bot(command_prefix='l!')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


# 返信する非同期関数を定義
async def reply(message):
    reply = f' Hello {message.author.mention}' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

@client.event
# 発言時に実行されるイベントハンドラを定義
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行



client.run(token)
