import logging
#import tarfile
dayn = "6646133212"
ADMIN_ID = "6646133212"
ADMIN = "6646133212"
#import lzma
from aiogram import Bot, Dispatcher, types
#from aiogram.contrib.middlewares.logging import LoggingMiddleware
import shutil
import os
from aiogram.types.web_app_info import WebAppInfo
import zipfile
from PIL import Image
import time
#from text import start, mapo, new_smoke, new_listva
#from image_slicer import slice
import random
from random import *
#from rarfile import RarFile
#import numpy as np
from aiogram.utils.exceptions import BadRequest
import datetime
import string
import asyncio
from aiogram.dispatcher import FSMContext
from secrets import token_hex
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








# ТЕСТ 7480096602:AAEDLv749s3dv5iNty_BDJdKoUvJQ44Gx-4
# основа "7015124936:AAHjFtcciCAZGfxbscNh8HX3V5t_IjOgyBk" 
API_TOKEN = "8116506633:AAEX2Fzyb9qE4cWw2UakbPysxk8XMA4PzUU" 
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




def recolor_imae(input_path, output_path, color):
    img = Image.open(input_path).convert("RGBA")  # Используем RGBA для пр озрачности
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





@dp.message_handler(commands=['blood'])
async def blood_command(message: types.Message):
    try:
        # Разделение команды на части
        command_parts = message.text.split()
        
        if len(command_parts) != 3:
            await message.reply("Используйте: /blood <hex цвет крови> <размер>\nПалитра цветов представлена при команде /timecyc")
          #  await message.answer("/blood #FFFFF0 0.300", reply_markup="kb")
            return

        hex_color = command_parts[1]
        siz = float(command_parts[2])

        # Проверяем правильность hex цвета
        if not hex_color.startswith('#') or len(hex_color) != 7:
            await message.reply("Ошибка: Неверный hex либо размер")
            return

        # Преобразование hex в RGB
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        # Создание ответа
        response = f"{r} {g} {b} {siz} ИНФО"
        await message.reply("ожидайте файл✨")

        # Чтение содержимого файла
        with open("particle.cfgg", "r") as file:
            t = file.read()
            # Замена значений в содержимом
            t = t.replace("r22", str(r))
            t = t.replace("g22", str(g))
            t = t.replace("b22", str(b))
            t = t.replace("Q11", str(siz))

            # Генерация уникального имени файла
            code = token_hex(3)
            nam = f"ids.{code}_particle.cfg"
        
        # Запись измененного содержимого в новый файл
        with open(nam, "w") as file:
            file.write(t)

        # Отправка документа пользователю
        await message.answer_document(types.InputFile(nam), caption="Держи свой particle⚡")

    except ValueError:
        await message.reply("")
    except FileNotFoundError:
        await message.reply("INPUT NOT FOUND обратитесь к @timka_laxzisse")
    except Exception as e:
        await message.reply(f"")


        









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
        code = token_hex(3)
        bn = f"ids.{code}_button.zip"
        os.rename("button.zip", bn)
        await message.answer_document(types.InputFile(bn), caption="держи свои кнопки⚡")
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
     #   await message.answer_document(types.InputFile("button.zip"), caption="sex")
          
    else:
        await message.answer("❓")
        await message.answer("Используйте /button и цвет в формате RGB\nПример: /button 255,0,0")
        user = message.from_user.id
        await bot.send_message(ADMIN_ID, f"Map\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user}")
        




