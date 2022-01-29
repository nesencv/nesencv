

import ast
import json
import os
import glob
import sys
import requests
import inspect

def load_module(file_path, module_name=None):
    """
    Load a module by name and search path
    This function should work with python 2.7 and 3.x
    Returns None if Module could not be loaded.
    """
    if module_name is None:
        module_name = os.path.basename(os.path.splitext(file_path)[0])
    if sys.version_info >= (3, 5,):
        import importlib.util

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if not spec:
            return

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    else:
        import imp
        mod = imp.load_source(module_name, file_path)
        return mod