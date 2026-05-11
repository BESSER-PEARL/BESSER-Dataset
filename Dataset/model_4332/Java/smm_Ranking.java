





import java.util.List;
import java.util.ArrayList;

public class smm_Ranking extends Measure {






    private smm_RankingInterval smm_rankinginterval;




    private List<smm_RankingInterval> smm_rankingintervals;


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


    public smm_RankingInterval getSmm_rankinginterval() {
        return smm_rankinginterval;
    }

    public void setSmm_rankinginterval(smm_RankingInterval smm_rankinginterval) {
        this.smm_rankinginterval = smm_rankinginterval;
    }
    public List<smm_RankingInterval> getSmm_rankingintervals() {
        return smm_rankingintervals;
    }

    public void addSmm_rankinginterval(Smm_rankinginterval smm_rankinginterval) {
        this.smm_rankingintervals.add(smm_rankinginterval);
    }

}