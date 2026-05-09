





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodRef extends ASTNode {






    private List<DOM_MethodRefParameter> dom_methodrefparameters;


    public DOM_MethodRef(
    ) {
        super(
        );
        this.dom_methodrefparameters = new ArrayList<>();
    }

    public DOM_MethodRef(
        ArrayList<DOM_MethodRefParameter> dom_methodrefparameters    ) {
        this.dom_methodrefparameters = dom_methodrefparameters;
    }


    public List<DOM_MethodRefParameter> getDom_methodrefparameters() {
        return dom_methodrefparameters;
    }

    public void addDom_methodrefparameter(Dom_methodrefparameter dom_methodrefparameter) {
        this.dom_methodrefparameters.add(dom_methodrefparameter);
    }

}