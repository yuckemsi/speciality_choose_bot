from app.handlers import bot

def main():
    bot.polling(non_stop=True)

if __name__ == '__main__':
    main()