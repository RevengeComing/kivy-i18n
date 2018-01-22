from pyharfbuzz import shape
from pyfribidi import log2vis

__all__ = ('reshape_text', )

def simple_render(text):
    result = log2vis(text)
    return result

def get_extends(font_name ,text):
    result = log2vis(text)
    result = shape(font_name, text)
    return result
