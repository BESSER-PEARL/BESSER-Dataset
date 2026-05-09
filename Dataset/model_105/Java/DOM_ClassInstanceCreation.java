





import java.util.List;
import java.util.ArrayList;

public class DOM_ClassInstanceCreation extends Expression {






    private DOM_Type dom_type;




    private List<DOM_Expression> dom_expressions;




    private DOM_AnonymousClassDeclaration dom_anonymousclassdeclaration;




    private List<DOM_Type> dom_types;




    private DOM_Expression dom_expression;


    public DOM_ClassInstanceCreation(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
        this.dom_types = new ArrayList<>();
    }

    public DOM_ClassInstanceCreation(
        ArrayList<DOM_Expression> dom_expressions,        ArrayList<DOM_Type> dom_types    ) {
        this.dom_expressions = dom_expressions;
        this.dom_types = dom_types;
    }


    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }
    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }
    public DOM_AnonymousClassDeclaration getDom_anonymousclassdeclaration() {
        return dom_anonymousclassdeclaration;
    }

    public void setDom_anonymousclassdeclaration(DOM_AnonymousClassDeclaration dom_anonymousclassdeclaration) {
        this.dom_anonymousclassdeclaration = dom_anonymousclassdeclaration;
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