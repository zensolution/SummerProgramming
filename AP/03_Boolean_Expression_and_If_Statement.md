### THE if STATEMENT

1. Syntax
    ````
    int num1 = 4, num2 = 5;
    if (num1 == num2) {
       System.out.print("The numbers are the same.");
    }
    ````
2. Common Symbol
    ````
    && logical and
    || logical or
    ! logical not
    == is equal to
    != is not equal to
    ````
3. ATTN
    ````
    //What is wrong here?
    int studentCount = 100; 
    if ( studentCount = 10 ) {
      // do something
    }
    ````
5. Quiz
    ````
    Consider the following code.
         int x = 0;
         if (x == 0)
            System.out.print(“1”);
         else
            System.out.print(“2”);
            System.out.print(“3”);
    Which of the following best describes the result of executing the code segment?
    (A) Since the value of x is 0, the first print statement will be performed, producing 1 as the output.
    (B) Since the value of x is 0, the first print statement will be performed, producing 13 as the output.
    (C) Since the value of x is 0, the first print statement will be performed, producing 123 as the output.
    (D) == is not the correct boolean operator, so a syntax error will be produced by the compiler prior to execution.
    (E) == is not the correct boolean operator, so a logical error will be produced by the compiler prior to execution.
    ````
