





import java.util.List;
import java.util.ArrayList;

public class diva_ScoredElement extends DiVAModelElement {

    private int totalScore;





    private List<diva_Score> diva_scores;


    public diva_ScoredElement(
        int totalScore    ) {
        super(
        );
        this.totalScore = totalScore;
        this.diva_scores = new ArrayList<>();
    }

    public diva_ScoredElement(
        int totalScore        ArrayList<diva_Score> diva_scores    ) {
        this.totalScore = totalScore;
        this.diva_scores = diva_scores;
    }

    public int getTotalscore() {
        return totalScore;
    }

    public void setTotalscore(int totalScore) {
        this.totalScore = totalScore;
    }

    public List<diva_Score> getDiva_scores() {
        return diva_scores;
    }

    public void addDiva_score(Diva_score diva_score) {
        this.diva_scores.add(diva_score);
    }

}