from django.contrib import admin

from .models import News, Subscribe, Contact


class MemberAdmin(admin.ModelAdmin):
    list_display = ("title", "tag", "category", "date")


admin.site.register(News, MemberAdmin)
admin.site.register(Subscribe)
admin.site.register(Contact)
