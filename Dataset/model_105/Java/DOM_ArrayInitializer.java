





import java.util.List;
import java.util.ArrayList;

public class DOM_ArrayInitializer extends Expression {






    private DOM_ArrayCreation dom_arraycreation;




    private List<DOM_Expression> dom_expressions;


    public DOM_ArrayInitializer(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public DOM_ArrayInitializer(
        ArrayList<DOM_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public DOM_ArrayCreation getDom_arraycreation() {
        return dom_arraycreation;
    }

    public void setDom_arraycreation(DOM_ArrayCreation dom_arraycreation) {
        this.dom_arraycreation = dom_arraycreation;
    }
    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}