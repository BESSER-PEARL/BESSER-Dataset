





import java.util.List;
import java.util.ArrayList;

public class DOM_InfixExpression extends Expression {

    private String operator;





    private DOM_Expression dom_expression;




    private List<DOM_Expression> dom_expressions;




    private DOM_Expression dom_expression;


    public DOM_InfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.dom_expressions = new ArrayList<>();
    }

    public DOM_InfixExpression(
        String operator        ArrayList<DOM_Expression> dom_expressions    ) {
        this.operator = operator;
        this.dom_expressions = dom_expressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }
    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}