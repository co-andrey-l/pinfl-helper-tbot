import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pinfl_utilities_parser import PinflUtilitiesParser

def start(update, context):
    update.message.reply_text(
        "Привет! Отправь мне PINFL для анализа и я скажу валидный он или нет.\n" \
        "Тут все честно, я не сохраняю никаких данных о тебе или о том, что ты пишешь."
        )

def echo(update, context):
    pinfl_text = update.message.text.strip()

    if pinfl_text.isdigit() and len(pinfl_text) >= 14:
        parser = PinflUtilitiesParser(pinfl_text)

        if parser.is_valid():
            response = f"PINFL действителен.\nДата рождения: {parser.birth_date}"
        else:
            response = "Неверный PINFL. Проверьте следующие ошибки:\n"
            if not parser.is_valid_date():
                response += "- Неправильная дата.\n"
            if not parser.validate_check_digit():
                correct_check_digit = parser.calculate_check_digit()
                response += f"- Неправильная контрольная цифра. Правильная контрольная цифра: {correct_check_digit}\n"
            if not parser.validate_area_code():
                response += "- Неправильный код региона.\n"
            if not parser.validate_citizen_serial_number():
                response += "- Неправильный серийный номер гражданина.\n"
    else:
        response = "Неверный PINFL. Проверьте, что он содержит только цифры и имеет длину не менее 14 символов."

    update.message.reply_text(response)

def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    print(f"bot launched successfully")

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
