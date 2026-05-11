





import java.util.List;
import java.util.ArrayList;

public class diva_Score extends DiVAModelElement {

    private int score;





    private diva_ScoredElement diva_scoredelement;


    public diva_Score(
        int score    ) {
        super(
        );
        this.score = score;
    }


    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public diva_ScoredElement getDiva_scoredelement() {
        return diva_scoredelement;
    }

    public void setDiva_scoredelement(diva_ScoredElement diva_scoredelement) {
        this.diva_scoredelement = diva_scoredelement;
    }

}