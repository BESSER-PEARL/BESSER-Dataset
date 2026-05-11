





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_FunctionCall  {






    private expressionDSL_FunctionDef expressiondsl_functiondef;




    private expressionDSL_FunctionCallStatement expressiondsl_functioncallstatement;




    private List<expressionDSL_Expression> expressiondsl_expressions;


    public expressionDSL_FunctionCall(
    ) {
        this.expressiondsl_expressions = new ArrayList<>();
    }

    public expressionDSL_FunctionCall(
        ArrayList<expressionDSL_Expression> expressiondsl_expressions    ) {
        this.expressiondsl_expressions = expressiondsl_expressions;
    }


    public expressionDSL_FunctionDef getExpressiondsl_functiondef() {
        return expressiondsl_functiondef;
    }

    public void setExpressiondsl_functiondef(expressionDSL_FunctionDef expressiondsl_functiondef) {
        this.expressiondsl_functiondef = expressiondsl_functiondef;
    }
    public expressionDSL_FunctionCallStatement getExpressiondsl_functioncallstatement() {
        return expressiondsl_functioncallstatement;
    }

    public void setExpressiondsl_functioncallstatement(expressionDSL_FunctionCallStatement expressiondsl_functioncallstatement) {
        this.expressiondsl_functioncallstatement = expressiondsl_functioncallstatement;
    }
    public List<expressionDSL_Expression> getExpressiondsl_expressions() {
        return expressiondsl_expressions;
    }

    public void addExpressiondsl_expression(Expressiondsl_expression expressiondsl_expression) {
        this.expressiondsl_expressions.add(expressiondsl_expression);
    }

}