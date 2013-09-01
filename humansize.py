# coding=utf-8
__author__ = 'Giyyan'

SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    if size < 0:
        raise ValueError('Размер файла не может быть отрицательным')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{size:.1f} {suffix}'.format(size=size, suffix=suffix)
    raise ValueError('Число слишком большое')


if __name__ == '__main__':
    print(approximate_size(100000000000, False))
    print(approximate_size(100000000000))
