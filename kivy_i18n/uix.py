__all__ = ('Label', 'Button', 'TextInput')

import os
import inspect

from kivy.cache import Cache
from kivy.properties import StringProperty

from kivy.graphics.texture import Texture

from kivy.uix.label import Label as UIXLabel
from kivy.uix.button import Button as UIXButton
from kivy.uix.textinput import TextInput as UIXTextInput

from kivy.core.text import Label as CoreLabel
from kivy.core.text.markup import MarkupLabel as CoreMarkupLabel

from .renderer import simple_render, get_extents

DEFAULT_FONT = os.path.join(
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),
    "Vazir.ttf"    
)

Cache_get = Cache.get
Cache_append = Cache.append

class Label(UIXLabel):
    font_name = StringProperty(DEFAULT_FONT)

    def _create_label(self):
        if self._label is not None:
            cls = self._label.__class__
        else:
            cls = None
        markup = self.markup
        if (markup and cls is not CoreMarkupLabel) or \
           (not markup and cls is not CoreLabel):

            d = Label._font_properties
            dkw = dict(list(zip(d, [getattr(self, x) for x in d])))

            if dkw.get('text'):
                reshaped = simple_render(dkw.get('text'))
                # dkw['text'] = ''.join([char['char'] for char in reshaped])
                dkw['text'] = reshaped

            if markup:
                self._label = CoreMarkupLabel(**dkw)
            else:
                self._label = CoreLabel(**dkw)

    def _trigger_texture_update(self, name=None, source=None, value=None):
        if name == 'markup':
            self._create_label()
        if source:
            if name == 'text':
                self._label.text = value
            elif name == 'text_size':
                self._label.usersize = value
            elif name == 'font_size':
                self._label.options[name] = value
            elif name == 'disabled_color' and self.disabled:
                self._label.options['color'] = value
            elif name == 'disabled_outline_color' and self.disabled:
                self._label.options['outline_color'] = value
            elif name == 'disabled':
                self._label.options['color'] = self.disabled_color if value \
                    else self.color
                self._label.options['outline_color'] = (
                    self.disabled_outline_color if value else
                    self.outline_color)
            else:
                self._label.options[name] = value
        self._trigger_texture()


class Button(UIXButton, Label):
    pass

class TextInput(UIXTextInput):

    font_name = StringProperty(DEFAULT_FONT)

    def _create_line_label(self, text, hint=False):
        # Create a label from a text, using line options
        text = simple_render(text)
        return super(TextInput, self)._create_line_label(text, hint)

    def _get_text_width(self, text, tab_width, _label_cached):
        # Return the width of a text, according to the current line options
        kw = self._get_line_options()

        try:
            cid = u'{}\0{}\0{}'.format(text, self.password, kw)
        except UnicodeDecodeError:
            cid = '{}\0{}\0{}'.format(text, self.password, kw)

        width = Cache_get('textinput.width', cid)
        if width:
            return width
        if not _label_cached:
            _label_cached = self._label_cached
        text = text.replace('\t', ' ' * tab_width)
        if not self.password:
            width = get_extents(self.font_name, text, self.font_size)[0]
        else:
            width = _label_cached.get_extents()[0]
        Cache_append('textinput.width', cid, width)
        return width
