





import java.util.List;
import java.util.ArrayList;

public class expressions_ConditionalOrExpression extends ConditionalExpressionChild {






    private List<ConditionalOrExpressionChild> conditionalorexpressionchilds;


    public expressions_ConditionalOrExpression(
    ) {
        super(
        );
        this.conditionalorexpressionchilds = new ArrayList<>();
    }

    public expressions_ConditionalOrExpression(
        ArrayList<ConditionalOrExpressionChild> conditionalorexpressionchilds    ) {
        this.conditionalorexpressionchilds = conditionalorexpressionchilds;
    }


    public List<ConditionalOrExpressionChild> getConditionalorexpressionchilds() {
        return conditionalorexpressionchilds;
    }

    public void addConditionalorexpressionchild(Conditionalorexpressionchild conditionalorexpressionchild) {
        this.conditionalorexpressionchilds.add(conditionalorexpressionchild);
    }

}