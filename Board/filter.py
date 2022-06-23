from django_filters import FilterSet, DateTimeFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):
    date_create = DateTimeFromToRangeFilter()

    class Meta:
        model = Post
        # fields = ["date_create"]
        fields = {
            "title": ["icontains"],
            "text": ["icontains"],
        }
