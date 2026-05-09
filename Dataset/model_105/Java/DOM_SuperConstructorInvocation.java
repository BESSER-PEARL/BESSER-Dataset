





import java.util.List;
import java.util.ArrayList;

public class DOM_SuperConstructorInvocation extends Statement {






    private List<DOM_Expression> dom_expressions;




    private List<DOM_Type> dom_types;




    private DOM_Expression dom_expression;


    public DOM_SuperConstructorInvocation(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
        this.dom_types = new ArrayList<>();
    }

    public DOM_SuperConstructorInvocation(
        ArrayList<DOM_Expression> dom_expressions,        ArrayList<DOM_Type> dom_types    ) {
        this.dom_expressions = dom_expressions;
        this.dom_types = dom_types;
    }


    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }
    public List<DOM_Type> getDom_types() {
        return dom_types;
    }

    public void addDom_type(Dom_type dom_type) {
        this.dom_types.add(dom_type);
    }
    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}