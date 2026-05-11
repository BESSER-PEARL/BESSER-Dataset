





import java.util.List;
import java.util.ArrayList;

public class alf_ShiftExpressionCompletion  {

    private String operator;





    private List<alf_AdditiveExpression> alf_additiveexpressions;




    private alf_RelationalExpressionCompletion alf_relationalexpressioncompletion;




    private alf_AdditiveExpressionCompletion alf_additiveexpressioncompletion;




    private alf_ShiftExpression alf_shiftexpression;


    public alf_ShiftExpressionCompletion(
        String operator    ) {
        this.operator = operator;
        this.alf_additiveexpressions = new ArrayList<>();
    }

    public alf_ShiftExpressionCompletion(
        String operator        ArrayList<alf_AdditiveExpression> alf_additiveexpressions    ) {
        this.operator = operator;
        this.alf_additiveexpressions = alf_additiveexpressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<alf_AdditiveExpression> getAlf_additiveexpressions() {
        return alf_additiveexpressions;
    }

    public void addAlf_additiveexpression(Alf_additiveexpression alf_additiveexpression) {
        this.alf_additiveexpressions.add(alf_additiveexpression);
    }
    public alf_RelationalExpressionCompletion getAlf_relationalexpressioncompletion() {
        return alf_relationalexpressioncompletion;
    }

    public void setAlf_relationalexpressioncompletion(alf_RelationalExpressionCompletion alf_relationalexpressioncompletion) {
        this.alf_relationalexpressioncompletion = alf_relationalexpressioncompletion;
    }
    public alf_AdditiveExpressionCompletion getAlf_additiveexpressioncompletion() {
        return alf_additiveexpressioncompletion;
    }

    public void setAlf_additiveexpressioncompletion(alf_AdditiveExpressionCompletion alf_additiveexpressioncompletion) {
        this.alf_additiveexpressioncompletion = alf_additiveexpressioncompletion;
    }
    public alf_ShiftExpression getAlf_shiftexpression() {
        return alf_shiftexpression;
    }

    public void setAlf_shiftexpression(alf_ShiftExpression alf_shiftexpression) {
        this.alf_shiftexpression = alf_shiftexpression;
    }

}