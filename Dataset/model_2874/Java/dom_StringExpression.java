





import java.util.List;
import java.util.ArrayList;

public class dom_StringExpression extends PrimitiveExpression {

    private String val;





    private dom_Import dom_import;




    private dom_ModelDeclarationParameter dom_modeldeclarationparameter;


    public dom_StringExpression(
        String val    ) {
        super(
        );
        this.val = val;
    }


    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    public dom_Import getDom_import() {
        return dom_import;
    }

    public void setDom_import(dom_Import dom_import) {
        this.dom_import = dom_import;
    }
    public dom_ModelDeclarationParameter getDom_modeldeclarationparameter() {
        return dom_modeldeclarationparameter;
    }

    public void setDom_modeldeclarationparameter(dom_ModelDeclarationParameter dom_modeldeclarationparameter) {
        this.dom_modeldeclarationparameter = dom_modeldeclarationparameter;
    }

}