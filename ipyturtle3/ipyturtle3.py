#!/usr/bin/env python
# coding: utf-8
#
# ipyturtle3.py: an ipycanvas based turtle graphics module for Python
# implemented as wrapper around turtle.py which ships with python
# Version 0.1.0 - 14. 1. 2022
#
# Copyright [2022] [William Navaraj]

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from cmath import nan
import turtle
import time
import sys
from turtle import _CFG, Shape
import ipycanvas
from ipycanvas import hold_canvas
import webcolors
import copy
class Turtle(turtle.Turtle):
    def __init__(self, screen,
                 shape=_CFG["shape"],
                 undobuffersize=_CFG["undobuffersize"],
                 visible=_CFG["visible"], isHolonomic=False):
        Turtle._screen = screen
        turtle.RawTurtle.__init__(self, Turtle._screen,
                           shape=shape,
                           undobuffersize=undobuffersize,
                           visible=visible)
        self.isHolonomic=isHolonomic
    #Holonomic mode
    def moveup(self, distance):
        if(self.isHolonomic):
            """move turtle up by specified distance"""
            ende = self._position + self._orient.rotate(90) * distance
            self._goto(ende)
        else:
            print("moveup: only for holonomic robot")

    def movedown(self, distance):
        if(self.isHolonomic):
            """move turtle down by specified distance"""
            ende = self._position + self._orient.rotate(-90) * distance
            self._goto(ende)
        else:
            print("movedown: only for holonomic robot")
    def distance_at_angle(self,distance,angle):
        if(self.isHolonomic):
            """move turtle by specified distance and angle"""
            ende = self._position + self._orient.rotate(angle) * distance
            self._goto(ende)
        else:
            print("Distance_at_angle is compatible with only holonomic robots")


    def moveleft(self,distanceOrAngle):
        if(self.isHolonomic):
            """move turtle left by specified distance"""
            ende = self._position + self._orient * -distanceOrAngle
            self._goto(ende)
        else:
            print("moveleft: only for holonomic robot")

    def moveright(self,distanceOrAngle):
        if(self.isHolonomic):
            """move turtle forward by specified distance"""
            ende = self._position + self._orient * distanceOrAngle
            self._goto(ende)
        else:
            print("moveright: only for holonomic robot")


    def turnleft(self,angle):
        # same for both holonomic and nonholonomic
        super().left(angle)

    def turnright(self,angle):
        #same for both holonomic and non-holonomic
        super().right(angle)

    def turn(self,angle):
        #same for both holonomic and non-holonomic
        super().right(angle)

