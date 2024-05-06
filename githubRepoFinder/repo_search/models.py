from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=200)
    html_url = models.URLField(max_length=200)
    stargazers_count = models.IntegerField(default=0)
    watchers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

