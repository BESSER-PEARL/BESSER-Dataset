





import java.util.List;
import java.util.ArrayList;

public class qm_WeightedSumMultiMeasureEvaluation extends MultiMeasureEvaluation {






    private List<qm_MeasureRanking> qm_measurerankings;


    public qm_WeightedSumMultiMeasureEvaluation(
    ) {
        super(
        );
        this.qm_measurerankings = new ArrayList<>();
    }

    public qm_WeightedSumMultiMeasureEvaluation(
        ArrayList<qm_MeasureRanking> qm_measurerankings    ) {
        this.qm_measurerankings = qm_measurerankings;
    }


    public List<qm_MeasureRanking> getQm_measurerankings() {
        return qm_measurerankings;
    }

    public void addQm_measureranking(Qm_measureranking qm_measureranking) {
        this.qm_measurerankings.add(qm_measureranking);
    }

}