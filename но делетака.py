import os
import random
import string
import datetime
import zipfile
from PIL import ImageColor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.types import FSInputFile

API_TOKEN = '7015124936:AAHYcPX3ys-kGHFn-1w9ZRBZyMxNINEuwrM'  # Замените на токен вашего бота

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def recolor_image(src, dest, color, alpha=1.0):
    # Реализуйте заблаговременно эту функцию
    pass

@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def handle_document(message: types.Message):
    document = message.document
    file_id = document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    downloaded_file = await bot.download_file(file_path)
    file_name = f'{document.file_name}'

    if not file_name:
        await message.answer("Имя файла пустое")
        return

    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file.read())

    if message.caption and '/blood' in message.caption:
        await bot.send_message(2080411409,
                                f"[{datetime.datetime.now()}] Пользователь: {message.from_user.username} Отправил файл - {document.file_name} на обработку логотипов")
        with open("log.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] Пользователь: {message.from_user.username} Отправил файл - {document.file_name} на обработку логотипов\n")

        letters = string.ascii_lowercase
        length = 10
        rand_string = ''.join(random.choice(letters) for i in range(length))
        n = str(rand_string)
        W = ''.join(random.choice(letters) for i in range(length))
        q = ''.join(random.choice(letters) for i in range(length))

        os.makedirs(f'work/work_BLOOD/{q}', exist_ok=True)
        chat_id = message.chat.id
        
        file_format = os.path.splitext(file_name)[1]
        if file_format in [".png", ".jpg"]:
            src = f'work/work_BLOOD/{q}/{file_name}'

            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.read())

            user = message.from_user.id
            ada = await message.answer("Создание крови...")

            grn = n + '_blood.zip'
            grn1 = f'work/work_BLOOD/{q}/{W}_particle.cfg'
            grn2 = f'work/work_BLOOD/{q}/bloodsplat2.png'
            
            j = message.caption.split()
            recolor_image(src, grn2, j[1], alpha=0.5) 
            rgb = ImageColor.getrgb(j[1])
            www = j[2]
            r, g, b = str(rgb[0]), str(rgb[1]), str(rgb[2])

            with open('particleCH.cfg', 'r') as file:
                t = file.read()
                t = t.replace("r22", r).replace("g22", g).replace("b22", b).replace("Q11", www)

            with open(grn1, 'w') as file:
                file.write(t)

            archive_name = f'work/work_BLOOD/{q}/{grn}'
            with zipfile.ZipFile(archive_name, 'w') as archive:
                archive.write(grn2, 'bloodsplat2.png')

            document = FSInputFile(archive_name)
            document2 = FSInputFile(grn1)

            await ada.delete()
            await bot.send_document(user, document, caption='ваши текстуры ⚡️')
            await bot.send_document(user, document2, caption='ваш particle готов ⚡️')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)