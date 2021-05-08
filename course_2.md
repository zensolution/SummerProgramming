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
    
1. Loop can be nested 
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
