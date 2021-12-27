from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
class ModelTestCase(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with email"""
        email = 'test@test.com'
        password = 'strongP@ssw0rd'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized"""
        email = 'test@BHINNEKA.COM'
        user = get_user_model().objects.create_user(
            email=email, password='Test!23'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test!23')

    def test_create_new_superuser(self):
        """test creating a new user super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com', 'Test!23'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)