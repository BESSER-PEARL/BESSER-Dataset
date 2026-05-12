





import java.util.List;
import java.util.ArrayList;

public class RandomPlayer  {

    private String score;
    private String name;



    public RandomPlayer(
        String score,        String name    ) {
        this.score = score;
        this.name = name;
    }


    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}