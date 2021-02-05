import inspect
import pkgutil
import importlib
import sys


def import_models():
    this_module = sys.modules[__name__]

    for loader, module_name, is_pkg in pkgutil.iter_modules(
            this_module.__path__, this_module.__name__ + '.'):
        module = importlib.import_module(module_name, loader.path)
        for name, _object in inspect.getmembers(module, inspect.isclass):
            globals()[name] = _object


import_models()
