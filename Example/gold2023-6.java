import java.util.Scanner;

public class Main
{
    private String[][] map = new String[40][20];
    private int currentX = 1;
    private int currentY = 1;
    private char currentLetter = ' ';
    private String facing = "RIGHT";
    
    public Main() {
        initMap();
    }
    
    private void initMap() {
        for (int j=0; j<20; j++) {
            for(int i=0; i<40; i++) {
                if ( i == 0 || j == 0 || i == 39 || j == 19 ) {
                    map[i][j] = "*";
                } else {
                    map[i][j] = " ";
                }
            }
        }
        map[1][1] = "#";
    }
    
    private void drawMap() {
        for (int j=0; j<20; j++) {
            for(int i=0; i<40; i++) {
                System.out.print(map[i][j]);
            }
            System.out.println();
        }
    }
    
    private char getNextLetter(char letter) {
        if ( letter == ' ' ) {
            return 'a';
        } else if ( 'z' == letter ) {
            return 'A';
        } else {
            return ++letter;
        }
    }
    
    private String changeDirection(String currentDirection, String action) {
        if ( "RIGHT".equals(currentDirection) && "R".equals(action) ) {
            return "DOWN";
        }
        if ( "RIGHT".equals(currentDirection) && "L".equals(action) ) {
            return "UP";
        }
        if ( "LEFT".equals(currentDirection) && "R".equals(action) ) {
            return "UP";
        }
        if ( "LEFT".equals(currentDirection) && "L".equals(action) ) {
            return "DOWN";
        }
        if ( "UP".equals(currentDirection) && "R".equals(action) ) {
            return "RIGHT";
        }
        if ( "UP".equals(currentDirection) && "L".equals(action) ) {
            return "LEFT";
        }
        if ( "DOWN".equals(currentDirection) && "R".equals(action) ) {
            return "LEFT";
        }
        if ( "DOWN".equals(currentDirection) && "L".equals(action) ) {
            return "RIGHT";
        }
        throw new Error("unknown operation");
    }
    
    private boolean move(String direction, int step) {
        int moveX = 0;
        int moveY = 0;
        if ("RIGHT".equals(this.facing)) {
            moveX = "F".equals(direction) ? 1 : -1;
        }
        if ("LEFT".equals(this.facing)) {
            moveX = "F".equals(direction) ? -1 : 1;
        }        
        if ("UP".equals(this.facing)) {
            moveY = "F".equals(direction) ? -1 : 1;
        }        
        if ("DOWN".equals(this.facing)) {
            moveY = "F".equals(direction) ? 1 : -1;
        }             
        for (int i=0; i<step; i++) {
            int nextX = this.currentX + moveX;
            int nextY = this.currentY + moveY;
            if ("*".equals(this.map[nextX][nextY])) {
                return false;
            }
            if (this.currentLetter == 'Z' ) {
              return false;
            }
            this.currentLetter = this.getNextLetter(this.currentLetter);
            this.map[nextX][nextY] = this.currentLetter+"";
            this.currentX = nextX;
            this.currentY = nextY;
        }
        return true;
    }

    public void execute() {
        Scanner keyboard = new Scanner(System.in);
        char currentLeter = ' ';

        String direction = "RIGHT";
        
        while ( true ) {
            System.out.println("enter an action:");
            String actionLetter =  keyboard.nextLine();
            if ( "Q".equals(actionLetter)) {
                break;
            }
            int step = 0;
            if ("F".equals(actionLetter) || "B".equals(actionLetter) ) {
                System.out.println("enter steps:");
                step = keyboard.nextInt();
                keyboard.nextLine();
                if ( !this.move(actionLetter, step) ) {
                    break;
                }
            }

            if ("R".equals(actionLetter) || "L".equals(actionLetter) ) {
                this.facing = this.changeDirection(this.facing, actionLetter);
            }
            
        }
        this.drawMap();
    }
    
    public static void main(String[] args) {
        new Main().execute();
    }
}