'''
@dp.message_handler(commands=['road'])
async def ebal(message: types.Message):
    if message.text.count(",") == 2:  # Проверяем наличие двух запятых
        rgbb = message.text.replace('/road ', '')
        welcome_message = await message.answer("Ожидайте файл✨\nЭто может занять около 2 минут")
        
        os.makedirs('road', exist_ok=True)
        
        file_name = ["lf_arzparking1.png", "kor_road8.png", "kor_road2.png", "kor_road10.png", "kor_road1.png", "kart_asph3.png", "helipad8204a.png", "gett_parking.png", "gazprof_ash4.png", "gazoncottages2.png", "E_Ash_DrR_P.png", "E_Ash_DrR11.png", "CRB_roadsv1Str2.png", "CRB_roadsv1Str.png", "CRB_roadsv1park.png", "CRB_roadsv1.png", "CRBroads667.png", "CRBroads666.png", "auto_asphalt3.png", "country_road2.png", "auto_asphalt2.png", "asfpark8001.png", "AsfCRBtraskc6.png", "AsfCRBtraskc4.png", "AsfCRBtraskc3.png", "AsfCRBtraskc2.png", "AsfCRBtraskc1.png", "AsfCRBtraskc1suj.png", "arz_road_clePark3.png", "arzpark_bike2.png", "arzpark_bike1.png", "AphaltR1_10.png", "A889_newroad9.png", "A889_newroad8.png", "A889_newroad7.png", "A889_newroad4.png", "A889_newroad30.png", "A889_newroad28.png", "A889_newroad26.png", "A889_newroad24.png", "A889_newroad23.png", "A889_newroad21.png", "A889_newroad20.png", "A889_newroad18.png", "A889_newroad17.png", "A889_newroad16.png", "A889_newroad13.png", "A889_newroad12.png", "A889_newroad10.png", "A889_newashM.png", "A889_newash28.png", "A889_newash26.png", "lf_arzper2.png", "kart_start.png", "concrete33park_1.png", "lf_arzrd6.png", "lf_arzrd1.png", "lf_arzrd5.png", "lf_arzrd8.png", "lf_arzrd7.png", "lf_arzrd10.png", "lf_arzrd9.png", "new_asf_center.png", "NAVA_per1_a889.png", "lytash_parking1.png", "nn_road_2.png", "new_asfblend_oldgrass2.png", "new_asf_pulse.png", "nn_road_3.png", "nn_road_4.png", "nn_road_3b.png", "prich_newash28_1.png", "prich_newash28_2.png", "prich_newash28.png", "prich_newash30.png", "road2_a889.png", "road_2_2.png", "road1.png", "road4.png", "road3.png", "road2.png", "roadasf1.png", "road10.png", "road10_spec.png", "sa_centerblendnew.png", "roadasf3.png", "roadasf2.png", "srd_terrpick_rpark.png", "SBER_road2_a889.png", "sa_pulseblendnew.png", "vad_newash26.png", "teslaparkovkaline.png", "tkparklines.png", "wolv_roads.png", "wolv_roads_cross.png", "wolv_roads_per.png", "wolv_roadscrb2.png", "wolv_roadscr33b242.png", "wolv_roads2.png", "ws_carpark1.png", "znam_road2.png", "wolv_roadsCRBY.png"]
        alpha = 0.3
        
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
            output_path = os.path.join('road', file)
            recolor_image(file, output_path, color, alpha)
            print(f"готово {file}")
            

        # Создание ZIP-архива
        zip_file_path = 'butt.zip'
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            for file in file_name:
                zipf.write(os.path.join('road', file), file)

        await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
        code = token_hex(3)
        bn = f"ids.{code}_road.zip"
        os.rename("butt.zip", bn)
        await message.answer_document(types.InputFile(bn), caption="держи свои перекрашеные дороги ⚡")
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"ГИВ РОАД\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
     #   await message.answer_document(types.InputFile("button.zip"), caption="sex")
          
    else:
        await message.answer("❓")
        await message.answer("Используйте /road и цвет дорог в формате RGB\nПример: /road 255,0,0")
        user = message.from_user.id
        await bot.send_message(ADMIN_ID, f"ROAD ЕРОР\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user}")
'''
        
        



