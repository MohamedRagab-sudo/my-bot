import telebot
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

answers = {
  "ازيك": "الحمدلله، انت عامل ايه؟ اسألني اي سؤال",
  "ما هو المتغير": "المتغير هو مكان بنخزن فيه قيمة، زي let x = 5"
}

@bot.message_handler(func=lambda m: True)
def reply(message):
    q = message.text.strip()
    ans = answers.get(q, "لسه مش عارف اجابة السؤال ده، جرب تسأل بطريقة تانية")
    bot.reply_to(message, ans)

print("البوت شغال...")
bot.polling()
