import logging
import tarfile
dayn = "7357565595"
ADMIN_ID = "6033522149"
ADMIN = "6033522149"
import lzma
from aiogram import Bot, Dispatcher, types
#from aiogram.contrib.middlewares.logging import LoggingMiddleware
import shutil
import os
from aiogram.types.web_app_info import WebAppInfo
import zipfile
from PIL import Image
import time
#from text import start, mapo, new_smoke, new_listva
from image_slicer import slice
import random
from random import *
from rarfile import RarFile
import numpy as np
from aiogram.utils.exceptions import BadRequest
import datetime
import string
import asyncio
from aiogram.dispatcher import FSMContext
#import bytesIO


#_io_bytesIo






def extract_zip(zip_file_path, destination_folder="rec"):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

# Перекрашиваем изображения (ускоренная версия)
def tint_image(input_path, output_path, color, alpha):
    img = Image.open(input_path).convert("RGBA")
    new_color = tuple(map(int, color.split(',')))
    
    # Перекрашиваем только непрозрачные пиксели
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            if pixel[3] > 0: # Проверка прозрачности
                img.putpixel((x, y), (*new_color, int(pixel[3] * alpha)))

    img.save(output_path)

# Перекрашиваем все PNG-файлы в папке
def recolor_folder(folder_path, color="255,0,0", alpha=0.4):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, filename)
            tint_image(input_path, output_path, color, alpha)

# Создаем ZIP-архив из папки (ускоренная версия)
def create_zip(folder_path, zip_file_name="output.zip"):
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zip_ref.write(file_path, arcname)










API_TOKEN = '7015124936:AAHYcPX3ys-kGHFn-1w9ZRBZyMxNINEuwrM' # Замените на свой API токен
proces = 2
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
#dp.middleware.setup(LoggingMiddleware())
def zip_folder(folder_path):
    # Имя ZIP архива будет таким же, как имя папки
    zip_filename = f"{folder_path}.zip"

    # Создаем ZIP архив
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zip_ref.write(file_path, arcname)

    print(f"Папка {folder_path} успешно заархивирована в {zip_filename}.")
    
    
    
    
    
    ''' олд дефаф 
def recolor_image(input_path, output_path, color):
    img = Image.open(input_path).convert("RGB")
    new_color = tuple(map(int, color.split(',')))
    recolored_img = Image.new("RGB", img.size, new_color)
    
    # Смешивание оригинального изображения с новым цветом
    img = Image.blend(img, recolored_img, alpha=0.3)
    img.save(output_path)
    
    '''
    
def recolor_imae(input_path, output_path, color, alpha):
    img = Image.open(input_path).convert("RGBA")
    new_color = tuple(map(int, color.split(',')))
    recolored_img = Image.new("RGBA", img.size)
    
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            if pixel[3] > 0:  
                recolored_img.putpixel((x, y), (*new_color, int(pixel[3] * alpha)))

    combined = Image.alpha_composite(img, recolored_img)
    combined.save(output_path)




def recolor_image(input_path, output_path, color):
    img = Image.open(input_path).convert("RGBA")  # Используем RGBA для прозрачности
    new_color = tuple(map(int, color.split(',')))
    recolored_img = Image.new("RGBA", img.size)
    
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            if pixel[3] > 0:  # Проверяем альфа-канал на непрозрачные пиксели
                recolored_img.putpixel((x, y), (*new_color, pixel[3]))  # Сохраняем альфа-значение

    # Смешивание оригинального изображения с новым цветом
    combined = Image.alpha_composite(img, recolored_img)
    combined.save(output_path)




