





import java.util.List;
import java.util.ArrayList;

public class qm_SingleMeasureEvaluationResult extends EvaluationResult {

    private float ratioAffected;



    public qm_SingleMeasureEvaluationResult(
        float ratioAffected    ) {
        super(
        );
        this.ratioAffected = ratioAffected;
    }


    public float getRatioaffected() {
        return ratioAffected;
    }

    public void setRatioaffected(float ratioAffected) {
        this.ratioAffected = ratioAffected;
    }


}