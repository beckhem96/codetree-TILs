import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static final int DIR_NUM = 4;
    public static final int MAX_N = 100;

    public static int n;
    public static int currX, currY; 
    public static int[][] a = new int[MAX_N + 1][MAX_N + 1];

    public static ArrayList<Integer> visitedNums = new ArrayList();

    public static boolean inRange(int x, int y) {
        return 1 <= x && x <= n && 1 <= y && y <= n;
    }

    public static boolean canGo(int x, int y, int currNum) {
        return inRange(x, y) && a[x][y] > currNum;
    }

    public static boolean simulate() {
        int[] dx = new int[]{-1, 1, 0, 0};
        int[] dy = new int[]{0, 0, -1, 1};

        for(int i = 0; i < 4; i++) {
            int nextX = currX + dx[i];
            int nextY = currY + dy[i];

            if(canGo(nextX, nextY, a[currX][currY])) {
                currX = nextX;
                currY = nextY;
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        currX = sc.nextInt();
        currY = sc.nextInt();

        for(int i = 1; i <= n; i++) 
            for(int j = 1; j <= n; j++)
                a[i][j] = sc.nextInt();

        visitedNums.add(a[currX][currY]);

        while(true) {
            boolean greaterNumberExist = simulate();

            if(!greaterNumberExist)
                break;

            visitedNums.add(a[currX][currY]);
        }
        for(int i =0; i < visitedNums.size(); i++)
            System.out.print(visitedNums.get(i) + " ");
    }
}