@dp.message_handler(commands=['button'])
async def ebal(message: types.Message):
    if message.text.count(",") == 2:  # Проверяем наличие двух запятых
        rgbb = message.text.replace('/button ', '')
        welcome_message = await message.answer("Ожидайте файл✨")
        
        os.makedirs('button', exist_ok=True)
        
        file_name = [
            "brake.png", "shoot.png", "hud_chopper.png", "hud_circle.png",
            "punch.png", "hud_lockon.png", "hud_nitro.png", "sprint.png",
            "handbrake.png", "horn.png", "hud_bike.png", "hud_monstertruck.png",
            "accelerate.png", "cam-toggle.png"
        ]
        alpha = 0.5
        
        def recolor_image(input_path, output_path, color, alpha):
            img = Image.open(input_path).convert("RGBA")
            new_color = tuple(map(int, color.split(',')))
            recolored_img = Image.new("RGBA", img.size)
            for x in range(img.width):
                for y in range(img.height):
                    pixel = img.getpixel((x, y))
                    if pixel[3] > 0:
                        recolored_img.putpixel((x, y), (*new_color, int(pixel[3] * alpha)))
            combined = Image.alpha_composite(img, recolored_img)
            combined.save(output_path)

        color = rgbb  # Используем введенный цвет для перекрашивания
        for file in file_name:
            output_path = os.path.join('button', file)
            recolor_image(file, output_path, color, alpha)
            print(f"готово {file}")

        # Создание ZIP-архива
        zip_file_path = 'button.zip'
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            for file in file_name:
                zipf.write(os.path.join('button', file), file)

        await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
        await message.answer_document(types.InputFile("button.zip"), caption="держи свои кнопки⚡")
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
     #   await message.answer_document(types.InputFile("button.zip"), caption="sex")
          
    else:
        await message.answer("❓")
        await message.answer("Используйте /button и цвет в формате RGB\nПример: /button 255,0,0")
        user = message.from_user.id
        await bot.send_message(ADMIN_ID, f"Map\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user}")
        






        
        
        

    

