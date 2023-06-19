### The Math Class

1. Common Math Methods
    ````
    Math.abs(x); // x is an int
    Math.abs(x); // x is a double
    Math.pow(base, exponent); // A double equal to the base raised to the exponent
    Math.sqrt(x); // A double equal to the square root of x
    Math.random(); // A random double in the range [0, 1), including 0, exclude 1
    ````
1. Quiz
    ````
    A math teacher is writing a program that will correctly calculate the area of a circle. Recall that the area of a circle is pi times the radiussquared( r2).AssumingMath.PIreturnsanaccurate decimal approximation of pi, which of the following statements WILL NOT calculate an accurate area of a circle with radius 22 ?
    (A) r*r*Math.PI; // r is the int 22
    (B) r*r*Math.PI; // r is the double 22.0
    (C) (double)r*r*Math.PI; // r is the int 22
    (D) (double)(r*r)*Math.PI; // r is the int 22
    (E) All of the above choices will calculate an accurate area.
    ````
    
### The String Class
1. Common String methods+
    ````
    length(); // An int equal to the length of the string
    substring(int beginIndex); // A String that is a substring of 
    substring(int beginIndex, int endIndex); // A String that is a substring of this string starting at beginIndex, ends at endIndex
    equals(Object anObject); // boolean if two string are eqaul to
    compareTo(String anotherString); // Returns an integer < 0 if string1 comes before string2, 0 if equal; 1, if comes later
    ````
1. Tips
    ````
    Don't "abc" == "abc", Use "abc".equals("abc");
    ````

1. Sample
    ````
    String sample = "Sample";
    System.out.print(sample.length());

    System.out.print(sample.substring(1, 4));

    System.out.println(sample.substring(1, 7)); // What would happend?

    System.out.print(sample.substring(1));

    sample.indexOf("amp"); 
    sample.indexOf("ok"); 

    sample.substring(1.0, 4.0);
    ````
1. Quiz
    ````
    Consider the following code segment:
         String s = "This is the beginning";
         String t = s.substring(5);
         int n = t.indexOf("the");
    Which of the following will be the value of n ?
    (A) –1 
    (B) 3
    (C) 7
    (D) 9
    (E) n will have no value because of a run-time error.

    Given the following code, what line will cause a compiler error?
         1 String word = "Sunday Funday Celebration 1.0";
         2 word.substring(7);
         3 word.substring(3, 6);
         4 word.indexOf("day");
         5 word.indexOf(1.0);
         6 word.compareTo("day");
    (A) line 2 (B) line 3 (C) line 4 (D) line 5 (E) line 6
    ````
