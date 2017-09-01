from django.contrib import admin

# Register your models here.
from .models import MsgPost
class MsgPostAdmin(admin.ModelAdmin):
	list_display=('pk','content','datetime')
admin.site.register(MsgPost,MsgPostAdmin)
