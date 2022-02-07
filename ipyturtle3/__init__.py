#!/usr/bin/env python
# coding: utf-8

# Copyright (c) William Navaraj.
# Distributed under Apache 2.0 license
"""
ipyturtle3.
Turtle graphics based on ipycanvas which can run on jupyter lab/vscode. 
ipyturtle and ipyturtle2 was found to run only on classic jupyter notebook. 
This was developed to solve this.
"""
from .ipyturtle3 import Turtle, Canvas, TurtleScreen,hold_canvas, Shape

__version__ = "0.1.1"
__author__ = 'William Navaraj'
__homepage__ = 'https://github.com/williamnavaraj'
__all__ =['Turtle','Canvas','TurtleScreen','hold_canvas','Shape']