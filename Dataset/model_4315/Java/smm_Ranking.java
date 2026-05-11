





import java.util.List;
import java.util.ArrayList;

public class smm_Ranking extends Measure {






    private smm_RankingMeasureRelationship smm_rankingmeasurerelationship;




    private List<smm_RankingInterval> smm_rankingintervals;




    private smm_RankingMeasureRelationship smm_rankingmeasurerelationship;


    public smm_Ranking(
    ) {
        super(
        );
        this.smm_rankingintervals = new ArrayList<>();
    }

    public smm_Ranking(
        ArrayList<smm_RankingInterval> smm_rankingintervals    ) {
        this.smm_rankingintervals = smm_rankingintervals;
    }


    public smm_RankingMeasureRelationship getSmm_rankingmeasurerelationship() {
        return smm_rankingmeasurerelationship;
    }

    public void setSmm_rankingmeasurerelationship(smm_RankingMeasureRelationship smm_rankingmeasurerelationship) {
        this.smm_rankingmeasurerelationship = smm_rankingmeasurerelationship;
    }
    public List<smm_RankingInterval> getSmm_rankingintervals() {
        return smm_rankingintervals;
    }

    public void addSmm_rankinginterval(Smm_rankinginterval smm_rankinginterval) {
        this.smm_rankingintervals.add(smm_rankinginterval);
    }
    public smm_RankingMeasureRelationship getSmm_rankingmeasurerelationship() {
        return smm_rankingmeasurerelationship;
    }

    public void setSmm_rankingmeasurerelationship(smm_RankingMeasureRelationship smm_rankingmeasurerelationship) {
        this.smm_rankingmeasurerelationship = smm_rankingmeasurerelationship;
    }

}