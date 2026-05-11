





import java.util.List;
import java.util.ArrayList;

public class alf_AdditiveExpressionCompletion  {

    private String operator;





    private alf_MultiplicativeExpressionCompletion alf_multiplicativeexpressioncompletion;




    private alf_AdditiveExpression alf_additiveexpression;




    private List<alf_MultiplicativeExpression> alf_multiplicativeexpressions;


    public alf_AdditiveExpressionCompletion(
        String operator    ) {
        this.operator = operator;
        this.alf_multiplicativeexpressions = new ArrayList<>();
    }

    public alf_AdditiveExpressionCompletion(
        String operator        ArrayList<alf_MultiplicativeExpression> alf_multiplicativeexpressions    ) {
        this.operator = operator;
        this.alf_multiplicativeexpressions = alf_multiplicativeexpressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public alf_MultiplicativeExpressionCompletion getAlf_multiplicativeexpressioncompletion() {
        return alf_multiplicativeexpressioncompletion;
    }

    public void setAlf_multiplicativeexpressioncompletion(alf_MultiplicativeExpressionCompletion alf_multiplicativeexpressioncompletion) {
        this.alf_multiplicativeexpressioncompletion = alf_multiplicativeexpressioncompletion;
    }
    public alf_AdditiveExpression getAlf_additiveexpression() {
        return alf_additiveexpression;
    }

    public void setAlf_additiveexpression(alf_AdditiveExpression alf_additiveexpression) {
        this.alf_additiveexpression = alf_additiveexpression;
    }
    public List<alf_MultiplicativeExpression> getAlf_multiplicativeexpressions() {
        return alf_multiplicativeexpressions;
    }

    public void addAlf_multiplicativeexpression(Alf_multiplicativeexpression alf_multiplicativeexpression) {
        this.alf_multiplicativeexpressions.add(alf_multiplicativeexpression);
    }

}