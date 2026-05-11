





import java.util.List;
import java.util.ArrayList;

public class alf_InclusiveOrExpressionCompletion  {






    private alf_ExclusiveOrExpressionCompletion alf_exclusiveorexpressioncompletion;




    private List<alf_ExclusiveOrExpression> alf_exclusiveorexpressions;




    private alf_InclusiveOrExpression alf_inclusiveorexpression;


    public alf_InclusiveOrExpressionCompletion(
    ) {
        this.alf_exclusiveorexpressions = new ArrayList<>();
    }

    public alf_InclusiveOrExpressionCompletion(
        ArrayList<alf_ExclusiveOrExpression> alf_exclusiveorexpressions    ) {
        this.alf_exclusiveorexpressions = alf_exclusiveorexpressions;
    }


    public alf_ExclusiveOrExpressionCompletion getAlf_exclusiveorexpressioncompletion() {
        return alf_exclusiveorexpressioncompletion;
    }

    public void setAlf_exclusiveorexpressioncompletion(alf_ExclusiveOrExpressionCompletion alf_exclusiveorexpressioncompletion) {
        this.alf_exclusiveorexpressioncompletion = alf_exclusiveorexpressioncompletion;
    }
    public List<alf_ExclusiveOrExpression> getAlf_exclusiveorexpressions() {
        return alf_exclusiveorexpressions;
    }

    public void addAlf_exclusiveorexpression(Alf_exclusiveorexpression alf_exclusiveorexpression) {
        this.alf_exclusiveorexpressions.add(alf_exclusiveorexpression);
    }
    public alf_InclusiveOrExpression getAlf_inclusiveorexpression() {
        return alf_inclusiveorexpression;
    }

    public void setAlf_inclusiveorexpression(alf_InclusiveOrExpression alf_inclusiveorexpression) {
        this.alf_inclusiveorexpression = alf_inclusiveorexpression;
    }

}