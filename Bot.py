from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Список username, з якими бот працює
allowed_users = ["Mig29_pilot"]  # Додайте username без @

# Функція обробки команди /start
def start(update: Update, context: CallbackContext):
    username = update.effective_user.username  # Отримуємо username користувача
    
    if username in allowed_users:
        message = f"Привіт, {username}! Ви маєте доступ до цього бота."
    else:
        message = f"Вибачте, {username or 'аноніме'}, у вас немає доступу до бота."
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    # Введіть ваш токен
    updater = Updater("7797680757:AAE54hkJbN4A_bY9WUDGKeJ5O7bCz02B9-w")
    
    # Реєстрація команди /start
    updater.dispatcher.add_handler(CommandHandler("start", start))
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()