async def slice_and_send_image(message: types.Message, image_path, output_prefix, num_slices):
    img = Image.open(image_path)
    width, height = img.size
    segment_width = width // 12
    segment_height = height // 12
    zip_name = 'map.zip'
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for i in range(12):
            for j in range(12):
                left = j * segment_width
                upper = i * segment_height
                right = left + segment_width
                lower = upper + segment_height
                segment = img.crop((left, upper, right, lower))
                number = i * 12 + j
                segment_name = f"{output_prefix}{number:02}.png"
                with zip_file.open(segment_name, 'w') as segment_file:
                    segment.save(segment_file, format="PNG")
    with open(zip_name, 'rb') as zip_file:
        await bot.send_document(message.chat.id, zip_file, caption='держи свою карту⚡️')
    os.remove(zip_name)
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def handle_document(message: types.Message):
    if message.caption == '/map':
        document = message.document
        file_id = document.file_id
        file = await bot.get_file(file_id)
        welcome_message = await message.answer("Ожидайте файл✨")
        file_path = file.file_path

        downloaded_file = await bot.download_file(file_path)
        file_name = f'{document.file_name}'
        
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file.read())
            image_path = file_name
            output_prefix = "radar"
            num_slices = 143
            user = message.from_user.id
            await bot.send_message(ADMIN_ID, f"Map\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user}")
            await slice_and_send_image(message, image_path, output_prefix, num_slices)
            await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
            
            
            
            
            
    if message.caption == "/logo":
              document = message.document
              file_id = document.file_id
              file = await bot.get_file(file_id)
              welcome_message = await message.answer("Ожидайте файл✨")
              file_path = file.file_path

              downloaded_file = await bot.download_file(file_path)
              file_name = f'{document.file_name}'
        
              with open(file_name, 'wb') as new_file:
                    new_file.write(downloaded_file.read())
                    os.rename(file_name, "logo.btx")
              original_file = 'logo.btx'
              new_file_names = ['logobranapa.btx', 'logobraqua.btx', 'logobrarkhangelsk.btx', 'logobrarzamas.btx', 'logobrazure.btx', 'logobrbarnaul.btx', 'logobrbelgorod.btx', 'logobrblack.btx', 'logobrblue.btx', 'logobrbratsk.btx', 'logobrbryansk.btx', 'logobrcheboksary.btx', 'logobrchelyabinsk.btx', 'logobrcherry.btx', 'logobrchilli.btx', 'logobrchoco.btx', 'logobrcrimson.btx', 'logobrekb.btx', 'logobrgold.btx', 'logobrgray.btx', 'logobrgreen.btx', 'logobrgrozny.btx', 'logobrice.btx', 'logobrindigo.btx', 'logobrirkutsk.btx', 'logobrivanovo.btx', 'logobrkaliningrad.btx', 'logobrkaliningrad2.btx', 'logobrkazan.btx', 'logobrkemerovo.btx', 'logobrkhabarovsk.btx', 'logobrkirov.btx', 'logobrkrasnodar.btx', 'logobrkrasnoyarsk.btx', 'logobrkursk.btx', 'logobrlime.btx', 'logobrlipetsk.btx', 'logobrmagenta.btx', 'logobrmakhachkala.btx', 'logobrmoscow.btx', 'logobrmurmansk.btx', 'logobrnsk.btx', 'logobromsk.btx', 'logobrorange.btx', 'logobrorel.btx', 'logobrorenburg.btx', 'logobrpenza.btx', 'logobrperm.btx', 'logobrpink.btx', 'logobrplatinum.btx', 'logobrpskov.btx', 'logobrpurple.btx', 'logobrred.btx', 'logobrrostov.btx', 'logobrryazan.btx', 'logobrsamara.btx', 'logobrsaratov.btx', 'logobrsmolensk.btx', 'logobrsochi.btx', 'logobrspb.btx', 'logobrstavropol.btx', 'logobrtambov.btx', 'logobrtolyatti.btx', 'logobrtula.btx', 'logobrtyumen.btx', 'logobrufa.btx', 'logobrulyanovsk.btx', 'logobrvladikavkaz.btx', 'logobrvladivostok.btx', 'logobrvolgograd.btx', 'logobrvoronezh.btx', 'logobrwhite.btx', 'logobryakutsk.btx', 'logobryaroslavl.btx', 'logobryellow.btx','logobrchita.btx', 'logobrkostroma.btx']
              os.makedirs('logo', exist_ok=True)
              for new_name in new_file_names:
                          destination = os.path.join('logo', new_name)
                          shutil.copyfile(original_file, destination)
                          print(f'Копирование {original_file} в {new_name}')
              else:
                    folder_path = 'logo'
                    zip_folder(folder_path)
                    await message.reply_document(types.InputFile("logo.zip"), caption='Держи свои логотипы⚡️')
                  #  await message.reply_document(types.InputFile("logo.zip"), caption='Держи свои логотипы⚡️')
                    await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
                    user = message.from_user.username
                    await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
                    
    
    
    capt = message.caption

    # Разделяем ввод на части
    parts = capt.split()

    # Удаляем слово "привет"
    if "/ziprgb" in parts:
        parts.remove("/ziprgb")
        rgb_color = " ".join(parts)
        os.makedirs("rec", exist_ok=True)

        #await message.reply(f"{gb}
        document = message.document
        file_id = document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        downloaded_file = await bot.download_file(file_path)
        file_name = f'{document.file_name}'

        # Сохраняем файл в "rec"
        with open(os.path.join("rec", file_name), 'wb') as new_file:
              new_file.write(downloaded_file.read())

        # Перекрашиваем файл
        recolor_image(os.path.join("rec", file_name), os.path.join("rec", file_name), rgb_color) 

        # Отправляем обработанный файл
        await message.answer_document(types.InputFile(os.path.join("rec", file_name)), caption="Держи свой перекрашенный файл⚡")

        # Логирование
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")

        # Удаляем папку "rec"
        await asyncio.sleep(1) # Ждем 1 секунду, чтобы файл точно отправился
        os.rmdir('rec') 
    
    
    
    
        







    if message.caption == "/bildboard":
                    document = message.document
                    file_id = document.file_id
                    file = await bot.get_file(file_id)
                    welcome_message = await message.answer("Ожидайте файл✨")
                    file_path = file.file_path

                    downloaded_file = await bot.download_file(file_path)
                    file_name = (f'{document.file_name}')
                    with open(file_name, 'wb') as new_file:
                          new_file.write(downloaded_file.read())
                    os.rename(file_name, "ogo.btx")
                    original_file = 'ogo.btx'
                    new_file_names = ["Billb_GTABerlin.btx", "bilb_sign1.btx", "bilb_sign2.btx","Billb_AlienCity.btx", "Billb_GostownParadise.btx", "Billb_GTABerlin.btx", "Billb_GTAUnited.btx", "Billb_MyriadIslands.btx",
"Billb_SanVice.btx","Billb_YouAreHere.btx","BLBRD_1_a889.btx","BLBRD_2_a889.btx","BLBRD_3_a889.btx","BLBRD_4_a889.btx","BLBRD_5_a889.btx","BLBRD_6_a889.png", "bilb_sing2"]
                    os.makedirs('bildboard', exist_ok=True)
                    for new_name in new_file_names:
                          destination = os.path.join('bildboard', new_name)
                          shutil.copyfile(original_file, destination)
                          print(f'Копирование {original_file} в {new_name}')
                    else:
                          folder_path = 'bildboard'
                          zip_folder(folder_path)
                          await message.reply_document(types.InputFile("bildboard.zip"), caption='Держи свои билборды⚡️')
                          await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
                          os.rmdir('bildboard')
                          os.remove("bildboard.zip")
                          user = message.from_user.username
                          await bot.send_message(ADMIN_ID, f" БИЛДБОПОД\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
                          
                          
                          
                          
                          
    cpt = message.caption

    # Разделяем ввод на части
    parts = cpt.split()

    # Удаляем слово "привет"
    if "/recolor" in parts:
        parts.remove("/recolor")
        gb = " ".join(parts)
                          
        document = message.document
        file_id = document.file_id
        file = await bot.get_file(file_id)
        welcome_message = await message.answer("Ожидайте файл✨")
        file_path = file.file_path

        downloaded_file = await bot.download_file(file_path)
        file_name = (f'{document.file_name}')
        with open(file_name, 'wb') as new_file:
              new_file.write(downloaded_file)
        zip_file_path = file_name
        extract_zip(zip_file_path)
        colorREC = "255,0,0" 
        recolor_folder("rec", colorREC)
        create_zip("rec", "file.zip")
        print(f"ZIP-архив 'recolored_listva.zip' создан успешно!")
        await message.answer_document(types.InputFile("file.zip"), caption='Держи перекрашеные файлы⚡')
                    



  
          




dayn = "7357565595"
ADMIN_ID = "6033522149"
ADMIN = "6033522149"
st =('''
Привет ты попал в Lxz tool✨
Рекомендуется прочитать документацию
чтобы узнать функции бота
''')


hl = '''
/start - начать работу с ботом
/map - разрезать свою карту на части 
/blood - создать файл цветной крови
/timecyc - создать свой таймкук любых цветов
/colorcyc - создать цветной colorcycle
/button - создать кнопки по rgb цветам
/rgb - перекраска изображений файл и описание /rgb *rgb цвет*
/deagle - gun editor *кол-ов патрон,*разброс оружия*
/bildboard - создание билбордов из btx файла, файл и описание /bildboard
/logo - создание Логотипов из btx файла, файл и описание /logo
'''
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
      await message.answer(hl)



@dp.message_handler(commands=['logo'])
async def help(message: types.Message):
      await message.answer("Отправьте файл и добавьте к нему описание /logo")


@dp.message_handler(commands=['rgb'])
async def help(message: types.Message):
      await message.answer("Отправьте файл и добавьте к нему описание /rgb *ваш rgb цвет* пример👇")
      await message.answer_document(types.InputFile("test/ex.png"), caption="/rgb 0, 255, 0")


@dp.message_handler(commands=['bildboard'])
async def help(message: types.Message):
      await message.answer("Отправьте ваш файл btx и добавьте к нему описание /bildboard и вы получите свои билборды с нужными именами в ZIP ")


@dp.message_handler(commands=['send'])
async def send_message(message: types.Message):
    try:
        # Разделяем сообщение по пробелам
        command, user_id, *text = message.text.split()
        text_message = ' '.join(text)

        # Преобразуем user_id к int
        user_id = int(user_id)

        # Отправляем сообщение пользователю
        await bot.send_message(user_id, f"сообщения от администратора: >> {text_message}")
        await message.reply("Сообщение отправлено!")
    except Exception as e:
        print("Ерорка")



'''
🎨Hex палитра

📃Документация
'''



ti = ('''
Используйте /timecyc и 4 цвета hex
к примеру /timecyc #FFFFFF #FFFFFF #FFFFFF #FFF000
Используй палитру цветов которая представлена ниже
''')

mapH = '''
Используйте команду /map
таким образом чтобы ваша
карта была ОБЕЗАТЕЛЬНО формата PNG.
И было описание /map 
чтобы бот понял что делать с этим файлом.

Пример представлен ниже👇
'''

fr = '''
Неизвестный формат файла
для разреза карты используется формат PNG
file.png
'''

ft = '''
Используйте команду /blood🩸
и после нее hex цвет

пример и палитра цветов представлена ниже👇

'''


@dp.message_handler(commands=("blood"))
async def blood(message: types.Message):
    color = message.text.lstrip('/blood #')
    if len(color) < 6:
        kb = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="🎨палитра цветов",  web_app=WebAppInfo(url="https://g.co/kgs/iLyiVzY"))
        kb.row(url_button)
        
        
        await message.answer("❓")
        await message.answer(ft, reply_markup=kb)
        await message.answer("/blood #FFFF00")
        
        
        
        
        
        
        
        
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
        return
    
    random_name = message.from_user.username
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    grn1 = f'ids.{random_name}_particle.cfg'
    with open('debug/parta.cfg', 'r') as file:
        data = file.read()
        data = data.replace("r22", str(rgb[0])).replace("g22", str(rgb[1])).replace("b22", str(rgb[2]))
    with open(grn1, 'w') as file:
        file.write(data)
        await message.reply_document(types.InputFile(grn1), caption="Держи свой particle⚡")
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")








