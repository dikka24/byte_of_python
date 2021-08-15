from mymodule import sayhi, __version__

sayhi()
print('версия', __version__)

'''Вы могли бы также использовать:
from mymodule import *
Это импортирует все публичные имена, такие какsayhi, но не импортирует__version__,
потому что оно начинается с двойного подчёркивания'''