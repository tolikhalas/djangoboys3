import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('Назва статті', max_length=200)
    article_text = models.TextField('Текст статті')
    pub_date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def num_of_comments(self):
        return self.set_comment.count()

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Ім'я автора", max_length=50)
    comment_text = models.CharField('Текст коментару', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"