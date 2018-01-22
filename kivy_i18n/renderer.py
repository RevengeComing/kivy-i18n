from pyharfbuzz import shape
from pyfribidi import log2vis

__all__ = ('reshape_text', )

def simple_render(text):
    result = log2vis(text)
    return result

def get_extents(font_name ,text, font_size):
    result = log2vis(text)
    result = shape(font_name, text, font_size)
    x_advance = sum([char['x_advance'] for char in result])
    y_advance = 0
    return x_advance, y_advance
