





import java.util.List;
import java.util.ArrayList;

public class qm_DoubleInterval  {

    private float upper;
    private float lower;





    private qm_MeasureRankingEvaluationResult qm_measurerankingevaluationresult;




    private qm_NumberMeasurementResult qm_numbermeasurementresult;




    private qm_EvaluationResult qm_evaluationresult;


    public qm_DoubleInterval(
        float upper,        float lower    ) {
        this.upper = upper;
        this.lower = lower;
    }


    public float getUpper() {
        return upper;
    }

    public void setUpper(float upper) {
        this.upper = upper;
    }
    public float getLower() {
        return lower;
    }

    public void setLower(float lower) {
        this.lower = lower;
    }

    public qm_MeasureRankingEvaluationResult getQm_measurerankingevaluationresult() {
        return qm_measurerankingevaluationresult;
    }

    public void setQm_measurerankingevaluationresult(qm_MeasureRankingEvaluationResult qm_measurerankingevaluationresult) {
        this.qm_measurerankingevaluationresult = qm_measurerankingevaluationresult;
    }
    public qm_NumberMeasurementResult getQm_numbermeasurementresult() {
        return qm_numbermeasurementresult;
    }

    public void setQm_numbermeasurementresult(qm_NumberMeasurementResult qm_numbermeasurementresult) {
        this.qm_numbermeasurementresult = qm_numbermeasurementresult;
    }
    public qm_EvaluationResult getQm_evaluationresult() {
        return qm_evaluationresult;
    }

    public void setQm_evaluationresult(qm_EvaluationResult qm_evaluationresult) {
        this.qm_evaluationresult = qm_evaluationresult;
    }

}