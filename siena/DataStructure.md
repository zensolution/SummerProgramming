# Data structure 

Definition: data structure is a specialized format for organizing, processing, retrieving and storing data.

## private class without method
  
  ````
  public class Main {

    public static void main(String[] args) {
       Status status = new Status();
       status.x = 1;
       status.y = 1;
       status.direction=2;
    }
  }

 class Status {
     int x;
     int y;
     int direction; 
  }
  ````

## Linear Data structure in Java

### Stack

  In stack, elements are stored and accessed in Last In First Out manner. That is, elements are added to the top of the stack and removed from the top of the stack.
  
  ````
  // Java code for stack implementation
  
  import java.io.*;
  import java.util.*;
  
  class Main { 
  	public static void main (String[] args)
  	{
  		Stack<String> stack = new Stack<String>();
  		stack.push("Z");
  		stack.push("Y");
  		stack.push("X");
  		stack.push("W");
  
      System.out.println(stack.pop());
      System.out.println(stack.peek());
      System.out.println(stack.push("A"));
      System.out.println(stack.pop());
  	}
  }
  ````

### Queue

It is an ordered list of objects with its use limited to inserting elements at the end of the list and deleting elements from the start of the list, (i.e.), it follows the FIFO or the First-In-First-Out principle.

  ````
  // Java code for stack implementation
  
  import java.io.*;
  import java.util.*;
  
  public class Main { 
  	public static void main (String[] args)
  	{
  		Queue<String> queue = new ArrayDeque<String>();
  		queue.add("Z");
  		queue.add("Y");
  		queue.add("X");
  		queue.add("W");
  
      System.out.println(queue.remove());
      System.out.println(queue.size());
      System.out.println(queue.peek());
      System.out.println(queue.add("A"));
      System.out.println(queue.remove());
  	}
  }
  ````

### Array

## Non-Linear Data structure in Java

### HashMap

LinkedHashMap is ordered.

### Tree

#### Singly Linked List
  
  ````
    public class Main {
  
      public static void main(String[] args) {
          TreeNode root = new TreeNode("Root");
          TreeNode node1 = new TreeNode("1");
          TreeNode node2 = new TreeNode("2");
          TreeNode node3 = new TreeNode("3");
          root.setNext(node1);
          node1.setNext(node2);
          node2.setNext(node3);
          
          TreeNode node = root;
          while ( true ) {
              System.out.println(node.getValue());
              if ( node.isLeaf() ) {
                  break;
              }
              node = node.getNext();
          }  
      }
    }
    
  class TreeNode {
      private String value;
      private TreeNode next;
      
      public TreeNode(String value) {
          this.value = value;
      }
      
      public boolean isLeaf() {
        return next == null;
      }
      
      public String getValue() {
        return value;
      }
      
      public void setNext(TreeNode node) {
         this.next = node;
      }
      
      public TreeNode getNext() {
        return this.next;
      }
  }
  ````

#### Doubly Linked List
    
#### Circular Linked List

#### Tree

 A node contains children.





