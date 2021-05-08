## Pre course video

https://www.youtube.com/watch?v=l26oaHV7D40&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye&index=13

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
    } else {
       console.log("Unknown Book<");
    } 
    ````
    
    ````
      //Logical AND Expression
      x && y
      
      //Logical OR Expression
      x || y      
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
    
    Implement a function to tell if a number can be divided by 3 or 5
    ````
      console.log(isDividableBy3Or5(10)) // should print true
      console.log(isDividableBy3Or5(9)) // should print true
      console.log(isDividableBy3Or5(17)) // should print false
      
      function isDividableBy3Or5(x) {
        // implement your code
      }
      //Hint. use something like if (conditionA and conditionB) { // ... }
      
    ````        
    
    Implement guess function 
    ````
      console.log(guess("o")) // should print "vowel sound"
      console.log(guess("b")) // should print "consonant sound"
      
      // Assume they are all lower case
      function guess(str) {
        // implement your code
      }
    ````
    
1. while statement
    ````
    var count = 0;
    console.log("Starting Loop ");

    while (count < 10) {
       console.log("Current Count : " + count + "<br />");
       count++;  // equival to count = count + 1
    }

    console.log("Loop stopped!");
    ````
    **Quiz**
    
    What does the following code output? 
    ````
      var i = 0;
      while (i < 3) {
          println("hi");
          i++;
      }
    ````
    
    Print repeat star
    ````
    loop(5)  // should output *****
    loop(1)  // should output *
    loop(0)  // do nothing
    loop(-1) // should output Error
    
    function loop(count) {
      //implement your code
    }
    ````
     
    Write a program and output 9 x 9 Multiplication table
    Hint: you can use nested loop
    ````
    1 * 1 = 1
    2 * 1 = 2 2 * 2 = 4
    3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
    ...
    9 * 1 = 9 ... ...         9 * 9 = 81
    ````   
   
1. for loop
    ````
    var count;
    console.log("Starting Loop" + "<br />");

    for(count = 0; count < 10; count++) {
       console.log("Current Count : " + count );
       console.log("<br />");
    }         
    console.log("Loop stopped!");
    ````
    
    **Quiz**
    
    Implement a reverse function
    ````
      reverse("Hello") // should output olleH
      
      //Hint. You can use String length and charAt function
      
      function reverse(str) {
        var retval = ""
        // implement your code
        return retval
      }
    ````    
    
    Implement a reverse Integer function
    ````
      reverse(321) // should output 123
      reverse(210) // should output 12
      reverse(-123) // should output -321
      
      function reverse(x) {
        // implement your code
      }
    ````     
    
    sigma function
    ````
      console.log(sigma(2, 5)) // should output 2+3+4+5=14
      
      function sigma(begin, end) {
        // implement your code
      }
    ````     
     
    sigma function. but only calculate value can be divided by 8
    ````
      console.log(sigma(2, 16)) // should output 8 + 16 = 24
      
      function sigma(begin, end) {
        // implement your code
      }
    ````        
1. Jumps 

    ````
    for(count = 0; count < 10; count++) {
       console.log(count)
       if ( count == 3) {
         break;
       }
    }         
    ````
    
    ````
    function run() {
        for(count = 0; count < 10; count++) {
           console.log(count)
           if ( count == 3) {
             return count;
           }
        }     
    }    
    ````
