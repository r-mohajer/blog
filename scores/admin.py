from django.contrib import admin
from scores.models import Score


@admin.register(Score)
class Post(admin.ModelAdmin):
    list_display = (
        "post",
        "user",
        "score_number",
        "created_at",
        "updated_at",
    )