class Canvas(ipycanvas.Canvas):
    #TODO: setting width, height
    def __init__(self, width=500,height=300):
        super().__init__(size=[width,height])
        self.canvwidth=0
        self.canvheight=0
        self.scrollregion=None
        self.canvas_objects=[]

        self.object_id=1
        self.background_color='white'
        self.canvas_objects.append({"ID":0,"BackgroundColor":self.background_color})


    def cget(self,what="width"):
        (self.canvwidth,self.canvheight)=self.size
        if what=="width":
            return self.canvwidth
        elif what=="height":
            return self.canvheight

        elif what=="bg":
            return self.background_color
        else:
            return nan

    def config(self,scrollregion=None):
        if(not scrollregion is None):
            self.scrollregion=scrollregion

    def delete(self, what):
        if what=="all":
            self.canvas_objects=[]
            self.background_color='white'
            self.canvas_objects.append({"ID":0,"BackgroundColor":self.background_color,"Type":"BG"})
        else:
            for i in self.canvas_objects:
                if(i["ID"]==what):
                    self.canvas_objects.remove(i)

    def clear(self):
        """Clear the entire canvas. This is the same as calling ``clear_rect(0, 0, canvas.width, canvas.height)``."""
        self.canvas_objects=[]
        self.background_color='white'
        self.canvas_objects.append({"ID":0,"BackgroundColor":self.background_color,"Type":"BG"})
        super().clear()
            
    def create_image(self, x, y,image_file_name):
        from ipywidgets import Image
        isNull=True
        img=None
        if(image_file_name!=""):     
            img=Image.from_file(image_file_name)
            isNull=False
        self.object_id=self.object_id+1
        self.canvas_objects.append({"ID":self.object_id,"Type":"Image","Image":img,"XPos":x,"YPos":y,"isNull":isNull})
        return self.object_id

    def create_line(self,a=0, b=0, c=0, d=0, fill="", width=2,
                                   capstyle = "ROUND"):
        self.object_id=self.object_id+1
        self.canvas_objects.append({"ID":self.object_id,"Type":"Line","LineSegments":[a,b,c,d],"Fill":fill,"Width":width})
        return self.object_id
    def create_polygon(self,pg, fill="", width=2,
                                   capstyle = "ROUND",outline=""):
        self.object_id=self.object_id+1
        self.canvas_objects.append({"ID":self.object_id,"Type":"Polygon","Polygon":pg,"Fill":fill,"Width":width,"Outline":outline,"Top":False})
        return self.object_id
    def after(self,ms):

        time.sleep(ms*0.001)
    def coords(self,pg_item,*coords_list):
        for i in self.canvas_objects:
            if i["ID"]==pg_item and i["Type"]=="Polygon":
                i["Polygon"]=copy.deepcopy([*coords_list])
                return i["Polygon"]
            elif i["ID"]==pg_item and i["Type"]=="Line":
                i["LineSegments"]=copy.deepcopy([*coords_list])
                return i["LineSegments"]
    def itemconfigure(self,pg_item,fill=None,width=None,outline=None):
        for i in self.canvas_objects:
            if i["ID"]==pg_item:
                if(fill is not None):
                    i["Fill"]=fill
                elif(width is not None):
                    i["Width"]=width
                if(outline is not None):
                    i["Outline"]=outline
                break
    def tag_raise(self,pg_item):
        for i in range(len(self.canvas_objects)):
            if self.canvas_objects[i]["ID"]==pg_item:
                a=self.canvas_objects.pop()
                self.canvas_objects.append(a)
                break

        
            

    def winfo_rgb(self, color):
        """Return a tuple of integer RGB values in range(65536) for color in this widget."""

        return(webcolors.name_to_rgb(color))
    def bgcolor(self, color=None):
        """Set canvas' backgroundcolor if color is not None,
        else return backgroundcolor."""
        if color is not None:
            self.background_color=color
            
            self.canvas_objects[0]["BackgroundColor"]=webcolors.name_to_rgb(color)

        return self.background_color


