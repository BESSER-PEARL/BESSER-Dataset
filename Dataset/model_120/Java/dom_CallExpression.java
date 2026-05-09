





import java.util.List;
import java.util.ArrayList;

public class dom_CallExpression extends Expression {






    private List<dom_Expression> dom_expressions;




    private dom_Expression dom_expression;


    public dom_CallExpression(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public dom_CallExpression(
        ArrayList<dom_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}