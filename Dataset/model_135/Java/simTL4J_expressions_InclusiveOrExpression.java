





import java.util.List;
import java.util.ArrayList;

public class simTL4J_expressions_InclusiveOrExpression extends ConditionalAndExpressionChild {






    private List<InclusiveOrExpressionChild> inclusiveorexpressionchilds;


    public simTL4J_expressions_InclusiveOrExpression(
    ) {
        super(
        );
        this.inclusiveorexpressionchilds = new ArrayList<>();
    }

    public simTL4J_expressions_InclusiveOrExpression(
        ArrayList<InclusiveOrExpressionChild> inclusiveorexpressionchilds    ) {
        this.inclusiveorexpressionchilds = inclusiveorexpressionchilds;
    }


    public List<InclusiveOrExpressionChild> getInclusiveorexpressionchilds() {
        return inclusiveorexpressionchilds;
    }

    public void addInclusiveorexpressionchild(Inclusiveorexpressionchild inclusiveorexpressionchild) {
        this.inclusiveorexpressionchilds.add(inclusiveorexpressionchild);
    }

}