class TurtleScreen(turtle.TurtleScreen):
    """Provide the basic graphics functionality.
       Interface between ipycanvas and turtle.py.

    """


    def __init__(self, cv, mode=_CFG["mode"],
                 colormode=_CFG["colormode"], delay=_CFG["delay"]):        
        self.cv = cv
        w = int(self.cv.cget("width"))
        h = int(self.cv.cget("height"))
        self.cv.config(scrollregion = (-w//2, -h//2, w//2, h//2 ))
        self.canvwidth = w
        self.canvheight = h
        self.xscale = self.yscale = 1.0

        self._shapes = {
                   "arrow" : Shape("polygon", ((-10,0), (10,0), (0,10))),
                  "turtle" : Shape("polygon", ((0,16), (-2,14), (-1,10), (-4,7),
                              (-7,9), (-9,8), (-6,5), (-7,1), (-5,-3), (-8,-6),
                              (-6,-8), (-4,-5), (0,-7), (4,-5), (6,-8), (8,-6),
                              (5,-3), (7,1), (6,5), (9,8), (7,9), (4,7), (1,10),
                              (2,14))),
                  "circle" : Shape("polygon", ((10,0), (9.51,3.09), (8.09,5.88),
                              (5.88,8.09), (3.09,9.51), (0,10), (-3.09,9.51),
                              (-5.88,8.09), (-8.09,5.88), (-9.51,3.09), (-10,0),
                              (-9.51,-3.09), (-8.09,-5.88), (-5.88,-8.09),
                              (-3.09,-9.51), (-0.00,-10.00), (3.09,-9.51),
                              (5.88,-8.09), (8.09,-5.88), (9.51,-3.09))),
                  "square" : Shape("polygon", ((10,-10), (10,10), (-10,10),
                              (-10,-10))),
                "triangle" : Shape("polygon", ((10,-5.77), (0,11.55),
                              (-10,-5.77))),
                  "classic": Shape("polygon", ((0,0),(-5,-9),(0,-7),(5,-9))),
                   "blank" : Shape("image", self._blankimage())
                  }

        self._bgpics = {"nopic" : ""}

        self._mode = mode
        self._delayvalue = delay
        self._colormode = _CFG["colormode"]
        self._keys = []
        self.clear()
        TurtleScreen._RUNNING=True
    def register_shape(self, name, shape=None):
        

        if shape is None:
            # image
            if name.lower().endswith(".gif"):
                #shape = Shape("image", self._image(name))
                raise turtle.TurtleGraphicsError("Image registration: Not implemented for ipython yet")
            else:
                raise turtle.TurtleGraphicsError("Image registration: Not implemented for ipython yet")
                #raise TurtleGraphicsError("Bad arguments for register_shape.\n"
                #                            + "Use  help(register_shape)" )
        elif isinstance(shape, tuple):
            shape = Shape("polygon", shape)
        ## else shape assumed to be Shape-instance
        self._shapes[name] = shape

    def _blankimage(self):
        img=ipycanvas.Canvas.create_image_data(self.cv,1,1)
        return img
    def _image(self):
        img=ipycanvas.Canvas.create_image_data(self.cv,1,1)
        return img
    def clear(self):
        """Delete all drawings and all turtles from the TurtleScreen.

        No argument.

        Reset empty TurtleScreen to its initial state: white background,
        no backgroundimage, no eventbindings and tracing on.

        Example (for a TurtleScreen instance named screen):
        >>> screen.clear()

        Note: this method is not available as function.
        """
        self._delayvalue = _CFG["delay"]
        self._colormode = _CFG["colormode"]
        self._delete("all")
        self._bgpic = self._createimage("")
        self._bgpicname = "nopic"
        self._tracing = 1
        self._updatecounter = 0
        self._turtles = []
        self.bgcolor("white")

        Turtle._pen = None

        self.cv.clear()

    def _incrementudc(self):
        """Increment update counter."""
        if not TurtleScreen._RUNNING:
            TurtleScreen._RUNNING = True
            #raise Terminator
        if self._tracing > 0:
            self._updatecounter += 1
            self._updatecounter %= self._tracing
    def _createline(self):
        """Create an invisible line item on canvas self.cv)
        """
        return self.cv.create_line(0, 0, 0, 0, fill="", width=2,
                                   capstyle = "ROUND") #TK.ROUND


    def _update(self):
        """Redraw graphics items on canvas
           TODO: Multicanvas implementation
        """
        with hold_canvas(self.cv):
            for i in self.cv.canvas_objects:
                if i["ID"]==0:
                    self.cv.fill_style=self.cv.background_color
                    self.cv.fill_rect(0, 0, self.cv.canvwidth, self.cv.canvheight)
                elif i["Type"]=="Polygon":
                    if i['Fill'] !="":
                        self.cv.fill_style=i['Fill']
                    if i['Outline'] != "":
                        self.cv.stroke_style=i['Outline']
                    L=i["Polygon"]
                    pg=[(L[i]+self.cv.canvwidth/2,L[i+1]+self.cv.canvheight/2) for i in range(0, len(L),2)]
                    self.cv.fill_polygon(pg)
                    self.cv.stroke_polygon(pg)
                elif i["Type"]=="Line":
                    if i['Fill'] !="":
                        self.cv.fill_style=i['Fill']
                        self.cv.stroke_style=i['Fill']
                    L=i["LineSegments"]         
                    if (len(L)>=4):
                        pg=[(L[i]+self.cv.canvwidth/2,L[i+1]+self.cv.canvheight/2) for i in range(0, len(L),2)] #[L[0]+self.cv.canvwidth/2,L[1]+self.cv.canvheight/2, L[2]+self.cv.canvwidth/2,L[3]+self.cv.canvheight/2 ]
                        self.cv.stroke_lines(pg)
                elif i["Type"]=="Image":
                    if(i["isNull"]==False):
                        #pass
                        self.cv.draw_image(i["Image"], i["XPos"], i["YPos"])
        self.cv

    def _bgcolor(self, color=None):
        """Set canvas' backgroundcolor if color is not None,
        else return backgroundcolor."""
        if color is not None:
            self.cv.bgcolor(color)
            self._update()
        else:
            return self.cv.cget("bg")

    def _createimage(self, image):
        """Create and return image item on canvas.
        """   
        return self.cv.create_image(0, 0, image_file_name=image)