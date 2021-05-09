## Pre Course 

https://www.youtube.com/watch?v=DuDz6B4cqVc&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye&index=15

## Basic Javascript Syntax

1. Define Variable - we use variable to store things
    ````
    let x = 5;
    let title = "Natual Selection";
    let y = x + 3;
    ````
1. Comment
      - Online comment: //
        ````
        // This is a commit
        ````
      - Multiline comment: /* */
        ````
        /*
         *  I have a lot to say
         */ 
        ````
1. Print something to console

    ````
    let x = 5;
    console.log(x)
    ````
**Quiz:**

    Define a variable "name" with your name and print it out    

## Primitive Javascript Type

1. Number
    ````
    let x = 5;
    let pi = 3.14;
    ````
 
    **Math Operator:**
    
        +   Addition
        -   Minus
        *   Multiply
        /   Divide
        %   Remainder
        
    **Quiz:**
    
        What is the value of 5 % 2?
    
    **Math Library:** 
    
        // JavaScript provides a Math library. The below are some frequently used function 
        console.log(Math.max(1, 3, 2));

        console.log(Math.min(1, 3, 2));

        console.pws(Math.pow(2, 4));

        console.log(Math.ceil(7.004));

        console.log(Math.floor(-5.05));

        console.log(Math.round(0.9));

        console.log(Math.round(1.1));
        
    **Quiz:**
        
        Use Math library to print the maximum value of 5.4^3 and 3.5^4       
        
    **Reference:**
    
        More Math library. Plear check this link. [&#8594;](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)   

        Find the method that can generate a rand integer?
        
1. String
    ````
    var name = "John Doe";
    
    // return length of a string
    var sln = name.length; 
    
    // return a new string that located at the specified offset of the string.
    console.log(name.charAt(5))
    
    //Join two string
    var firstName = "Tom"
    var lastName = "Brady"
    var fullName = firstName + " " + lastName
    console.log(fullName)
    
    // determines whether a string begins with the characters of a specified string
    const str1 = 'Saturday night plans';
    console.log(str1.startsWith('Sat'));
    
    // returns the index within the calling String object of the first occurrence of the specified value
    const paragraph = 'The quick brown fox jumps over the lazy dog. If the dog barked, was it really lazy?';
    const searchTerm = 'dog';
    const indexOfFirst = paragraph.indexOf(searchTerm);
    
    // returns the part of the string between the start and end indexes, or to the end of the string.
    const str = 'Mozilla';
    console.log(str.substring(1, 3));
    console.log(str.substring(2));
    ````
    **Quiz:**
        
        // Hint: check string indexOf method
        Find if "of" exits in the string "This is the best time, this is the worst time"
        
        Find the 8th character in the string "This is the best time, this is the worst time"
    
    **Reference:**
        
        More String library. Plear check this link. [&#8594;](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) 
        
        Find the method 
        
1. Character
    ````
    // Convert a number to a string
    var x = 68
    console.log(String.fromCharCode(x))
    
    // Convert a string to number
    console.log("a".charCodeAt(0))
    ````
    
    **Reference:**        
        ASCII table. Plear check this link. [&#8594;](https://www.youtube.com/watch?v=zB85kTs-sEw)   
    
1. Bool  
    ````
    let x = true;
    ````
1. Data Type conversion
    ````
    // convert a number to string
    var x = 68
    var y = x.toString()
    console.log(y)
    console.log(typeof(y))

    // convert string to a number
    var x = "68"
    var y = parseInt(x)
    console.log(y)
    console.log(typeof(y))
    ````
## Function 

    Function is a reusable block of code
    
    ````
    function sum(a, b) {
        return a + b;
    }

    console.log(sum(1,3))
    console.log(sum(3,5))
    ````
    
    **Quiz** 

      write a function to calculate slope? Make sure you have considered all scenario

      ````
      function slope(x1, y1, x2, y2) {
      }
      console.log(slope(2,4,6,8))
      ````

    

## Object

    Some kinds of key-value pair. for example, 
    
    ````
    let person = {
        firstName: "James",
        lastName: "Bond",
        salary: 120000,
    }
    
    // Access the object
    console.log(person.lastName)
    console.log(person["firstName"])
    ````
  **Quiz** 

1. Define an object that describes a cirle in the X-Y plane
2. Define an object that describes a cat
3. rewrite the slope function using object
  
  ````
  function slope(point1, point2) {
  }
  // Please define point1 and point2 below
  // end of definition
  console.log(slope(point1, point2))
  ````  
