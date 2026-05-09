





import java.util.List;
import java.util.ArrayList;

public class DOM_QualifiedName extends Name {






    private DOM_SimpleName dom_simplename;




    private DOM_Name dom_name;


    public DOM_QualifiedName(
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
    public DOM_Name getDom_name() {
        return dom_name;
    }

    public void setDom_name(DOM_Name dom_name) {
        this.dom_name = dom_name;
    }

}