@dp.message_handler(content_types=['document'])
async def handle_docs(message: types.Message):
    # Проверяем формат файла
    if message.document.mime_type == 'image/jpeg':
        await message.answer("❓")
        await message.answer(fr)





@dp.message_handler(commands=['map'])
async def maphelp(message: types.Message):
      await message.answer("❓")
      await message.answer(mapH)
      await message.answer_document(types.InputFile("debug/map2.png"), caption="/map")


            
            

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
       kb = types.InlineKeyboardMarkup()
       url_button = types.InlineKeyboardButton(text="Наш канал📱", url="https://t.me//lxz_mods")
       
    #   u = types.InlineKeyboardButton(text="📃Документация", web_app=WebAppInfo(url="https://teletype"))
       kb.row(url_button)
       
       
       k = types.InlineKeyboardMarkup()
       url_butto = types.InlineKeyboardButton(text="Документация🧾", url="teletype.in/@timka_lxz/atlYG7SpCC0")
       url_button = types.InlineKeyboardButton(text="Наш канал📱", url="https://t.me//lxz_mods")
       
    #   u = types.InlineKeyboardButton(text="📃Документация", web_app=WebAppInfo(url="https://teletype"))
       k.row(url_button, url_butto)
       
       
       welcome_message = await message.answer("подпишись на наш канал", reply_markup=kb)
      # time.sleep(3)
     #  await message.reply("Проверка может занять от 10секунд до минуты")
       
       
       time.sleep(5)
       await bot.edit_message_text("Спасибо за подписку♥️", chat_id=message.chat.id, message_id=welcome_message.message_id)
       await message.answer("👋")
       await message.answer(st, reply_markup=k)
       
       
       
