





import java.util.List;
import java.util.ArrayList;

public class alf_PostfixOperation  {

    private String operator;





    private alf_PostfixExpressionCompletion alf_postfixexpressioncompletion;


    public alf_PostfixOperation(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public alf_PostfixExpressionCompletion getAlf_postfixexpressioncompletion() {
        return alf_postfixexpressioncompletion;
    }

    public void setAlf_postfixexpressioncompletion(alf_PostfixExpressionCompletion alf_postfixexpressioncompletion) {
        this.alf_postfixexpressioncompletion = alf_postfixexpressioncompletion;
    }

}