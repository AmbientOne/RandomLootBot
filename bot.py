# bot.py
import os
from random import randrange

import discord
from dotenv import load_dotenv
import csv

#replace this with your loot table, uses only CSV for now
loot_table = ''
def read_table(filename):
    loot_table = []
    itemNum = 1
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row[0] != '':
                dictionary = { 'ItemNumber': itemNum,
                    'Name': row[0],
                                'Description': row[1],
                                'Properties': row[7]
                                }
                loot_table.append(dictionary)
                itemNum+=1
    return loot_table

### Returns a string of what the item is
def print_item(my_item):

    item = "You have received the: " + my_item['Name']
    if my_item['Properties'] != '':
       item += "\nThis item has the following properties: " + my_item['Properties']

    if my_item['Description'] != '':
        item += "\nThe item has the following description: " + my_item['Description']


    return item




loot = read_table(loot_table)


randomItems = ['Sword', 'Shield', 'Blaster']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    ### Checks the item to see if its possible
    if "$random.item" in message.content.lower():
        randomItemNumber = randrange(980)
        my_item = next((item for item in loot if item['ItemNumber'] == randomItemNumber), None)

        await message.author.send(
            print_item(my_item) if my_item is not None else "That item does not exist! Pleas try again!")
client.run(TOKEN)