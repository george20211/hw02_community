from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(max_length=100)
    pub_date = models.DateTimeField("date published",
                                    auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey(
        'Group', on_delete=models.CASCADE, blank=True, null=True)
    list_filter = ('text')


class Group(models.Model):
    title = models.CharField(max_length=200, blank=True, null=False)
    slug = models.SlugField(verbose_name='slug',
                            blank=True, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return self.title
