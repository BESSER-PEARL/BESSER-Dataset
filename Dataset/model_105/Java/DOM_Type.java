





import java.util.List;
import java.util.ArrayList;

public class DOM_Type extends ASTNode {






    private DOM_MethodRefParameter dom_methodrefparameter;




    private DOM_TypeParameter dom_typeparameter;


    public DOM_Type(
    ) {
        super(
        );
    }



    public DOM_MethodRefParameter getDom_methodrefparameter() {
        return dom_methodrefparameter;
    }

    public void setDom_methodrefparameter(DOM_MethodRefParameter dom_methodrefparameter) {
        this.dom_methodrefparameter = dom_methodrefparameter;
    }
    public DOM_TypeParameter getDom_typeparameter() {
        return dom_typeparameter;
    }

    public void setDom_typeparameter(DOM_TypeParameter dom_typeparameter) {
        this.dom_typeparameter = dom_typeparameter;
    }

}