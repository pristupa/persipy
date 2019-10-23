import inspect

from pyannotations import annotate
from typing import Type


def entity(cls: Type):
    if not inspect.isclass(cls):
        raise TypeError('Only classes can be annotated as entities')
    return annotate('persipy.entity')(cls)
