





import java.util.List;
import java.util.ArrayList;

public class qm_WeightedSumFactorAggregation extends FactorAggregation {






    private List<qm_FactorRanking> qm_factorrankings;


    public qm_WeightedSumFactorAggregation(
    ) {
        super(
        );
        this.qm_factorrankings = new ArrayList<>();
    }

    public qm_WeightedSumFactorAggregation(
        ArrayList<qm_FactorRanking> qm_factorrankings    ) {
        this.qm_factorrankings = qm_factorrankings;
    }


    public List<qm_FactorRanking> getQm_factorrankings() {
        return qm_factorrankings;
    }

    public void addQm_factorranking(Qm_factorranking qm_factorranking) {
        this.qm_factorrankings.add(qm_factorranking);
    }

}