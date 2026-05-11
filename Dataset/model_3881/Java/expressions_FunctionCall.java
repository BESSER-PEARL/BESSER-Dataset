





import java.util.List;
import java.util.ArrayList;

public class expressions_FunctionCall extends Expression {






    private List<expressions_Expression> expressions_expressions;




    private expressions_Function expressions_function;


    public expressions_FunctionCall(
    ) {
        super(
        );
        this.expressions_expressions = new ArrayList<>();
    }

    public expressions_FunctionCall(
        ArrayList<expressions_Expression> expressions_expressions    ) {
        this.expressions_expressions = expressions_expressions;
    }


    public List<expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }
    public expressions_Function getExpressions_function() {
        return expressions_function;
    }

    public void setExpressions_function(expressions_Function expressions_function) {
        this.expressions_function = expressions_function;
    }

}