@dp.message_handler(commands=['hud'])
async def ebal(message: types.Message):
    if message.text.count(",") == 2:  # Проверяем наличие двух запятых
        rgbb = message.text.replace('/hud ', '')
        welcome_message = await message.answer("Ожидайте файл✨")
        
        os.makedirs('hud', exist_ok=True)
        
        file_name = ["hud_back.png", "hud_center.png", "hud_down.png", "hud_ruble.png", "hud_heart.png", "hud_up.png", "hud_health_scale.png", "hud_menu.png", "hud_armor.png"]
        alpha = 0.25
        
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
            output_path = os.path.join('hud', file)
            recolor_image(file, output_path, color, alpha)
            print(f"готово {file}")

        # Создание ZIP-архива
        zip_file_path = 'hud.zip'
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            for file in file_name:
                zipf.write(os.path.join('hud', file), file)

        await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
        code = token_hex(3)
        bn = f"ids.{code}_hud.zip"
        os.rename("hud.zip", bn)
        await message.answer_document(types.InputFile(bn), caption="держи свой худ⚡")
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"ГИФ ХУД\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
     #   await message.answer_document(types.InputFile("button.zip"), caption="sex")
          
    else:
        await message.answer("❓")
        await message.answer("Используйте /hud и цвет худа в формате RGB\nПример: /hud 255,0,0")
        user = message.from_user.id
        await bot.send_message(ADMIN_ID, f"HUD HOT\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user}")



    


