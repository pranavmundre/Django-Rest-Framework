from django.core.exceptions import ValidationError


def only_int(val):
    if not val.isdigit():
        raise ValidationError('Only integer accepted.')
