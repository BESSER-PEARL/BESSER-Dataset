





import java.util.List;
import java.util.ArrayList;

public class DOM_SuperMethodInvocation extends Expression {






    private DOM_Name dom_name;




    private List<DOM_Type> dom_types;




    private DOM_Name dom_name;




    private List<DOM_Expression> dom_expressions;


    public DOM_SuperMethodInvocation(
    ) {
        super(
        );
        this.dom_types = new ArrayList<>();
        this.dom_expressions = new ArrayList<>();
    }

    public DOM_SuperMethodInvocation(
        ArrayList<DOM_Type> dom_types,        ArrayList<DOM_Expression> dom_expressions    ) {
        this.dom_types = dom_types;
        this.dom_expressions = dom_expressions;
    }


    public DOM_Name getDom_name() {
        return dom_name;
    }

    public void setDom_name(DOM_Name dom_name) {
        this.dom_name = dom_name;
    }
    public List<DOM_Type> getDom_types() {
        return dom_types;
    }

    public void addDom_type(Dom_type dom_type) {
        this.dom_types.add(dom_type);
    }
    public DOM_Name getDom_name() {
        return dom_name;
    }

    public void setDom_name(DOM_Name dom_name) {
        this.dom_name = dom_name;
    }
    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}