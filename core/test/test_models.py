from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """testing a new user with email"""
        email = "test@gmail.com"
        password = "123456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """testing user email with lower case"""
        email = "demo@GMAIL.COM"
        user = get_user_model().objects.create_user(email, '12345')
        self.assertEqual(user.email, email.lower())
        
    def test_new_user_email_invalid(self):
        """testing for email provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345')

    def test_superuser_created(self):
        """creating superuser test"""
        user = get_user_model().objects.create_superuser(
            'demo@gmail.com',
            'demo1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)