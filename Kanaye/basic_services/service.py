from django.core.exceptions import ValidationError


def get_path_upload_track_cover(instance, file):
    return f'track_cover/{file}'


def get_path_upload_track_file(instance, file):
    return f'track/{file}'


def get_path_upload_album(instance, file):
    return f'album/{file}'


def get_path_upload_user(instance, file):
    return f'users/{file}'


def validate_size_image(file_obj):
    max_size = 2
    if file_obj.size > max_size * 1024 * 1024:
        return ValidationError(f'Максимальный размер файла {max_size}')