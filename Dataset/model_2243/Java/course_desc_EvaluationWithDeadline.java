





import java.util.List;
import java.util.ArrayList;

public class course_desc_EvaluationWithDeadline extends Evaluation {

    private String deadlineEvaluation;



    public course_desc_EvaluationWithDeadline(
        String deadlineEvaluation    ) {
        super(
        );
        this.deadlineEvaluation = deadlineEvaluation;
    }


    public String getDeadlineevaluation() {
        return deadlineEvaluation;
    }

    public void setDeadlineevaluation(String deadlineEvaluation) {
        this.deadlineEvaluation = deadlineEvaluation;
    }


}