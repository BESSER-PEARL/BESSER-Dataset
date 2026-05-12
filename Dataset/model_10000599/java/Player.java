





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;
    private int score;



    public Player(
        String name,        int score    ) {
        this.name = name;
        this.score = score;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }


}