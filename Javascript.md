## First Javascript Program

  ````
  var slope = calculateSlope(10, 3, 12, 5)
  console.log(slope)

  // Calculate the slope in algebra?
  function calculateSlope(x1, y1, x2, y2) {
     if (x2 == x1) {
        return "NA"
     }
     return (y2-y1)/(x2-x1)
  }
  ````
  
## Variable - we use variable to store things

1. DECLARATION WITH LET: BLOCK SCOPE

  **let** keyword can be used to declare a variable. Any variables declared this way are in the closest block scope (meaning within the {} they were declared in).
  
  ````
  trial(true)

  function trial(print) {
    if ( print ) {
      let job = "painter"
      console.log(job)
    }
    console.log(job)
  }
  ````
2. DECLARATION WITH VAR: FUNCTIONAL SCOPE

  **var** is one keyword used to declare variables. These variable declarations “float” all the way to the top
  
  ````
  trial(true)

  function trial(print) {
    if ( print ) {
      var job = "painter"
      console.log(job)
    }
    console.log(job)
  }
  ````
  
3. GLOBAL DECLARATION: GLOBAL SCOPE
 ````
 job = "painter"
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
   console.log(typeof fruits); // object 
   
   var me = {firstName:"Sammie", lastName:"Bae"};
   console.log(typeof me); // object    
  ````
