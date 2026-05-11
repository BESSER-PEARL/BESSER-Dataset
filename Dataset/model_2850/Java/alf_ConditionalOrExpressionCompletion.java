





import java.util.List;
import java.util.ArrayList;

public class alf_ConditionalOrExpressionCompletion  {






    private alf_ConditionalExpressionCompletion alf_conditionalexpressioncompletion;




    private List<alf_ConditionalAndExpression> alf_conditionalandexpressions;




    private alf_ConditionalAndExpressionCompletion alf_conditionalandexpressioncompletion;




    private alf_ConditionalOrExpression alf_conditionalorexpression;


    public alf_ConditionalOrExpressionCompletion(
    ) {
        this.alf_conditionalandexpressions = new ArrayList<>();
    }

    public alf_ConditionalOrExpressionCompletion(
        ArrayList<alf_ConditionalAndExpression> alf_conditionalandexpressions    ) {
        this.alf_conditionalandexpressions = alf_conditionalandexpressions;
    }


    public alf_ConditionalExpressionCompletion getAlf_conditionalexpressioncompletion() {
        return alf_conditionalexpressioncompletion;
    }

    public void setAlf_conditionalexpressioncompletion(alf_ConditionalExpressionCompletion alf_conditionalexpressioncompletion) {
        this.alf_conditionalexpressioncompletion = alf_conditionalexpressioncompletion;
    }
    public List<alf_ConditionalAndExpression> getAlf_conditionalandexpressions() {
        return alf_conditionalandexpressions;
    }

    public void addAlf_conditionalandexpression(Alf_conditionalandexpression alf_conditionalandexpression) {
        this.alf_conditionalandexpressions.add(alf_conditionalandexpression);
    }
    public alf_ConditionalAndExpressionCompletion getAlf_conditionalandexpressioncompletion() {
        return alf_conditionalandexpressioncompletion;
    }

    public void setAlf_conditionalandexpressioncompletion(alf_ConditionalAndExpressionCompletion alf_conditionalandexpressioncompletion) {
        this.alf_conditionalandexpressioncompletion = alf_conditionalandexpressioncompletion;
    }
    public alf_ConditionalOrExpression getAlf_conditionalorexpression() {
        return alf_conditionalorexpression;
    }

    public void setAlf_conditionalorexpression(alf_ConditionalOrExpression alf_conditionalorexpression) {
        this.alf_conditionalorexpression = alf_conditionalorexpression;
    }

}