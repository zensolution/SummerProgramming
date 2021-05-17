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
 
## Equality and Types

### VARIABLE TYPES

  ````
   var is20 = false;
   console.log(typeof is20); // boolean
   
   var age = 16; 
   console.log(typeof age); // number
    
   var lastName = "Bae"; 
   console.log(typeof lastName); // string 
   
   var fruits = ["Apple", "Banana", "Kiwi"];
   console.log(typeof fruits); // object ΩΩ
   
   var me = {firstName:"Sammie", lastName:"Bae"};
   console.log(typeof me); // object    
  ````
