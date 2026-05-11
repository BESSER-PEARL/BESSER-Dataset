





import java.util.List;
import java.util.ArrayList;

public class expressions_Model  {






    private List<expressions_Expression> expressions_expressions;


    public expressions_Model(
    ) {
        this.expressions_expressions = new ArrayList<>();
    }

    public expressions_Model(
        ArrayList<expressions_Expression> expressions_expressions    ) {
        this.expressions_expressions = expressions_expressions;
    }


    public List<expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }

}