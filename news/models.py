from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()
    def delete_editor(self):
        my_obj = Editor.objects.get(pk = id(1))
        self.delete(my_obj)
    def update_editor(self):
        self.update()

    class Meta:
        ordering = ['first_name']

class Tags(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    def save_tags(self):
        self.save()
    def delete_tags(self):
        my_obj = Tags.objects.get(name = 'me')
        self.delete(my_obj)
    def update_tags(self):
        self.update()

class Article(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField()
    editor = models.ForeignKey('Editor',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/',default = 'SOME STRING')

    def __str__(self):
        return self.title
    def save_article(self):
        self.save()
    def delete_article(self):
        my_obj = Article.objects.get(title = 'Beautiful')
        self.delete(my_obj)
    def update_tags(self):
        self.update()

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news