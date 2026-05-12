





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private int number;
    private int score;



    public Game(
        int number,        int score    ) {
        this.number = number;
        this.score = score;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }


}