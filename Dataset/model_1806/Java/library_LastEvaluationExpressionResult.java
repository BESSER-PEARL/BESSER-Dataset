





import java.util.List;
import java.util.ArrayList;

public class library_LastEvaluationExpressionResult extends BaseExpressionResult {

    private String lastEvalResult;



    public library_LastEvaluationExpressionResult(
        String lastEvalResult    ) {
        super(
        );
        this.lastEvalResult = lastEvalResult;
    }


    public String getLastevalresult() {
        return lastEvalResult;
    }

    public void setLastevalresult(String lastEvalResult) {
        this.lastEvalResult = lastEvalResult;
    }


}