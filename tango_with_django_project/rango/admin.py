from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    def __unicode__(self):
        return self.name


admin.site.register(Page, PageAdmin)
