





import java.util.List;
import java.util.ArrayList;

public class DOM_AnnotationTypeMemberDeclaration extends BodyDeclaration {






    private DOM_SimpleName dom_simplename;




    private DOM_Type dom_type;




    private DOM_Expression dom_expression;


    public DOM_AnnotationTypeMemberDeclaration(
    ) {
        super(
        );
    }



    public DOM_SimpleName getDom_simplename() {
        return dom_simplename;
    }

    public void setDom_simplename(DOM_SimpleName dom_simplename) {
        this.dom_simplename = dom_simplename;
    }
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }
    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}