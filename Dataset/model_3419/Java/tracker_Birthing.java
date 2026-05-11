





import java.util.List;
import java.util.ArrayList;

public class tracker_Birthing extends Event {

    private boolean assisted;
    private boolean viability;
    private String difficulty;



    public tracker_Birthing(
        boolean assisted,        boolean viability,        String difficulty    ) {
        super(
        );
        this.assisted = assisted;
        this.viability = viability;
        this.difficulty = difficulty;
    }


    public boolean getAssisted() {
        return assisted;
    }

    public void setAssisted(boolean assisted) {
        this.assisted = assisted;
    }
    public boolean getViability() {
        return viability;
    }

    public void setViability(boolean viability) {
        this.viability = viability;
    }
    public String getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }


}