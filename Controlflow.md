## Expression

  - Comparison Operators

    // Given that x = 5
    
    | Operator      | Description | Comparing     |  Returns |
    | :---        |    :----:   |          ---: |  ---: |
    | ==      | Equal to       | x == 8   |  False |
    |         |         | x == 5     |  True  |
    |  !=     |  not equal | x != 8 | True |
    |        |    | x != 5 | false |
    |   >     |   greater than  | x > 8 | False |
    |   <     |   less than  | x < 8 | True |
    |   >=     |  greater than or equal to  | x >= 8 | False |
    |   <=     |  less than or equal to  | x <= 8 | False |

  - Logical Operators
  
    Given that x = 6 and y = 3, the table below explains the logical operators:
 
    | Operator      | Description | Example     |  
    | :---        |    :----:   |          ---: |  
    |  and     | and       | (x < 10 and y > 1) is True   |  
    |  or      | or       | (x == 5 or y == 5) is False  |  
    |  not      | not       |  not(x == y) is true   |  
    
   **quiz**
   
   1.  i = 10, j = 3, k = 20, what is the value of the following logical expression: 
         
         j < 4 or j == 5 and i <= k    
         
   1. The expression P and Q is TRUE if either P or Q is TRUE or both are TRUE.
   
   3. If p is a Boolean variable, which of the following logical expressions always has the value false?
        
        A. p and p
        
        B. p or p
        
        C. p and !p
        
        D. p or !p
        
        E. b and d above

   3. True or False? The expression not (n < 5) is equivalent to the expression n > 5.
   
        A.	True

        B.	False

## Control Flow

1. If Statement

    ````
    book = "maths"

    if book == "history":
        print("History Book")
    elif book == "maths":
        print("Math Book")
    else:
        print("Unknown Book")  
    ````

    **Quiz**
    
    Implement abs function 
    ````
      def abs(x):
          #Implement your code below 

      print(abs(10)) # should print 10
      print(abs(-10)) # should print 10
    ````
    
    If time is less than 10:00, create a "Good morning" greeting, if not, but time is less than 20:00, create a "Good day" greeting, otherwise a "Good evening":
    ````
        def greeting(hour):
          # Implement your code here

       print(greeting(8))   # print "Good morning" 
       print(greeting(13))  # print "Good day"
       print(greeting(22))  # print "Good evening"             
    ````            
    
1. while statement
    ````
    count = 0
    print("Starting loop")

    while count<10:
        print("Current count : " + str(count))
        count +=1  # equivalent to "count = count+1"

    print("End loop")
    ````
    **Quiz**
    
    What does the following code output? 
    ````
    i = 0
    while i < 3:
        print("hi")
        i += 1
    ````
    
    Print repeat star
    ````
    def loop(count):
      ## Implement your code
      
    loop(5)  // should output 
    /* should output 
        *
        **
        ***
        ****
        *****
    */
    
    # Hint, check this link. https://www.w3schools.in/python-tutorial/repeat-string-in-python/
    ````
   
1. for loop
    ````
    for i in range(8):
      print(i)
    
    for i in range(2,6):
      print(i)
    ````
    
    **Quiz**
    
    sigma function
    ````
      def sigma(begin, end):
        // implement your code
      
      print(sigma(2, 5)) // should output 2+3+4+5=14            
    ````     
   
1. Break 

    ````
    for letter in 'Python':     # First Example
       if letter == 'h':
          break
       print 'Current Letter :', letter
    ````
    
1. Continue

    ````
    for letter in 'Python':     # First Example
       if letter == 'h':
          continue
       print 'Current Letter :', letter
    ````

