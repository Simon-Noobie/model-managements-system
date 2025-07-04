from django.test import TestCase
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

def test_template(request):
    return render(request, 'login.html')
# Create your tests here.

class LoginViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')
