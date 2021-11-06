from asyncio.windows_events import NULL
import discord
import random
from discord import message
import numpy as np
from discord.ext import commands
import requests
import re
from bs4 import BeautifulSoup
import array
import random

client = commands.Bot(command_prefix="!")

tkn = "--"

@client.event
async def on_ready():
    print("pronto")

@client.command()
async def ajuda(ctx):
    await ctx.send("digite !google (sua pesquisa)")

@client.command()
async def google(ctx, palavra_v: str):
    k=0
    links = [9999] * 100
    encoding = 'utf-8'
    palavra_v = str(input(""))
    palavra = palavra_v.replace(" ", "_")
    site= "--"
    site = site + palavra
    print(site)
    resposta = requests.get(site)

    content = resposta.content

    site = BeautifulSoup(content, 'html.parser')

    images = site.findAll('img')

    for image in images:
        links[k] = image['src']
        k +=1

    num = random.randint(0, k)

    if(links[num] == 9999):
        await ctx.send("nada encontrado")
    else:    
        await ctx.send(links[num])
        

client.run(tkn)