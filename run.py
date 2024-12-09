#!python

import importlib
import sys

module_name = sys.argv[1]
input = sys.argv[2]

with open(f"{module_name}.{input}", 'r') as file:
    lines = file.readlines()

module = importlib.import_module(module_name)

module.run(module.parse(lines))
