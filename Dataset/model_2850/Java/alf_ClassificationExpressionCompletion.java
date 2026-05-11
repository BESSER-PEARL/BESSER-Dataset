





import java.util.List;
import java.util.ArrayList;

public class alf_ClassificationExpressionCompletion  {

    private String operator;





    private alf_QualifiedName alf_qualifiedname;




    private alf_ClassificationExpression alf_classificationexpression;




    private alf_RelationalExpressionCompletion alf_relationalexpressioncompletion;


    public alf_ClassificationExpressionCompletion(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public alf_QualifiedName getAlf_qualifiedname() {
        return alf_qualifiedname;
    }

    public void setAlf_qualifiedname(alf_QualifiedName alf_qualifiedname) {
        this.alf_qualifiedname = alf_qualifiedname;
    }
    public alf_ClassificationExpression getAlf_classificationexpression() {
        return alf_classificationexpression;
    }

    public void setAlf_classificationexpression(alf_ClassificationExpression alf_classificationexpression) {
        this.alf_classificationexpression = alf_classificationexpression;
    }
    public alf_RelationalExpressionCompletion getAlf_relationalexpressioncompletion() {
        return alf_relationalexpressioncompletion;
    }

    public void setAlf_relationalexpressioncompletion(alf_RelationalExpressionCompletion alf_relationalexpressioncompletion) {
        this.alf_relationalexpressioncompletion = alf_relationalexpressioncompletion;
    }

}