async def slice_and_send_image(message: types.Message, image_path, output_prefix, num_slices):
    img = Image.open(image_path)
    width, height = img.size
    
    # Разделение на 14x14 сегментов
    segment_width = width // 14
    segment_height = height // 14
    
    zip_name = f'map.zip'
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for i in range(14):
            for j in range(14):
                left = j * segment_width
                upper = i * segment_height
                right = left + segment_width
                lower = upper + segment_height
                
                segment = img.crop((left, upper, right, lower))
                number = i * 14 + j
                segment_name = f"{output_prefix}{number:03}.png"
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
            num_slices = 196
            user = message.from_user.id
            await bot.send_message(ADMIN_ID, f"Map\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user}")
            await slice_and_send_image(message, image_path, output_prefix, num_slices)
            
            code = token_hex(3)
            '''
            nnn = f"ids.{code}_map.zip"
            os.rename("map.zip", nnn)
            await message.answer(InputFile(nnn), caption="держи свой файл⚡")
            '''
            
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
              new_file_names = ["logobranapa.btx", "logobraqua.btx", "logobrarkhangelsk.btx", "logobrarzamas.btx", "logobrastrakhan.btx", "logobrazure.btx", "logobrbarnaul.btx", "logobrbelgorod.btx", "logobrblack.btx", "logobrblue.btx", "logobrbratsk.btx", "logobrbryansk.btx", "logobrcheboksary.btx", "logobrchelyabinsk.btx", "logobrcherry.btx", "logobrchilli.btx", "logobrchita.btx", "logobrchoco.btx", "logobrcrimson.btx", "logobrekb.btx", "logobrgold.btx", "logobrgray.btx", "logobrgreen.btx", "logobrgrozny.btx", "logobrice.btx", "logobrindigo.btx", "logobrirkutsk.btx", "logobrivanovo.btx", "logobrizhevsk.btx", "logobrkaliningrad.btx", "logobrkaliningrad2.btx", "logobrkaluga.btx", "logobrkazan.btx", "logobrkemerovo.btx", "logobrkhabarovsk.btx", "logobrkirov.btx", "logobrkostroma.btx", "logobrkrasnodar.btx", "logobrkrasnoyarsk.btx", "logobrkursk.btx", "logobrlime.btx", "logobrlipetsk.btx", "logobrmagenta.btx", "logobrmakhachkala.btx", "logobrmoscow.btx", "logobrmurmansk.btx", "logobrnovgorod.btx", "logobrnsk.btx", "logobromsk.btx", "logobrorange.btx", "logobrorel.btx", "logobrorenburg.btx", "logobrpenza.btx", "logobrperm.btx", "logobrpink.btx", "logobrplatinum.btx", "logobrpskov.btx", "logobrpurple.btx", "logobrred.btx", "logobrrostov.btx", "logobrryazan.btx", "logobrsamara.btx", "logobrsaratov.btx", "logobrsmolensk.btx", "logobrsochi.btx", "logobrspb.btx", "logobrstavropol.btx", "logobrsurgut.btx", "logobrtaganrog.btx", "logobrtambov.btx", "logobrtolyatti.btx", "logobrtomsk.btx", "logobrtula.btx", "logobrtver.btx", "logobrtyumen.btx", "logobrufa.btx", "logobrulyanovsk.btx", "logobrvladikavkaz.btx", "logobrvladimir.btx", "logobrvladivostok.btx", "logobrvolgograd.btx", "logobrvologda.btx", "logobrvoronezh.btx", "logobrwhite.btx", "logobryakutsk.btx", "logobryaroslavl.btx", "logobryellow.btx"]
              os.makedirs('logo', exist_ok=True)
              for new_name in new_file_names:
                          destination = os.path.join('logo', new_name)
                          shutil.copyfile(original_file, destination)
                          print(f'Копирование {original_file} в {new_name}')
              else:
                    folder_path = 'logo'
                    zip_folder(folder_path)
                    code = token_hex(3)
                    nn = f"ids.{code}_logo.zip"
                    os.rename("logo.zip", nn)
                    await message.reply_document(types.InputFile(nn), caption='Держи свои логотипы⚡️')
                  #  await message.reply_document(types.InputFile("logo.zip"), caption='Держи свои логотипы⚡️')
                    await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
                    user = message.from_user.username
                    await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
                    
    
    
    
    
    
        







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
                          code = token_hex(3)
                        #  os.rename("bildboard.zip", f"ids.{code}_bildboard.zip")
                          fi = f"{code}_bildboard.zip"
                          await message.reply_document(types.InputFile("bildboard.zip"), caption='Держи свои билборды⚡️')
                          await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
                          os.rmdir('bildboard')
                          user = message.from_user.username
                          await bot.send_message(ADMIN_ID, f" БИЛДБОПОД\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
                          
                          
                          
                          
                          
    cpt = message.caption

    # Разделяем ввод на части
    parts = cpt.split()

    # Удаляем слово "привет"
    if "/rgb" in parts:
        parts.remove("/rgb")
        gb = " ".join(parts)
                          
        document = message.document
        file_id = document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        downloaded_file = await bot.download_file(file_path)
        file_name = f'1.{document.file_name}'

        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file.read())

        color = f"{gb}"  # Ваш RGB цвет
        alpha = 0.3
        recolor_image(file_name, file_name, color, alpha)
     #   os.rename("ran.png", f"1.{document.file_name}")
        await message.answer_document(types.InputFile(file_name), caption="Держи свой перекрашеный файл⚡")
                    
    if message.caption == "/listva":
              document = message.document
              file_id = document.file_id
              file = await bot.get_file(file_id)
              welcome_message = await message.answer("Ожидайте файл✨")
              file_path = file.file_path

              downloaded_file = await bot.download_file(file_path)
              file_name = f'{document.file_name}'
        
              with open(file_name, 'wb') as new_file:
                    new_file.write(downloaded_file.read())
                    os.rename(file_name, "loo.btx")
              original_file = 'loo.btx'
              new_file_names = ['TomatoFarm.btx',
    'tomato.btx',
    'tikva.btx',
    'svekla.btx',
    'stvolListv1.btx',
    'kustik1.btx',
    'kust_farm1.btx',
    'krapiva_list.btx',
    'kolosya_rog.btx',
    'kustik2.btx',
    'WH_flowers1.btx',
    'lopux_list.btx',
    'lopux_koluchka.btx',
    'LeavesTropical0218_1.btx',
    'LeavesTropical0202_1.btx',
    'LeavesTropical0141_1.btx',
    'lager_trees2.btx',
    'lager_trees1.btx',
    'kyst3.btx',
    'yellosmallflowers.btx',
    'starflower3yel.btx',
    'starflower3prpl.btx',
    'starflower3.btx',
    'starflower2wht.btx',
    'starflower2.btx',
    'rus_bigORGANGEflower.btx',
    'rn_hell_flow.btx',
    'mp_h_acc_vase_flowers_04.btx',
    'mp_gs_flowerwall.btx',
    'mp_flowerbush.btx',
    'lf_arzflowers1.btx',
    'km_flowerpic2.btx',
    'int_pr_flow2.btx',
    'int_pr_flow1.btx',
    'int_fsb_flow1a.btx',
    'int_fsb_flow1.btx',
    'hot_flowers1.btx',
    'flowert.btx',
    'fialkiflowers.btx',
    'edovo_coundom_flower.btx',
    'CJ_FLOWER_256cj_flower_a.btx',
    'cj_flower(hi_res)cj_flower_a(h.btx',
    'byssch_flower5.btx',
    'byssch_flower4.btx',
    'byssch_flower3.btx',
    'byssch_flower2.btx',
    'byssch_flower1.btx',
    'bys_flowers.btx',
    'BRG_flowers1.btx',
    'apat_flowers.btx',
    'UGPRST_der1.btx',
    '43tree1.btx',
    '43tree2.btx',
    '43tree3.btx',
    '43tree4.btx',
    '43tree5.btx',
    '43tree6.btx',
    '43tree7.btx',
    '43tree8.btx',
    '43tree9.btx',
    '44tree1.btx',
    '44tree2.btx',
    '44tree4.btx',
    '44tree5.btx',
    'AppleTree.btx',
    'AucTreeCrone8712.btx',
    'b_craet1_4_ca.btx',
    'beregd1_listv2.btx',
    'BRTREE_Atl_B.btx',
    'BRTREE_leaf1.btx',
    'BRTREE_leaf1o.btx',
    'BRTREE_leaf2.btx',
    'BRTREE_leaf2o.btx',
    'BRTREE_leaf3.btx',
    'BRTREE_leaf4.btx',
    'BRTREE_leaf4o.btx',
    'BRTREE_leaf5.btx',
    'BRTREE_leaf5o.btx',
    'BRTREE_leaf6.btx',
    'BRTREE_leaf7.btx',
    'BRTREE_leaf8.btx',
    'BRTREE_leaf8o.btx',
    'BukTree1.btx',
    'BukTree2.btx',
    'bys_appletree.btx',
    'bys_cherrytree.btx',
    'bys_plumtree.btx',
    'bys_wires.btx',
    'GrassA_04.btx',
    'GrassA_15.btx',
    'GrassA_15_1.btx',
    'GrassA_05.btx',
    'derevachkacrb.btx',
    'derevo.btx',
    'derevo3.btx',
    'derevo_krov.btx',
    'derevoclub8201.btx',
    'derevoclub8201st.btx',
    'derevoclub8202st.btx',
    'derevoclub8203.btx',
    'derevoclub8203st.btx',
    'derevoclub82021.btx',
    'derevoclub82022.btx',
    'GrassA_20.btx',
    'LODH_Rdeadtree.btx',
    'LODH_pinetree3.btx',
    'R_Dub1.btx',
    'KustRog8716.btx',
    'lentisk.btx',
    'newtreeleaves128.btx',
    'newtreeleavesb128.btx',
    'R_Listv1.btx',
    'Tree.btx',
    'tree19Mi.btx',
    'tree_lodderevo1.btx',
    'tree_lodeubeech1.btx',
    'tree_lodfikovnik.btx',
    'tree_lodkastan.btx',
    'tree_lodlinden.btx',
    'tree_lodpaper_der1.btx',
    'tree_lodpaper_der2.btx',
    'tree_lodwillow.btx',
    'TREE_STUB1.btx',
    'treeCRB221_1.btx',
    'TreeCron9716.btx',
    'TreeCron9716_2.btx',
    'LODH_pinetree2.btx',
    'LODH_pinetree1.btx',
    'LODH_leaftree_vol.btx',
    'LODH_leaftree_sml.btx',
    'LODH_leaftree_root.btx',
    'LODH_leaftree_med.btx',
    'LODH_leaftree_big.btx',
    'LODbuktree8_a889.btx',
    'LODbuktree7_a889.btx',
    'LODbuktree6_a889.btx',
    'LODbuktree5_a889.btx',
    'LODbuktree4_a889.btx',
    'LODbuktree3_a889.btx',
    'LODbuktree2_a889.btx',
    'LODBRTREE_atl.btx',
    'LODBRTREE_4_5_9_10.btx',
    'LODBRTREE_2_3.btx',
    'LODBRTREE_1_6_7_8.btx',
    'R_Berez1_b.btx',
    'R_Berez1_t.btx',
    'cottagetuya.btx',
    'cottagetuya-2.btx',
    'NRock_kust2.btx']
              os.makedirs('listik', exist_ok=True)
              for new_name in new_file_names:
                          destination = os.path.join('listik', new_name)
                          shutil.copyfile(original_file, destination)
                          print(f'Копирование {original_file} в {new_name}')
              else:
                    folder_path = 'listik'
                    zip_folder(folder_path)
                    code = token_hex(3)
                    nn = f"ids.{code}_listik.zip"
                    os.rename("listik.zip", nn)
                    await message.reply_document(types.InputFile(nn), caption='Держи свои логотипы⚡️')
                  #  await message.reply_document(types.InputFile("logo.zip"), caption='Держи свои логотипы⚡️')
                    await bot.edit_message_text("Ваш файл ниже⚡️", chat_id=message.chat.id, message_id=welcome_message.message_id)
                    user = message.from_user.username
                    await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")

    if message.caption == "/aim":
              document = message.document
              file_id = document.file_id
              file = await bot.get_file(file_id)
              welcome_message = await message.answer("Ожидайте файл✨")
              file_path = file.file_path

              downloaded_file = await bot.download_file(file_path)
              file_name = f'{document.file_name}'
        
              with open(file_name, 'wb') as new_file:
                    new_file.write(downloaded_file.read())
              os.rename(file_name, "siteM16.png")
              img = Image.open("siteM16.png")
              width, height = img.size
              full_img = Image.new("RGBA", (width * 2, height * 2))
              overlap = 5 
              full_img.paste(img, (0, 0)) # Верхняя левая (без поворота)
              full_img.paste(img.rotate(270), (width - overlap, 0)) #
              full_img.paste(img.rotate(180), (width - overlap, height - overlap)) # Нижняя правая (поворот на 180 градусов)
              full_img.paste(img.rotate(90), (0, height - overlap)) # Нижняя левая (поворот на 90 градусов)
              full_img.save(f"{file_name}")
              print("Полное изображение прицела сохранено как full_sight.png")
              await message.answer_document(types.InputFile(file_name), caption="Держи свой прицел⚡")
              user = message.from_user.username
              await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")



