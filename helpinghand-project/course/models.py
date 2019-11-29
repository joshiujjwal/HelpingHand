from django.db import models
from django.utils.html import escape, mark_safe



# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    course_syllabus = models.FileField()
    overview = models.CharField(max_length=200,default ='')
    videos= models.FileField(default='')
    quiz = models.FileField(default='')
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)



