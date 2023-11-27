

# Create your views here.
 



from django.shortcuts import render
from django.http import JsonResponse
from .models import Conversation

def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')
        
        # Process user message using a chatbot engine (implement this part)
        bot_response = process_user_message(user_message)
        
        # Save the conversation to the database
        Conversation.objects.create(user_message=user_message, bot_response=bot_response)

        return JsonResponse({'bot_response': bot_response})

    return render(request, 'chatapp/chat.html')
