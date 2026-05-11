





import java.util.List;
import java.util.ArrayList;

public class qm_EvaluationResult extends Result {






    private qm_QualityModelResult qm_qualitymodelresult;




    private qm_Evaluation qm_evaluation;


    public qm_EvaluationResult(
    ) {
        super(
        );
    }



    public qm_QualityModelResult getQm_qualitymodelresult() {
        return qm_qualitymodelresult;
    }

    public void setQm_qualitymodelresult(qm_QualityModelResult qm_qualitymodelresult) {
        this.qm_qualitymodelresult = qm_qualitymodelresult;
    }
    public qm_Evaluation getQm_evaluation() {
        return qm_evaluation;
    }

    public void setQm_evaluation(qm_Evaluation qm_evaluation) {
        this.qm_evaluation = qm_evaluation;
    }

}