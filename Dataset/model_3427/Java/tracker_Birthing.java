





import java.util.List;
import java.util.ArrayList;

public class tracker_Birthing extends Event {

    private boolean assisted;
    private String difficulty;
    private boolean viability;



    public tracker_Birthing(
        boolean assisted,        String difficulty,        boolean viability    ) {
        super(
        );
        this.assisted = assisted;
        this.difficulty = difficulty;
        this.viability = viability;
    }


    public boolean getAssisted() {
        return assisted;
    }

    public void setAssisted(boolean assisted) {
        this.assisted = assisted;
    }
    public String getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }
    public boolean getViability() {
        return viability;
    }

    public void setViability(boolean viability) {
        this.viability = viability;
    }


}