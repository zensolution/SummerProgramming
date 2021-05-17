## Expression

  - Comparison Operators

    // Given that x = 5
    
    | Operator      | Description | Comparing     |  Returns |
    | :---        |    :----:   |          ---: |  ---: |
    | ==      | Equal to       | x == 8   |  false |
    |         |         | x == 5     |  true  |
    |  !=     |  not equal | x != 8 | true |
    |        |    | x != 5 | false |
    |   >     |   greater than  | x > 8 | false |
    |   <     |   less than  | x < 8 | true |
    |   >=     |  greater than or equal to  | x >= 8 | false |
    |   <=     |  less than or equal to  | x <= 8 | false |

  - Logical Operators
  
    Given that x = 6 and y = 3, the table below explains the logical operators:
 
    | Operator      | Description | Example     |  
    | :---        |    :----:   |          ---: |  
    |  &&      | and       | (x < 10 && y > 1) is true   |  
    |  \|\|      | or       | (x == 5 \|\| y == 5) is false  |  
    |  !      | not       | !(x == y) is true   |  
    
   **quiz**
   
   1.  i, j, and k contain the values 10, 3, and 20, respectively, what is the value of the following logical expression: 
         
         j < 4 || j == 5 && i <= k    
         
   1. The expression P AND Q is TRUE if either P or Q is TRUE or both are TRUE.
   
   3. If p is a Boolean variable, which of the following logical expressions always has the value false?
        
        A. p && p
        
        B. p || p
        
        C. p && !p
        
        D. p || !p
        
        E. b and d above

   3. True or False? The expression !(n < 5) is equivalent to the expression n > 5.
   
        A.	True

        B.	False

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

    **Quiz**
    
    Implement abs function 
    ````
      console.log(abs(10)) // should print 10
      console.log(abs(-10)) // should print 10
      
      function abs(x) {
        // implement your code
      }
    ````
    
    If time is less than 10:00, create a "Good morning" greeting, if not, but time is less than 20:00, create a "Good day" greeting, otherwise a "Good evening":
    ````
       console.log(greeting(8))   // print "Good morning" 
       console.log(greeting(13))  // print "Good day"
       console.log(greeting(22))  // print "Good evening"
       
       function greeting(hour) {
         //implement your code
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
    loop(5)  // should output 
    /* should output 
        *
        **
        ***
        ****
        *****
    */
    
    
    function loop(count) {
      //implement your code
    }
    
    // Hint, please experiment "*".repeat(5)
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
    
    sigma function
    ````
      console.log(sigma(2, 5)) // should output 2+3+4+5=14
      
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
