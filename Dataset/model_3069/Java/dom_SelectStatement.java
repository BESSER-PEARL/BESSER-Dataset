





import java.util.List;
import java.util.ArrayList;

public class dom_SelectStatement extends QlStatement {






    private dom_Expression dom_expression;




    private dom_Expression dom_expression;




    private List<dom_Expression> dom_expressions;




    private dom_InsertStatement dom_insertstatement;


    public dom_SelectStatement(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public dom_SelectStatement(
        ArrayList<dom_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }
    public dom_InsertStatement getDom_insertstatement() {
        return dom_insertstatement;
    }

    public void setDom_insertstatement(dom_InsertStatement dom_insertstatement) {
        this.dom_insertstatement = dom_insertstatement;
    }

}