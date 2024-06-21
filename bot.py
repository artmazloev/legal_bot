import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import handle_document, handle_text

# Настройка логирования для проверки
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# Функция для обработки команды /start
def start(update: Update, context):
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Привет, {user.mention_markdown_v2()}! Я бот для проверки юридических документов. '
        'Отправьте мне документ, и я проверю его на корректность.'
    )


def main():
    # Заменить 'YOUR_BOT_TOKEN' на актуальный токен для нашего бота
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, handle_document))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
