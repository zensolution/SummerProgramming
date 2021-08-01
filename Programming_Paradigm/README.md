## About this course

1. Programming Paradigm
2. Markdown 

## 道 (Tao) vs 术 (Shu)

道: Used to guide the direction
术: Used to guide the action.

## Programming Paradigm

- Procedural/Structured Programming
- Object Oriented Programming

## Example of Procedure Pragramming

1. Procedure Calculate the volume of a Box

    ````
    def getVolume(width, length, height):
      return width * length * height

    width = 10 
    length = 8 
    height = 6

    volume = getVolume(width, length, height)
    ````
    
1. Add Big Box and Small Box

    ````
    def getVolume(width, length, height):
      return width * length * height

    widthSmall = 10 
    lengthSmall = 8 
    heightSmall = 6

    volumeSmall = getVolume(widthSmall, lengthSmall, heightSmall)

    widthBig = 10 
    lengthBig = 8 
    heightBig = 6

    volumeBig = getVolume(widthBig, lengthBig, heightBig)
    ````
1. Add Validation

    ````
    def getVolume(width, length, height):
      return width * length * height

    widthSmall = 10 
    lengthSmall = 8 
    heightSmall = 6
    if widthSmall <= 0:
       raise ValueError('Width must be greater than zero')
    if lengthSmall <= 0:
       raise ValueError('Length must be greater than zero')
    if heightSmall <= 0:
       raise ValueError('Height must be greater than zero')

    volumeSmall = getVolume(widthSmall, lengthSmall, heightSmall)

    widthBig = 20 
    lengthBig = 28 
    heightBig = 26
    if widthBig <= 0:
       raise ValueError('Width must be greater than zero')
    if lengthBig <= 0:
       raise ValueError('Length must be greater than zero')
    if heightBig <= 0:
       raise ValueError('Height must be greater than zero')

    volumeBig = getVolume(widthBig, lengthBig, heightBig)
    ````
1. Add Unit 

    ````
    def getVolume(width, length, height):
      return width * length * height

    def getMetricVolume(width, length, height, unit):
      volume = getVolume(width, length, width)
      if unit == "inch":
        return volume * (2.54 ** 3)
      else:
        return volume  

    unitSmall = "cm"
    widthSmall = 10 
    lengthSmall = 8 
    heightSmall = 6
    if widthSmall <= 0:
       raise ValueError('Width must be greater than zero')
    if lengthSmall <= 0:
       raise ValueError('Length must be greater than zero')
    if heightSmall <= 0:
       raise ValueError('Height must be greater than zero')

    volumeSmall = getVolume(widthSmall, lengthSmall, heightSmall)
    metricVolumeSmall = getMetricVolume(widthSmall, lengthSmall, heightSmall, unitSmall)

    unitBig = "inch"
    widthBig = 20 
    lengthBig = 28 
    heightBig = 26
    if widthBig <= 0:
       raise ValueError('Width must be greater than zero')
    if lengthBig <= 0:
       raise ValueError('Length must be greater than zero')
    if heightBig <= 0:
       raise ValueError('Height must be greater than zero')

    volumeBig = getVolume(widthBig, lengthBig, heightBig)
    metricVolumeBig = getMetricVolume(widthBig, lengthBig, heightBig, unitBig)
    ````
