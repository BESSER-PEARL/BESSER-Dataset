





import java.util.List;
import java.util.ArrayList;

public class diva_ScoredElement extends DiVAModelElement {

    private int totalScore;



    public diva_ScoredElement(
        int totalScore    ) {
        super(
        );
        this.totalScore = totalScore;
    }


    public int getTotalscore() {
        return totalScore;
    }

    public void setTotalscore(int totalScore) {
        this.totalScore = totalScore;
    }


}