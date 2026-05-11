





import java.util.List;
import java.util.ArrayList;

public class qm_MeasureRankingEvaluationResult  {

    private float ratioAffected;





    private qm_MultiMeasureEvaluationResult qm_multimeasureevaluationresult;




    private qm_MeasureRanking qm_measureranking;


    public qm_MeasureRankingEvaluationResult(
        float ratioAffected    ) {
        this.ratioAffected = ratioAffected;
    }


    public float getRatioaffected() {
        return ratioAffected;
    }

    public void setRatioaffected(float ratioAffected) {
        this.ratioAffected = ratioAffected;
    }

    public qm_MultiMeasureEvaluationResult getQm_multimeasureevaluationresult() {
        return qm_multimeasureevaluationresult;
    }

    public void setQm_multimeasureevaluationresult(qm_MultiMeasureEvaluationResult qm_multimeasureevaluationresult) {
        this.qm_multimeasureevaluationresult = qm_multimeasureevaluationresult;
    }
    public qm_MeasureRanking getQm_measureranking() {
        return qm_measureranking;
    }

    public void setQm_measureranking(qm_MeasureRanking qm_measureranking) {
        this.qm_measureranking = qm_measureranking;
    }

}