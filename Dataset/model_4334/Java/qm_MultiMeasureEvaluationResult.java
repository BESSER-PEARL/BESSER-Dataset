





import java.util.List;
import java.util.ArrayList;

public class qm_MultiMeasureEvaluationResult extends EvaluationResult {






    private List<qm_MeasureRankingEvaluationResult> qm_measurerankingevaluationresults;


    public qm_MultiMeasureEvaluationResult(
    ) {
        super(
        );
        this.qm_measurerankingevaluationresults = new ArrayList<>();
    }

    public qm_MultiMeasureEvaluationResult(
        ArrayList<qm_MeasureRankingEvaluationResult> qm_measurerankingevaluationresults    ) {
        this.qm_measurerankingevaluationresults = qm_measurerankingevaluationresults;
    }


    public List<qm_MeasureRankingEvaluationResult> getQm_measurerankingevaluationresults() {
        return qm_measurerankingevaluationresults;
    }

    public void addQm_measurerankingevaluationresult(Qm_measurerankingevaluationresult qm_measurerankingevaluationresult) {
        this.qm_measurerankingevaluationresults.add(qm_measurerankingevaluationresult);
    }

}