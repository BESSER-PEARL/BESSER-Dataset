





import java.util.List;
import java.util.ArrayList;

public class alf_EqualityExpressionCompletion  {

    private String operator;





    private List<alf_ClassificationExpression> alf_classificationexpressions;




    private alf_ClassificationExpressionCompletion alf_classificationexpressioncompletion;




    private alf_AndExpressionCompletion alf_andexpressioncompletion;


    public alf_EqualityExpressionCompletion(
        String operator    ) {
        this.operator = operator;
        this.alf_classificationexpressions = new ArrayList<>();
    }

    public alf_EqualityExpressionCompletion(
        String operator        ArrayList<alf_ClassificationExpression> alf_classificationexpressions    ) {
        this.operator = operator;
        this.alf_classificationexpressions = alf_classificationexpressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<alf_ClassificationExpression> getAlf_classificationexpressions() {
        return alf_classificationexpressions;
    }

    public void addAlf_classificationexpression(Alf_classificationexpression alf_classificationexpression) {
        this.alf_classificationexpressions.add(alf_classificationexpression);
    }
    public alf_ClassificationExpressionCompletion getAlf_classificationexpressioncompletion() {
        return alf_classificationexpressioncompletion;
    }

    public void setAlf_classificationexpressioncompletion(alf_ClassificationExpressionCompletion alf_classificationexpressioncompletion) {
        this.alf_classificationexpressioncompletion = alf_classificationexpressioncompletion;
    }
    public alf_AndExpressionCompletion getAlf_andexpressioncompletion() {
        return alf_andexpressioncompletion;
    }

    public void setAlf_andexpressioncompletion(alf_AndExpressionCompletion alf_andexpressioncompletion) {
        this.alf_andexpressioncompletion = alf_andexpressioncompletion;
    }

}