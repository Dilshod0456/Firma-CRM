from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(Category)
admin.site.register(Fikr)
admin.site.register(Post)

