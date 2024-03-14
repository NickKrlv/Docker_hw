from django.core.exceptions import ValidationError


class Char_validate_youtube_link:
    def __call__(self, value):
        if not value.startswith('https://www.youtube.com/watch?v='):
            raise ValidationError('The link should start with "https://www.youtube.com/watch?v=')
        return value
