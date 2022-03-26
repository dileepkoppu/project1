from django.contrib import admin
from .models import kid,image
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    readonly_fields=('updated_at','thumbnail_preview')
    radio_fields={'food_group':admin.HORIZONTAL}

    
    def thumbnail_preview(self, obj):
        print(obj.thumbnail_preview,'@@@@@@@@@@@@@@@@@@@@')
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(kid)
admin.site.register(image,MyModelAdmin)
