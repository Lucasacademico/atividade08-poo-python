from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def acessar_pagina(bot, url):
    print("Iniciando a automação do formulário de produto.")
    bot.browse(url)
    bot.wait(1000)

def iniciar_bot():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    return bot

def main():
    # Inicialização do Maestro
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Inicializa o bot
    bot = iniciar_bot()

    # Acessa a página
    acessar_pagina(bot, r'http://127.0.0.1:5000')


def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()