





import java.util.List;
import java.util.ArrayList;

public class jcl_expressions_ConditionalAndExpression extends ConditionalOrExpressionChild {






    private List<ConditionalAndExpressionChild> conditionalandexpressionchilds;


    public jcl_expressions_ConditionalAndExpression(
    ) {
        super(
        );
        this.conditionalandexpressionchilds = new ArrayList<>();
    }

    public jcl_expressions_ConditionalAndExpression(
        ArrayList<ConditionalAndExpressionChild> conditionalandexpressionchilds    ) {
        this.conditionalandexpressionchilds = conditionalandexpressionchilds;
    }


    public List<ConditionalAndExpressionChild> getConditionalandexpressionchilds() {
        return conditionalandexpressionchilds;
    }

    public void addConditionalandexpressionchild(Conditionalandexpressionchild conditionalandexpressionchild) {
        this.conditionalandexpressionchilds.add(conditionalandexpressionchild);
    }

}