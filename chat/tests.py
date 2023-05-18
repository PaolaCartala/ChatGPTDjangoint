from django.test import TestCase, Client
from django.urls import reverse

from chat.views import ChatView


# Create your tests here.
class ChatViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_request_returns_form(self):
        response = self.client.get(reverse('chat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')

    def test_post_request_with_question_returns_response(self):
        question = 'What is the capital of France?'
        response_text = 'The capital of France is Paris.'

        response = self.client.post(reverse('chat'), {'question': question})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')
        self.assertContains(response, response_text)

    def test_post_request_without_question_returns_form(self):
        response = self.client.post(reverse('chat'), {})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')
        self.assertNotContains(response, 'Answer:')

    def test_chatbot_response(self):
        question = 'What is the weather today?'
        expected_response = 'The weather today is sunny.'

        view = ChatView()
        response = view.get_chatbot_response(question)
        self.assertEqual(response, expected_response)
