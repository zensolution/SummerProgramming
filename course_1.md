## Basic Javascript Syntax

1. Basic Javascript statement Syntax
    ````
    let x = 5;
    var title = "Natual Selection";
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
## Primitive Javascript Type

1. Number
    ````
    let x = 5;
    var title = "Natual Selection";
    ````
1. String
    ````
    let x = "Hello";
    ````
1. Bool  
    ````
    let x = true;
    ````
## Control Flow

1. If Statement

    ````
    var age = 15;
    
    // if
    if( age > 18 ) {
       document.write("<b>Qualifies for driving</b>");
    }
    
    // if ... else ...
    if( age > 18 ) {
       document.write("<b>Qualifies for driving</b>");
    } else {
       document.write("<b>Does not qualify for driving</b>");
    }
    
    // if ... else if ...
    var book = "maths";
    if( book == "history" ) {
       document.write("<b>History Book</b>");
    } else if( book == "maths" ) {
       document.write("<b>Maths Book</b>");
    } else if( book == "economics" ) {
       document.write("<b>Economics Book</b>");
    } else {
       document.write("<b>Unknown Book</b>");
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
## Object

    Some kinds of key-value pair. for example, 
    
    ````
    let person = {
        firstName: "James",
        lastName: "Bond",
        salary: 120000,
    }
    ````
### Quiz 

1. Define an object that describes a cirle in the X-Y plane
1. rewrite the slope function using object
  
  ````
  function slope(point1, point2) {
  }
  // Please define point1 and point2 below
  // end of definition
  console.log(slope(point1, point2))
  ````
    
    
