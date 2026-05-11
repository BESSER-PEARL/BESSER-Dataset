





import java.util.List;
import java.util.ArrayList;

public class dom_NewExpression extends Expression {






    private List<dom_Expression> dom_expressions;


    public dom_NewExpression(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public dom_NewExpression(
        ArrayList<dom_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}