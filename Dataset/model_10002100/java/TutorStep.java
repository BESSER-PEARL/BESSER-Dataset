





import java.util.List;
import java.util.ArrayList;

public class TutorStep  {

    private String evidence;
    private int difficulty;



    public TutorStep(
        String evidence,        int difficulty    ) {
        this.evidence = evidence;
        this.difficulty = difficulty;
    }


    public String getEvidence() {
        return evidence;
    }

    public void setEvidence(String evidence) {
        this.evidence = evidence;
    }
    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }


}