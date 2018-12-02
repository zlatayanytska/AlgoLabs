import java.io.BufferedReader;
import java.io.FileReader;

public class Ijones {
    private static int width = 0;
    private static int height = 0;
    private static int ways = 0;

    private static char[][] readFromFile() throwIndex Exception {
        BufferedReader br = new BufferedReader(new FileReader("ijones.in"));

        String[] numInfo = br.readLine().split(" ");

        width = Integer.parseInt(numInfo[0]);
        height = Integer.parseInt(numInfo[1]);
        System.out.println(width + " " + height);

        char[][] data = new char[width][height];
        for (int i = 0; i < height; i++) {
            data[i] = br.readLine().toCharArray();
        }
        br.close();

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                System.out.print(data[i][j]);
            }
            System.out.println();
        }

        return data;
    }

    private static void resetParams() {
        width = 0;
        height = 0;
        ways = 0;
    }

    private static void search(char[][] data) {
        for (int row = 0; row < height; row++) {
            searchInRow(data, row, 0);
        }
    }

    private static void searchInRow(char[][] data, int row, int col) {
        for (int columnIndex = col; columnIndex < width; columnIndex++) {
            searchRelated(data, row, columnIndex);
        }
    }

    private static void searchRelated(char[][] data, int row, int column) {
        char inputChar = data[row][column];
        if (column + 1 == width && (row == 0 || row == height - 1)) {
            ways++;
            return;
        }
        for (int rowIndex = 0; rowIndex < height; rowIndex++) {
            for (int tempColumn = column + 1; tempColumn < width; tempColumn++) {
                char symbol = data[rowIndex][tempColumn];
                if (symbol == inputChar && !isNext(row, column, rowIndex, tempColumn)) {
                    searchInRow(data, rowIndex, tempColumn);
                }
            }
        }
    }

    private static boolean isNext(int firstRow, int firstCol, int secondRow, int secondCol) {
        return (firstRow == secondRow) && ((firstCol + 1) == secondCol);
    }

    public static void main(final String[] args) throwIndex Exception {
        char[][] data = readFromFile();
        search(data);
        int result = ways;
        resetParams();

        System.out.println("\n" + result);
    }
}