@dp.message_handler(commands=['timecyc'])
async def timecyc(message: types.Message):
    timka = str(message.text)
    if len(timka) < 35:
          
          kb = types.InlineKeyboardMarkup()
          url_button = types.InlineKeyboardButton(text="🎨палитра цветов",  web_app=WebAppInfo(url="https://g.co/kgs/iLyiVzY"))
          kb.row(url_button)
          
          
          
          
          await message.reply(ti, reply_markup=kb)
          
          user = message.from_user.username
          await bot.send_message(ADMIN_ID, f"NOT GIVE\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
          
          return
          
    random_name = message.from_user.username
    grn1 = f"ids.{random_name}_timecyc.json"
    usercs = str(message.text)
    usercs = usercs.lstrip('/timecyc ').replace('#', '').split()
  #  await message.reply("")

    colors = [
        tuple(int(usercs[i][j:j + 2], 16) for j in (0, 2, 4)) for i in range(4)
    ]
    with open('debug/TCYC.json', 'r') as file:
        data = file.read()
        data = data.replace('skbr', str(colors[0][0])).replace('skbg', str(colors[0][1])).replace('skbb', str(colors[0][2])).replace('sktr', str(colors[1][0])).replace('sktg', str(colors[1][1])).replace('sktb', str(colors[1][2])).replace('scr', str(colors[2][0])).replace('scg', str(colors[2][1])).replace('scb', str(colors[2][2])).replace('clr', str(colors[3][0])).replace('clg', str(colors[3][1])).replace('clb', str(colors[3][2]))
        with open(grn1, 'w') as file:
              file.write(data)
              
        user = message.from_user.username
        print(f".      ФАЙЛ ОТДАН    {user}: {message.text}")
        print(".             ФАЙЛ ОТДАН")
        await message.reply_document(types.InputFile(grn1), caption='Держи свой timecyc⚡️')
        EX = f"GIVE\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} "
        await bot.send_message(ADMIN_ID, f"{EX}")





@dp.message_handler(commands=['colorcycle'])
async def cycle(message: types.Message):
      await message.answer("Используйте команду /colorcyc")
      user = message.from_user.username
      await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")


@dp.message_handler(commands=("colorcyc")) 
async def colorcyc(message: types.Message):
    color = str(message.text) 
    if len(color) < 12:
        user = message.from_user.username
        print(f".    ОШИБКА.     {user}: {message.text}")
        user = message.from_user.username
        print("")
        kb = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="🎨палитра цветов",  web_app=WebAppInfo(url="https://g.co/kgs/iLyiVzY"))
        kb.row(url_button)
        
        
        
        
        
        
        await message.answer("❓")
        await message.answer("Используйте команду /colorcyc\nтаким образом чтобы после команды был цвет в формате hex\n\nпример представлен ниже👇", reply_markup=kb)
        await message.answer("/colorcyc #FF0000")
             
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
        
        return

    random_name = message.from_user.username
    color = str(message.text)
    grn1 = f"ids.{random_name}_colorcycle.dat"
    rgb = (tuple(int(color.lstrip('/colorcyc #')[i:i+2], 16)/100 for i in (0, 2, 4)))
    with open('debug/cc.dat', 'r') as file:
        data = file.read()
        data = data.replace('r', str(round(rgb[0],3))).replace('g', str(round(rgb[1],3))).replace('b', str(round(rgb[2],3)))
        with open(grn1, 'w') as file:
            file.write(data)
            user = message.from_user.username
            print(f".      ФАЙЛ ОТДАН     {user}: {message.text}")
          #  print(".             ФАЙЛ ОТДАН")
            print("")
            await message.reply_document(types.InputFile(f"{grn1}"), caption='Держи свой Colorcycle⚡️')
            user = message.from_user.username
            await bot.send_message(ADMIN_ID, f"GIVE\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")



