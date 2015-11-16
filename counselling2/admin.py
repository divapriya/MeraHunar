from django.contrib import admin
from .models import User_Details,Organization_Details,Individual_Details,Comment_Organization,Comment_Individual,Ranking_Organization,Ranking_Individual


admin.site.register(User_Details)
admin.site.register(Organization_Details)
admin.site.register(Individual_Details)
admin.site.register(Comment_Organization)
admin.site.register(Comment_Individual)
admin.site.register(Ranking_Organization)
admin.site.register(Ranking_Individual)
# Register your models here.
