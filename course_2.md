## Control Flow

1. If Statement

    ````
    var age = 15;
    
    // if
    if( age > 18 ) {
       console.log("You are adult.");
    }
    
    // if ... else ...
    if( age > 18 ) {
       console.log("You can vote.");
    } else {
       console.log("You can not vote");
    }
    
    // if ... else if ...
    var book = "maths";
    if( book == "history" ) {
       console.log("History Book");
    } else if( book == "maths" ) {
       console.log("Maths Book");
    } else if( book == "economics" ) {
       document.write("Economics Book");
    } else {
       console.log("Unknown Book<");
    } 
    ````
    
    **Quiz**
    
    Implement abs function 
    ````
      console.log(abs(10)) // should print 10
      console.log(abs(-10)) // should print 10
      
      function abs(x) {
        // implement your code
      }
    ````
    
1. while statement
    ````
    var count = 0;
    document.write("Starting Loop ");

    while (count < 10) {
       document.write("Current Count : " + count + "<br />");
       count++;
    }

    document.write("Loop stopped!");
    ````
1. for loop
    ````
    var count;
    document.write("Starting Loop" + "<br />");

    for(count = 0; count < 10; count++) {
       document.write("Current Count : " + count );
       document.write("<br />");
    }         
    document.write("Loop stopped!");
    ````
## function 

    Function is a reusable block of code
    
    ````
    function sum(a, b) {
        return a + b;
    }

    console.log(sum(1,3))
    console.log(sum(3,5))
    ````
### Quiz 
  
  write a function to calculate slope? Make sure you have considered all scenario
  
  ````
  function slope(x1, y1, x2, y2) {
  }
  console.log(slope(2,4,6,8))
  ````

    
