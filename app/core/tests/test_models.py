from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email """
        email = "test@aqurds.com"
        password = "aqurds123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        """Test if the email is normalized or not"""
        email = "test@AQURDS.COM"
        password = "aqurds123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_email_validation_for_user(self):
        """Test will validate user email.
        None is not allowed and will raise ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "aqurds123")

    def test_create_super_user(self):
        """Test creating a new super user with email"""
        email = "super_user@aqurds.com"
        password = "super_user_123"
        super_user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
