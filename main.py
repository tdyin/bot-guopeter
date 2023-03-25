import json
import logging

from khl import Bot
from revChatGPT.V3 import Chatbot

from bot.commands import register_cmds

logging.basicConfig(
    level='INFO', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

######################################################################

with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

gpt = Chatbot(**{
    "api_key": config['openai_key'],
})

bot = Bot(token=config['token'])

register_cmds(bot, gpt)

if __name__ == "__main__":
    bot.run()
