import math

class line:

  __width = 0
  __height = 0
  def __init__(self, width, height):
      self.__width = width
      self.__height = height
  def set_length(self, width, height):
      self.__width = width
      self.__height = height
  def get_length(self):
      return self.__width, self.__height
  def area_square(width, height):
      if width<=0 or height <= 0: raise ValueError
  def area_circle(width, height):
      if width <=0 or height <= 0: raise ValueError
  def area_regular_triangle(width, height):
      if width <=0 or height <=0: raise ValueError
      return width *height/2
  
  