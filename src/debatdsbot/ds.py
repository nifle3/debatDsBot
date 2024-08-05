from discord import Client, Message


class MyClient(Client):
    """
        Implement discord bot
    """

    async def on_ready(self) -> None:
        print(f'logged on as {self.user}')


    async def on_message(self, message: Message) -> None:
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('world')
        else:
            await message.channel.send('Uknown command')

        print(f'Message from {message.author}: {message}')
