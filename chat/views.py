import requests
from django.shortcuts import render
from django.views import View

from chatgpt_integration.settings import API_KEY


# Create your views here.
class ChatView(View):
    template_name = 'chat.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        question = request.POST['question']
        response = self.get_chatbot_response(question)
        return render(request, self.template_name, {'response': response})

    def get_chatbot_response(self, question):
        api_key = API_KEY
        url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        data = {
            'prompt': question,
            'max_tokens': 50
        }
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        return response_json['choices'][0]['text']
