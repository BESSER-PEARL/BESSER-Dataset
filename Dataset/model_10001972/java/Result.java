





import java.util.List;
import java.util.ArrayList;

public class Result  {

    private int score;
    private String player;



    public Result(
        int score,        String player    ) {
        this.score = score;
        this.player = player;
    }


    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }


}