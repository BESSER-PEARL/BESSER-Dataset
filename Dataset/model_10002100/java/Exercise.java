





import java.util.List;
import java.util.ArrayList;

public class Exercise  {

    private boolean user_exercise;
    private int difficulty;



    public Exercise(
        boolean user_exercise,        int difficulty    ) {
        this.user_exercise = user_exercise;
        this.difficulty = difficulty;
    }


    public boolean getUser_exercise() {
        return user_exercise;
    }

    public void setUser_exercise(boolean user_exercise) {
        this.user_exercise = user_exercise;
    }
    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }


}