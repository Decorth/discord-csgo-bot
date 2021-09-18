import discord
import random
from Classes import Case
from Classes import Smoke
from Classes import RequestHandler

COMMAND_SYMBOL = "$"
DISCORD_TOKEN = "Nzk3MzEzOTkxNjc5ODAzNDQz.X_kqhA.v_VUZ03PVJGa1goRDb9JPdYL19I"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(COMMAND_SYMBOL) == False:
        return

    handler = RequestHandler.RequestHandler(message.content)

    # This checks if the request is syntactically and semantically valid
    if (handler.inputValidation() == False):
        await message.channel.send(handler.getErrorMessage())

    # This handles case opening requests
    elif handler.getUserCommand() == COMMAND_SYMBOL + 'case':
        caseopener = Case.Case()
        await message.channel.send(caseopener.openCase(handler.buildRequest(1)))

    # This handles smoke requests
    elif handler.getUserCommand() == COMMAND_SYMBOL +  'smoke':
        smoke = Smoke.Smoke(handler.buildRequestWithEnd(1, 2), handler.buildRequest(2))
        await message.channel.send(files=smoke.getSmoke())

client.run(DISCORD_TOKEN)
