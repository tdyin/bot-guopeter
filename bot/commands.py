from khl import Message, Bot, MessageTypes
from khl.card import CardMessage, Card, Module, Element

from revChatGPT.V3 import Chatbot


def register_cmds(bot: Bot, gpt: Chatbot):
    @bot.command(name='hi')
    async def greet(msg: Message):
        try:
            response = gpt.ask(prompt="你好", convo_id=msg.author.username)
        except Exception as e:
            print(e)
            response = e
        await msg.reply(response)

    @bot.command(name='chat')
    async def chat(msg: Message, content: str):
        try:
            response = gpt.ask(prompt=content, convo_id=msg.author.username)
        except Exception as e:
            print(e)
            response = e
        await msg.reply(response)
