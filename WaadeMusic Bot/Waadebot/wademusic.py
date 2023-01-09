from pathlib import Path

import discord
from discord.ext import commands

class WadeMusic(commands.bot):

    def __init__(self):
        self._cogs= [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(command_prefix=self.prefix, case_insensitive=True)

    def setup(self):
        print("Iniciando a instalação ...")

        for cog in self._cogs:
            self.load_extension(f"bot.cogs.{cog}")
            print(f"Loaded `{cog}` cog.")

        print("Setup complete.")

    def run(self):
        self.setup()

        with open("data/token.0", "r", encoding="utf-8") as f:
            TOKEN = f.read()

        print ("Running bot ...")
        super().run(TOKEN, reconnect=True)

    async def shutdown(self):
        print("Fechando a conexão do discord ...")
        await super(). close()

    async def on_connection(self):
        print("Fechado e Interrompido com o teclado..")
        await self.shutdown()

    async def on_connect(self):
        print(f"Conectado ao Discord (latency: {self.latency*1000:,.0f} ms).")

    async def on_resumed(self):
        print("Waade de volta .")
    
    async def on_disconnect(self):
        print("Waade acabou de sair u.u,")

    async def on_error(self, err, *args, **kwargs):
        raise

    async def on_ready(self,ctx, exc):
        raise getattr(exc,"original",exc)

    async def on_ready(self):
        self.client_id=(await self.application_info()).id
        print("Waade ao seu comando !")

    async def on_message(self,msg):
        if not msg.author.bot:
            await self.process_commands(msg)