from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post,Review,Category

class PostAdmin(SummernoteModelAdmin):
    list_display=['user','title','publish_date']
    search_fields=['user','content']
    list_filter=['publish_date','category']

    summernote_fields = ('content',)


admin.site.register(Post,PostAdmin)
admin.site.register(Review)
admin.site.register(Category)

