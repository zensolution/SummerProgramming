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
1. Add Unit and get Metric Volume

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
    
## Example of Object Oriented Programming

1. Calculate the volume of a Box

        ````
        class Box:
          def __init__(self, width, length, height):
            self.length = length
            self.width = width
            self.height = height

          def getVolume(self):  
              return self.height * self.width * self.length

        box = Box(10, 20, 20)
        volume = box.getVolume()
        ````
        
1. Add Big Box and Small Box

        ````
        class Box:
          def __init__(self, width, length, height):
            self.length = length
            self.width = width
            self.height = height

          def getVolume(self):  
              return self.height * self.width * self.length

        smallBox = Box(10, 20, 20)
        volume = smallBox.getVolume()

        bigBox = Box(100, 200, 200)
        volume = bigBox.getVolume()
        ````
        
1. Add Validation

        ````
        class Box:
          def __init__(self, width, length, height):
            if length <= 0 and wdith <= 0 and height <= 0:
              raise Exception("Invalid parameter")
            self.length = length
            self.width = width
            self.height = height

          def getVolume(self):  
              return self.height * self.width * self.length

        smallBox = Box(10, 20, 20)
        volume = smallBox.getVolume()

        bigBox = Box(100, 200, 200)
        volume = bigBox.getVolume()
        ````
        
1. Add Unit and get Metric Volume

        ````
        class Box:
          def __init__(self, width, length, height, unit):
            if length <= 0 and wdith <= 0 and height <= 0:
              raise Exception("Invalid parameter")
            self.length = length
            self.width = width
            self.height = height
            self.unit = unit

          def getVolume(self):  
              return self.height * self.width * self.length

          def getMetricVolume(self):
            volume = getVolume(self)
            if self.unit == "inch":
              return volume * (2.54 ** 3)
            else:
              return volume  

        smallBox = Box(10, 20, 20, "inch")
        volume = smallBox.getMetricVolume()

        bigBox = Box(100, 200, 200, "cm")
        volume = bigBox.getMetricVolume()
        ````
       
