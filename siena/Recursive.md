## Example of Recursive Method

Given an equation f(n) = 3 * f(n-1) + 2 * f(n-2). f(0) = 1 f(1) = 2

  ````
    public class Main {
  
      public int solve(int n) {
          if ( n == 0 ) {
              return 1;
          } else if ( n == 1 ) {
              return 2;
          } else {
              return 3 * solve(n-1) + 2 * solve(n-2);
          }
      }
      
      public static void main(String[] args) {
         System.out.println(new Main().solve(11));
      }
    }
  ````

Find all divisible numbers

  ````
    import java.util.*;

    public class Main {
  
      public List<Integer> divisibleNumbers (int number, int divisor) {
          List<Integer> divisors = new ArrayList<Integer>();
          if ( number % divisor == 0 ) {
              divisors.add(Integer.valueOf(divisor));
          }
          if ( divisor > 1) {
            divisors.addAll(divisibleNumbers(number, divisor-1));
          }
          return divisors;
      }
      
      public static void main(String[] args) {
         System.out.println(new Main().divisibleNumbers(30, 30));
      }
    }
  ````

Quiz: 

  Reverse a string using recursive
  
  Given a number n, print the following pattern without using any loop.

    n, n-5, n-10, …, 0, 5, 10, …, n-5, n

Examples : 

    Input: n = 16
    Output: 16, 11, 6, 1, -4, 1, 6, 11, 16

More quiz: 

  https://www.geeksforgeeks.org/recursion-practice-problems-solutions/
