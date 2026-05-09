





import java.util.List;
import java.util.ArrayList;

public class DOM_ForStatement extends Statement {






    private DOM_Statement dom_statement;




    private List<DOM_Expression> dom_expressions;




    private DOM_Expression dom_expression;




    private List<DOM_Expression> dom_expressions;


    public DOM_ForStatement(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
        this.dom_expressions = new ArrayList<>();
    }

    public DOM_ForStatement(
        ArrayList<DOM_Expression> dom_expressions,        ArrayList<DOM_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
        this.dom_expressions = dom_expressions;
    }


    public DOM_Statement getDom_statement() {
        return dom_statement;
    }

    public void setDom_statement(DOM_Statement dom_statement) {
        this.dom_statement = dom_statement;
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
    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}