





import java.util.List;
import java.util.ArrayList;

public class alf_ConditionalAndExpressionCompletion  {






    private alf_ConditionalAndExpression alf_conditionalandexpression;




    private List<alf_InclusiveOrExpression> alf_inclusiveorexpressions;




    private alf_InclusiveOrExpressionCompletion alf_inclusiveorexpressioncompletion;


    public alf_ConditionalAndExpressionCompletion(
    ) {
        this.alf_inclusiveorexpressions = new ArrayList<>();
    }

    public alf_ConditionalAndExpressionCompletion(
        ArrayList<alf_InclusiveOrExpression> alf_inclusiveorexpressions    ) {
        this.alf_inclusiveorexpressions = alf_inclusiveorexpressions;
    }


    public alf_ConditionalAndExpression getAlf_conditionalandexpression() {
        return alf_conditionalandexpression;
    }

    public void setAlf_conditionalandexpression(alf_ConditionalAndExpression alf_conditionalandexpression) {
        this.alf_conditionalandexpression = alf_conditionalandexpression;
    }
    public List<alf_InclusiveOrExpression> getAlf_inclusiveorexpressions() {
        return alf_inclusiveorexpressions;
    }

    public void addAlf_inclusiveorexpression(Alf_inclusiveorexpression alf_inclusiveorexpression) {
        this.alf_inclusiveorexpressions.add(alf_inclusiveorexpression);
    }
    public alf_InclusiveOrExpressionCompletion getAlf_inclusiveorexpressioncompletion() {
        return alf_inclusiveorexpressioncompletion;
    }

    public void setAlf_inclusiveorexpressioncompletion(alf_InclusiveOrExpressionCompletion alf_inclusiveorexpressioncompletion) {
        this.alf_inclusiveorexpressioncompletion = alf_inclusiveorexpressioncompletion;
    }

}