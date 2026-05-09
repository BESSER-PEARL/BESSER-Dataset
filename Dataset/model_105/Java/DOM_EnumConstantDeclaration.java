





import java.util.List;
import java.util.ArrayList;

public class DOM_EnumConstantDeclaration extends BodyDeclaration {






    private DOM_SimpleName dom_simplename;




    private DOM_AnonymousClassDeclaration dom_anonymousclassdeclaration;




    private List<DOM_Expression> dom_expressions;


    public DOM_EnumConstantDeclaration(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public DOM_EnumConstantDeclaration(
        ArrayList<DOM_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public DOM_SimpleName getDom_simplename() {
        return dom_simplename;
    }

    public void setDom_simplename(DOM_SimpleName dom_simplename) {
        this.dom_simplename = dom_simplename;
    }
    public DOM_AnonymousClassDeclaration getDom_anonymousclassdeclaration() {
        return dom_anonymousclassdeclaration;
    }

    public void setDom_anonymousclassdeclaration(DOM_AnonymousClassDeclaration dom_anonymousclassdeclaration) {
        this.dom_anonymousclassdeclaration = dom_anonymousclassdeclaration;
    }
    public List<DOM_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}