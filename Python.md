## First Python Program

  ````
# Calculate the slope in algebra
def calculateSlope(x1, y1, x2, y2):
    if x2 == x1:
      return "NA"
    return (y2-y1)/(x2-x1)

slope = calculateSlope(10, 3, 12, 5)
print(slope)    
  ````
  
## Variable - Every variable is connected to a value

### Scope

1. Local Scope
    ````
    def trial():
        name = "James"

    trial()
    print(name)
    ````
    
1. Global Scope
  
    ````
    def trial():
        print(name)

    name = "James"
    trial()  
    ````

  
3. Nested Scope
 ````
  def trial():
      def nestedFunc():
          nested = "nested"
          print(outer)  
      outer = "outer"
      nestedFunc()
      print(nested)    

  trial()
 ````
 
## VARIABLE TYPES

| Category  |  Type   |  Example  |
|---|---|---|
| Text Type  |  string  | x = "Hello World"  |
| Numeric Type  | int  | x = 20  |
|   | int  | x = 20  |
|   | float  | x = 20.5  |
| Sequence Type  | list  | x = ["apple", "banana", "cherry"]  |
|   | tuple  | x = ("apple", "banana", "cherry")  |
|   | range  | x = range(6)  |
|Mapping Type| dict | x = {"name" : "John", "age" : 36} |
| Set Types  |  set | x = {"apple", "banana", "cherry"} |
| Boolean Type | bool | x = True |
| Binary Type | bytes | x = b"Hello" 	 |
|   | bytearray | x = bytearray(5) |

### Equality

