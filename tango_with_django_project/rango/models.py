from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
        
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
        
''' Update the Category model to include the additional attributes, views and likes where the default value is zero. '''


''' Re-sync your database, and update your population script so that the Python category has 128 views and 64 likes, the Django category has 64 views and 32 likes, and the Other Frameworks category has 32 views and 16 likes.

Undertake the part two of official Django tutorial if you have not done so. This will help to reinforce further what you have learnt here, and to learn more about customising the admin interface.

Customise the Admin Interface - so that when you view the Page model it displays in a list the category, the name of the page and the url. '''