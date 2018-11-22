public class Beers {
    private static int countBeers(String[] strings) {
        int numberOfBeers = strings[0].length();
        int numbers[] = new int[strings.length];
        int result = numberOfBeers;
        for (int i = 0; i < strings.length; i++) {
            numbers[i] = Integer.parseInt(strings[i].replace('Y', '1').replace('N', '0'), 2);
        }
        for (int i = 0; i < 1 << numberOfBeers; i++) {
            boolean optimal = true;
            for (int number : numbers)
                if ((i & number) == 0)
                    optimal = false;
            if (optimal && result > Integer.bitCount(i))
                result = Integer.bitCount(i);
        }
        return result;
    }

    public static void main(String[] args) {
        String[] strings = new String[]{"YNN", "YNY", "YNY", "NYY", "NYY", "NYN"};
        System.out.println(countBeers(strings));
    }
}