import requests
from django.shortcuts import render
from django.views import View

from chatgpt_integration.settings import API_KEY


# Create your views here.
class ChatView(View):
    """
    View for handling chat interactions with ChatGPT.
    """
    template_name: str = 'chat.html'

    def get(self, request) -> render:
        """
        Handle GET request and render the chat template.
        """
        return render(request, self.template_name)

    def post(self, request) -> render:
        """
        Handle POST request with user's question and generate chatbot response.
        """
        question = request.POST['question']
        response = self.get_chatbot_response(question)
        return render(request, self.template_name, {'response': response})

    def get_chatbot_response(self, question: str) -> str:
        """
        Get the response from the ChatGPT API for the given question.
        """
        api_key = API_KEY
        url = 'https://api.openai.com/v1/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        data = {
            'model': "text-davinci-003",
            'prompt': question,
            'max_tokens': 50
        }
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        return response_json['choices'][0]['text']
