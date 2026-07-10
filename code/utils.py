import re

def is_valid_url(url):
    """
    Checks if URL format is valid.
    """

    pattern = re.compile(
        r'^(https?:\/\/)?'
        r'([a-zA-Z0-9.-]+)\.'
        r'([a-zA-Z]{2,6})'
        r'(\/\S*)?$'
    )