'''
    if file_name in ["hud_back.png", "hud_center.png", "hud_down.png", "hud_ruble.png", "hud_heart.png", "hud_up.png", "hud_health_scale.png", "hud_menu.png", "hud_armor.png"]:
          await message.answer(f'ваш файл может нарушать структуру программы из-за вашего имени файла\nРекоменждуем сделать 1.{file_name}')
'''




              
          

@dp.message_handler(commands=['listva'])
async def help(message: types.Message):
      await message.answer("Отправь мне листву любого цвета и добавь к ней описание /listva и жди листву ZIP")


@dp.message_handler(commands=['aim'])
async def help(message: types.Message):
      await message.answer("Отправь мне прицел из гта санадрес и добавь к нему описание/aim и я его превращаю в обычный прицел")






dayn = "6646133212"
ADMIN_ID = "6646133212"
ADMIN = "6646133212"
st =('''
Привет ты попал в ToolsBR⚙️
Рекомендуется прочитать документацию
чтобы узнать функции бота /help
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
/road - перекраска всех дорог команда + rgb цвет
/hud - перекраска худа команда + rgb цвет
/aim - переконверт прицела из старого олд движка в стандарт прицел 
/listva - создание листвы файл и описание к нему /listva
'''
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
      await message.answer(hl)



@dp.message_handler(commands=['logo'])
async def help(message: types.Message):
      await message.answer("Отправьте файл и добавьте к нему описание /logo")
      user = message.from_user.username
      await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")


@dp.message_handler(commands=['rgb'])
async def help(message: types.Message):
      await message.answer("Отправьте файл и добавьте к нему описание /rgb *ваш rgb цвет* пример👇")
      await message.answer_document(types.InputFile("test/ex.png"), caption="/rgb 0, 255, 0")
      user = message.from_user.username
      await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")


@dp.message_handler(commands=['bildboard'])
async def help(message: types.Message):
      await message.answer("Отправьте ваш файл btx и добавьте к нему описание /bildboard и вы получите свои билборды с нужными именами в ZIP ")
      user = message.from_user.username
      await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
      

@dp.message_handler(commands=['send'])
async def send_message(message: types.Message):
    try:
        # Разделяем сообщение по пробелам
        command, user_id, *text = message.text.split()
        text_message = ' '.join(text)

        # Преобразуем user_id к int
        user_id = int(user_id)

        # Отправляем сообщение пользователю
        await bot.send_message(user_id, f"сообщения от администратора : >> {text_message}")
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

'''
@dp.message_handler(commands=("bloodOLD"))
async def blood(message: types.Message):
    color = message.text.lstrip('/bloodOLD #')
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
    code = token_hex(3)
    grn1 = f'ids.{code}_particle.cfg'
    with open('debug/parta.cfg', 'r') as file:
        data = file.read()
        data = data.replace("r22", str(rgb[0])).replace("g22", str(rgb[1])).replace("b22", str(rgb[2]))
    with open(grn1, 'w') as file:
        file.write(data)
        await message.reply_document(types.InputFile(grn1), caption="Держи свой particle⚡")
        user = message.from_user.username
        await bot.send_message(ADMIN_ID, f"Пользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")
'''







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
       url_button = types.InlineKeyboardButton(text="Наш канал🦴", url="https://t.me//Madimodzs")
       
    #   u = types.InlineKeyboardButton(text="📃Документация", web_app=WebAppInfo(url="https://teletype"))
       kb.row(url_button)
       
       
       k = types.InlineKeyboardMarkup()
       url_butto = types.InlineKeyboardButton(text="Документация🧾", url="teletype.in/@timka_lxz/atlYG7SpCC0")
       url_button = types.InlineKeyboardButton(text="Наш канал🦴", url="https://t.me//Madimodzs")
       
    #   u = types.InlineKeyboardButton(text="📃Документация", web_app=WebAppInfo(url="https://teletype"))
       k.row(url_button, url_butto)
       
       
       welcome_message = await message.answer("подпишись на наш канал", reply_markup=kb)
      # time.sleep(3)
     #  await message.reply("Проверка может занять от 10секунд до минуты")
       
       
       time.sleep(5)
       await bot.edit_message_text("Спасибо за подписку🦾", chat_id=message.chat.id, message_id=welcome_message.message_id)
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
    
    code = token_hex(3)
    print(f"{code}_timecyc.json")
    random_name = message.from_user.username
    grn1 = f"ids.{code}_timecyc.json"
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
    code = token_hex(3)
    print(f"{code}_timecyc.json")
    grn1 = f"ids.{code}_colorcycle.dat"
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
        
        if PT.is_integer():
              PT = int(PT)
        
        

        with open("weapon.isx", "r") as file:
            dg = file.read()
            dg = dg.replace("ПТ", str(PT))
            dg = dg.replace("RAZB", str(RAZB))
            random_name = message.from_user.username
            code = token_hex(3)
            print(f"{code}_timecyc.json")
            eix = f"ids.{code}_weapon.dat"
        with open(eix, "w") as file:
           file.write(dg)
        
        
        await message.answer_document(types.InputFile(eix), caption = f"держи свой weapon⚡\nКоличество патрон в магазине: {PT}\nРазброс патрон: {RAZB}")
        await bot.send_message(ADMIN_ID, f" GIVE ВЕАП\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{message.from_user.username} \nДействие: {message.text} \nДата: {message.date} ")
    except Exception as e:
        await message.answer("❌")
        await message.answer("Вы используете что-то кроме чисел\nИСПОЛЬЗУЙТЕ ПО ПРИМЕРУ НИЖЕ\n /deagle количество пт в магазине,разброс пт\nПолноценный пример👇")
        await message.reply("/deagle 9,1")
        await message.reply(e)
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
        await bot.send_message(ADMIN_ID, f"MSG\nПользователь: {message.from_user.first_name} \nПрофиль: tg://openmessage?user_id={message.from_user.id} \nЮзер: @{user} \nДействие: {message.text} \nДата: {message.date} ")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)