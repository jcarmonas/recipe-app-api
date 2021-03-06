from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(**args):
    '''Create a sample user'''
    email = 'test@gmail.com'
    password = 'testpassword.'
    return get_user_model().objects.create_user(email, password)
    
class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@gmail.com'
        password = 'testpass123.'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())
        
    def test_new_user_invalid_email(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError): # This checks if an error is raised, if it isn't the test fails.
            get_user_model().objects.create_user(None, 'test123')
            
    def test_create_new_superuser(self):
        '''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123.'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
    def test_tag_str(self):
        ''' '''
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )        
        self.assertEqual(str(tag), tag.name)