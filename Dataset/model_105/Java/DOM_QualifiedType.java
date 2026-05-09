





import java.util.List;
import java.util.ArrayList;

public class DOM_QualifiedType extends Type {






    private DOM_Type dom_type;




    private DOM_SimpleName dom_simplename;


    public DOM_QualifiedType(
    ) {
        super(
        );
    }



    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }
    public DOM_SimpleName getDom_simplename() {
        return dom_simplename;
    }

    public void setDom_simplename(DOM_SimpleName dom_simplename) {
        this.dom_simplename = dom_simplename;
    }

}