





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private None mine_field;
    private None time_keeper;
    private int score;





    private Timer timer;


    public Game(
        None mine_field,        None time_keeper,        int score    ) {
        this.mine_field = mine_field;
        this.time_keeper = time_keeper;
        this.score = score;
    }


    public None getMine_field() {
        return mine_field;
    }

    public void setMine_field(None mine_field) {
        this.mine_field = mine_field;
    }
    public None getTime_keeper() {
        return time_keeper;
    }

    public void setTime_keeper(None time_keeper) {
        this.time_keeper = time_keeper;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public Timer getTimer() {
        return timer;
    }

    public void setTimer(Timer timer) {
        this.timer = timer;
    }

}