from django.test import TestCase
from .models import Editor,Article,Tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.maryann = Editor(first_name = 'Maryann',last_name='Mwikali',email = 'mwikali119@gmail.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.maryann,Editor))
    #Testing Save Method
    def test_save_method(self):
        self.maryann.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
    # #Testing delete method
    # def test_delete_method(self):
    #     self.maryann.delete_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors)>0)

class TagsTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.tags = Tags(name='me')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tags,Tags))
    #Testing Save Method
    def test_save_method(self):
        self.tags.save_tags()
        tags = Tags.objects.all()
        self.assertTrue(len(tags)>0)
    #Testing delete method
    # def test_delete_method(self):
    #     self.tags.delete_tags()
    #     tags = Tags.objects.all()
    #     self.assertTrue(len(tags)>0)

class ArticleTestClass(TestCase):
    #Creating a new editor and saving it
    def setUp(self):
        self.maryann = Editor(first_name = 'Maryann',last_name='Mwikali',email = 'mwikali119@gmail.com')
        self.maryann.save_editor()
    #Creating a new tag 
    def setUp(self):
        self.new_tag = Tags(name = 'Test' )
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.maryann)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) == 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    