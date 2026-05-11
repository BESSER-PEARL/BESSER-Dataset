





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_VariableArrayOrFunctionRef extends Expression {






    private List<expressionDSL_Expression> expressiondsl_expressions;




    private expressionDSL_Named expressiondsl_named;


    public expressionDSL_VariableArrayOrFunctionRef(
    ) {
        super(
        );
        this.expressiondsl_expressions = new ArrayList<>();
    }

    public expressionDSL_VariableArrayOrFunctionRef(
        ArrayList<expressionDSL_Expression> expressiondsl_expressions    ) {
        this.expressiondsl_expressions = expressiondsl_expressions;
    }


    public List<expressionDSL_Expression> getExpressiondsl_expressions() {
        return expressiondsl_expressions;
    }

    public void addExpressiondsl_expression(Expressiondsl_expression expressiondsl_expression) {
        this.expressiondsl_expressions.add(expressiondsl_expression);
    }
    public expressionDSL_Named getExpressiondsl_named() {
        return expressiondsl_named;
    }

    public void setExpressiondsl_named(expressionDSL_Named expressiondsl_named) {
        this.expressiondsl_named = expressiondsl_named;
    }

}