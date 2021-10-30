from django.db import models
from django.contrib.auth.models import User

COLORS = [
    ('#eeeeee', 'gray'),
    ('#ff0000', 'red'),
    ('#0000ff', 'blue'),
    ('#00ff00', 'green'),
    ('#000000', 'black'),
    ('#ffffff', 'white'),
    ('#7E8F7C', 'khaki'),
]

class Activity(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    phone = models.CharField(verbose_name="Phone", max_length=12)
    date = models.DateField(verbose_name="Date")
    start_time = models.TimeField(verbose_name="Start Time")
    employee = models.CharField(verbose_name="Employee", max_length=50, blank=True, null=True)
    color = models.CharField(verbose_name="Color", max_length=7, choices=COLORS, default="gray")
    private = models.BooleanField(verbose_name="Private", default=False)
    comment = models.TextField(verbose_name="Comment", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    related_activity = models.ManyToManyField('Activity', verbose_name="Related Activities", blank=True)

    def __str__(self):
        return self.title + " " + str(self.start_time) + " " + self.employee

    def save(self, *args, **kwargs):
        if(self.id != None):
            for i in self.related_activity.all():
                i.delete()

        super().save(*args, **kwargs)


    def delete(self, using=None, keep_parents=False):
        # if there are related activities
        if(self.related_activity.count()):
            for i in self.related_activity.all():
                i.delete()
            return super().delete()
        return  super().delete()


    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