@dp.message_handler(commands=['deagle'])
async def cmd_cfg(message: types.Message):
    try:
        # получаем аргументы команды
        args = message.get_args().split(',')
        if len(args) != 2:
            await message.answer("❓")
            await message.answer("Используйте команду /deagle чтобы после нее находились 2 числа\n количество патрон в магазине,разброс оружия пример👇")
            await message.answer("/deagle 9,50")
            await bot.send_message(ADMIN_ID, f"НОТ GIVE ВЕАП\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{message.from_user.username} \nДействие: {message.text} \nДата: {message.date} ")
            return
        
        # парсим аргументы
        PT = float(args[0])
        RAZB = int(args[1])
        
        # Преобразование PT в целое число, если оно целое
        if PT.is_integer():
            PT = int(PT)

        with open("weapon.isx", "r") as file:
            dg = file.read()
            dg = dg.replace("ПТ", str(PT))
            dg = dg.replace("RAZB", str(RAZB))
            random_name = message.from_user.username
            eix = f"ids.{random_name}_weapon.dat"
        with open(eix, "w") as file:
           file.write(dg)
        
        
        await message.answer_document(types.InputFile(eix), caption = f"держи свой weapon⚡\nКоличество патрон в магазине: {PT}\nРазброс патрон: {RAZB}")
        await bot.send_message(ADMIN_ID, f" GIVE ВЕАП\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{message.from_user.username} \nДействие: {message.text} \nДата: {message.date} ")
    except Exception as e:
        await message.answer("❌")
        await message.answer("Вы используете что-то кроме чисел\nИСПОЛЬЗУЙТЕ ПО ПРИМЕРУ НИЖЕ\n /deagle количество пт в магазине,разброс пт\nПолноценный пример👇")
        await message.reply("/deagle 9,1")
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
       # await message.reply(e)














@dp.message_handler(commands=['bcp'])
async def bcp(message: types.Message):
      await message.answer_document(types.InputFile("common.bpc"), caption = "держи обновленный common в формате BCP⚡")
      await message.answer_document(types.InputFile("common.zip"), caption = "держи обновленный common в формате ZIP⚡")
      await bot.send_message(ADMIN_ID, f"БПК И ЗИПКИ GIVE\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")


@dp.message_handler()
async def handle_message(message:  types.Message):
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)