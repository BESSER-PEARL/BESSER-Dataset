





import java.util.List;
import java.util.ArrayList;

public class sql_groupBy_GroupByExpression  {






    private List<expression_Expression> expression_expressions;


    public sql_groupBy_GroupByExpression(
    ) {
        this.expression_expressions = new ArrayList<>();
    }

    public sql_groupBy_GroupByExpression(
        ArrayList<expression_Expression> expression_expressions    ) {
        this.expression_expressions = expression_expressions;
    }


    public List<expression_Expression> getExpression_expressions() {
        return expression_expressions;
    }

    public void addExpression_expression(Expression_expression expression_expression) {
        this.expression_expressions.add(expression_expression);
    }

}