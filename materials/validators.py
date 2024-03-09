from django.core.exceptions import ValidationError

def validate_youtube_link(value):
    if not value.startswith('https://www.youtube.com/watch?v='):
        raise ValidationError('The link should start with "https://www.youtube.com/watch?v=')
    return value