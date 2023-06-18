## PROGRAMMING STYLE
### Comments, Identifiers, White Space
1. Comments
  - In-line, or short, comments appear after or near a statement and are preceded by two forward slashes (“//”) 
    ````
    // This is a constant to represent PI
    constant int PI = 3.14159;
    int radius = 3; // This is a radius of a circle
    ````
  - Long comments. begin with (“/*”) and end with (“*/”)
    ````
    /* The following code is used to do the following work:
      1. put meat into water
      2. heat water into 100 degree
      3. wait for 30 minutes
    */
    private void cook() {
    }
    ````
2. Identifier
  - contain any combination of letters, numbers, and underscore ("_")
  - starts with letter
  - no space
  - Optional. Identifier should be self-explained. For example, radius is better than r. wheelRadius is better radius
  - Optional. Usually starts with lower case. The following words are capital, like numberOfStudents. 
3. Whitespace
  - Used to increase readablity, but doesn't affect functionality
  
### Compiling & Errors
1. syntax error
2. runtime error

   ````
     int total = 100;
     int count = 0;
     int average = total / count;
   ````

   ````
     int j = 10;
     j = j * total;
   ````
3. quiz 
  ````
  1. Assuming all other statements in the program are correct, each of the following statements will allow the program to compile EXCEPT
  (A) // This is a comment
  (B) /* This is a comment */
  (C) // myName is a good identifier name
  ````
 
 
 
