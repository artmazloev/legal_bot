from telegram import Update
# Хендлер для обработки входящих документов


def handle_document(update: Update, context):
    # Возможно здесь опишем логику проверки документа
    update.message.reply_text('Я получил ваш документ. Проверка началась...')
    pass


# Хендлер для обработки текстовых сообщен
def handle_text(update: Update, context):
    update.message.reply_text('Пожалуйста, отправьте документ для проверки.')
    pass
