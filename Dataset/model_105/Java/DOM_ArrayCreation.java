





import java.util.List;
import java.util.ArrayList;

public class DOM_ArrayCreation extends Expression {






    private List<DOM_Expression> dom_expressions;


    public DOM_ArrayCreation(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public DOM_ArrayCreation(
        ArrayList<DOM_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}