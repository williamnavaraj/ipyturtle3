#!/usr/bin/env python
# coding: utf-8

# Copyright (c) William Navaraj.
# Distributed under Apache 2.0 license
"""
ipyturtle3.

ipython turtle which runs in jupyter lab/vscode. 
This was developed as ipyturtle and ipyturtle2 was found to run only on classic jupyter notebook
"""
from .ipyturtle3 import Turtle, Canvas, TurtleScreen,hold_canvas

__version__ = "0.1.0"
__author__ = 'William Navaraj'
__homepage__ = 'https://github.com/williamnavaraj'
__all__ =['Turtle','Canvas','TurtleScreen','hold_canvas']