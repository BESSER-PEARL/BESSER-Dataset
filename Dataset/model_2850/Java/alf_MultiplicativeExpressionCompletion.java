





import java.util.List;
import java.util.ArrayList;

public class alf_MultiplicativeExpressionCompletion  {

    private String operator;





    private List<alf_UnaryExpression> alf_unaryexpressions;




    private alf_MultiplicativeExpression alf_multiplicativeexpression;


    public alf_MultiplicativeExpressionCompletion(
        String operator    ) {
        this.operator = operator;
        this.alf_unaryexpressions = new ArrayList<>();
    }

    public alf_MultiplicativeExpressionCompletion(
        String operator        ArrayList<alf_UnaryExpression> alf_unaryexpressions    ) {
        this.operator = operator;
        this.alf_unaryexpressions = alf_unaryexpressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<alf_UnaryExpression> getAlf_unaryexpressions() {
        return alf_unaryexpressions;
    }

    public void addAlf_unaryexpression(Alf_unaryexpression alf_unaryexpression) {
        this.alf_unaryexpressions.add(alf_unaryexpression);
    }
    public alf_MultiplicativeExpression getAlf_multiplicativeexpression() {
        return alf_multiplicativeexpression;
    }

    public void setAlf_multiplicativeexpression(alf_MultiplicativeExpression alf_multiplicativeexpression) {
        this.alf_multiplicativeexpression = alf_multiplicativeexpression;
    }

}