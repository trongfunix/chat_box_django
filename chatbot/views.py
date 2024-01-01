from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize ChatterBot
chatbot = ChatBot("My ChatterBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def chat_view(request):
    bot_response = ""
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        bot_response = chatbot.get_response(user_input)

    return render(request, 'chat.html', {'bot_response': str(bot_response)})
