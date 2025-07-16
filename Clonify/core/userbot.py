from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="PROAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = None
        if config.STRING2:
            self.two = Client(
                name="PROAss2",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING2),
                no_updates=True,
            )

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        # Start Assistant 1
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("ProBotGc")
                await self.one.join_chat("ProBotts")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant 1 Started")
            except:
                LOGGER(__name__).error("Assistant 1 failed to send log message.")
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant 1 Started as {self.one.name}")

        # Start Assistant 2
        if self.two:
            await self.two.start()
            try:
                await self.two.join_chat("ProBotGc")
                await self.two.join_chat("ProBotts")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant 2 Started")
            except:
                LOGGER(__name__).error("Assistant 2 failed to send log message.")
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant 2 Started as {self.two.name}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass
        try:
            if config.STRING2 and self.two:
                await self.two.stop()
        except:
            pass
