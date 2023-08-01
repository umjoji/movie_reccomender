from django.test import TestCase
from movierecommender.models import Movie

# Create your tests here.
class MovieTestCase(TestCase):

    def setUp(self):
        Movie.objects.create(original_title="Eye of the Tiger")


    # python manage.py test movierecommender.tests.MovieTestCase
    # ./manage.py test
    def test_movies(self):
        john = Movie.objects.get(original_title="Eye of the Tiger")
        print(john)



