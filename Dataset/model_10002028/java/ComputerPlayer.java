





import java.util.List;
import java.util.ArrayList;

public class ComputerPlayer  {

    private int difficulty;





    private Creator creator;


    public ComputerPlayer(
        int difficulty    ) {
        this.difficulty = difficulty;
    }


    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }

    public Creator getCreator() {
        return creator;
    }

    public void setCreator(Creator creator) {
        this.creator = creator;
    }

}