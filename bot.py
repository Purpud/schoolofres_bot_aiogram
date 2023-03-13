import logging
import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Організатори 👤")
    item2 = types.KeyboardButton("Інфо про проєкт ℹ")
    item3 = types.KeyboardButton("Зареєструватися ✍")
    item4 = types.KeyboardButton("Задати запитання ❓")
    markup.add(item1, item2)
    markup.add(item3)

    await bot.send_message(message.chat.id, "Привіт, <b>{0.first_name}</b>!\nХочеш дізнатися більше про локальну школу успіху в Києві?\nВибирай опцію нижче 👇".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(content_types=['text'])
async def answer_reply(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Організатори 👤':
            # Julia Popadina
            await bot.send_photo(message.chat.id, photo=open(
                'assets/participants_compressed/Julia.jpg', 'rb'), caption="⭐ *Юлія Попадіна* ⭐", parse_mode='markdown')
            await bot.send_message(message.chat.id, (
                "Я *Юля*, у квітні святкуватиму 17-ий день народження, люблю котів і творчість Жадана. Організаторка проєкту \"School of Resilience Kyiv\"\n"
                "Цього року стала випускницею проєкту \"School of Resilience\", що подарував 10 неймовірних днів у сонячному місті Гайдельберг.\n"
                "Нетворкінг, який ми отримали на проєкті, а також навички і знання, без яких ну просто ніяк у мінливому сучасному світі, були просто неоціненними! "), parse_mode='markdown')

            # Denis Budnichenko
            await bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Den.jpg',
                                                             'rb'), caption="⭐ *Денис Будниченко* ⭐", parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Привіт, я *Денис*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

            # Kamila Shaga
            await bot.send_photo(message.chat.id, photo=open(
                'assets/participants_compressed/Kamila.jpg', 'rb'), caption="⭐ *Каміла Шага* ⭐", parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Привіт, я *Каміла*, випускниця проєкту \"Shool of Resilience\" та організаторка проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

            # Margo Vovchek
            await bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Margo.jpg',
                                                             'rb'), caption="⭐ *Маргарита Вовчек* ⭐", parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Привіт, я *Марго*, випускниця проєкту \"Shool of Resilience\" та організаторка проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

            # Max Pinchuk
            await bot.send_photo(message.chat.id, photo=open(
                'assets/participants_compressed/Max.jpg', 'rb'), caption="⭐ *Максим Пінчук* ⭐", parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Привіт, я *Макс*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

            # Nazar Slabliuk
            await bot.send_photo(message.chat.id, photo=open(
                'assets/participants_compressed/Nazar.jpg', 'rb'), caption="⭐ *Назар Слаблюк* ⭐", parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Привіт, я *Назар*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

            # Sonia Kuchinska
            await bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Sonia.jpg',
                                                             'rb'), caption="⭐ *Софія Кучинська* ⭐", parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Привіт, я *Соня*, випускниця проєкту \"Shool of Resilience\" та організаторка проєкту \"Shool of Resilience Kyiv\" "), parse_mode='markdown')

            # Eugene Kravchuk
            await bot.send_photo(message.chat.id, photo=open('assets/participants_compressed/Eugene.jpg',
                                                             'rb'), caption="⭐ *Євгеній Кравчук* ⭐", parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Привіт, я *Женя*, випускник проєкту \"Shool of Resilience\" та організатор проєкту \"Shool of Resilience Kyiv\""), parse_mode='markdown')
        elif message.text == 'Інфо про проєкт ℹ':
            await bot.send_message(message.chat.id, ("*На проєкті ти дізнаєшся:*\n\n"
                                                     "• Як заповнити грантову заявку і отримати фінансування на свої найнеймовірніші ідеї? 💡\n"
                                                     "• Як захопити увагу аудиторії, побороти страх і стати майстром публічних виступів? 💬\n"
                                                     "• Як розвинути особистий бренд щоб залишати незабутнє враження скрізь, де вас побачать? 🎯\n\n"), parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Ми впевнені, що багатьох цікавлять ці питання, і гарантуємо: школа стійкості - це місце де ви обов'язково отримаєте відповідь на кожне із них! 😃\n\n"), parse_mode='markdown')
            await bot.send_message(message.chat.id, ("Натхненні власним досвідом, ми приступили до розробки проєкту *\"School of Resilience Kyiv\"*, стати учасником якого вже цієї весни, можеш стати саме ТИ! 🫵\n\n"), parse_mode='markdown')
            await bot.send_message(
                message.chat.id, ("Будьте певні, ми з командою підготували дещо дійсно крутезне! 😎"), parse_mode='markdown')
            await bot.send_message(message.chat.id, ("Щоб зареєструватися переходь за посиланням: <b><a href=\"https://docs.google.com/forms/d/e/1FAIpQLScTNtP9jxucN2n4RMWowc97i41DA16ibRbQp7KIGCF6uAmQVw/viewform\">реєстрація</a></b>"), parse_mode='html')
        elif message.text == 'Зареєструватися ✍':
            await bot.send_message(message.chat.id, "Щоб зареєструватися переходь за посиланням: <b><a href=\"https://docs.google.com/forms/d/e/1FAIpQLScTNtP9jxucN2n4RMWowc97i41DA16ibRbQp7KIGCF6uAmQVw/viewform\">реєстрація</a></b>", parse_mode="html")
        else:
            await bot.send_message(message.chat.id, "Я не знаю, що відповісти")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
