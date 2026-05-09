





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodInvocation extends Expression {






    private DOM_Expression dom_expression;




    private List<DOM_Expression> dom_expressions;




    private DOM_SimpleName dom_simplename;




    private List<DOM_Type> dom_types;




    private DOM_IMethod dom_imethod;


    public DOM_MethodInvocation(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
        this.dom_types = new ArrayList<>();
    }

    public DOM_MethodInvocation(
        ArrayList<DOM_Expression> dom_expressions,        ArrayList<DOM_Type> dom_types    ) {
        this.dom_expressions = dom_expressions;
        this.dom_types = dom_types;
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
    public DOM_SimpleName getDom_simplename() {
        return dom_simplename;
    }

    public void setDom_simplename(DOM_SimpleName dom_simplename) {
        this.dom_simplename = dom_simplename;
    }
    public List<DOM_Type> getDom_types() {
        return dom_types;
    }

    public void addDom_type(Dom_type dom_type) {
        this.dom_types.add(dom_type);
    }
    public DOM_IMethod getDom_imethod() {
        return dom_imethod;
    }

    public void setDom_imethod(DOM_IMethod dom_imethod) {
        this.dom_imethod = dom_imethod;
    }

}