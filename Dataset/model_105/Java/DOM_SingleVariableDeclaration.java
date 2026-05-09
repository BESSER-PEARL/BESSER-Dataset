





import java.util.List;
import java.util.ArrayList;

public class DOM_SingleVariableDeclaration extends VariableDeclaration {

    private String varargs;





    private List<DOM_ExtendedModifier> dom_extendedmodifiers;




    private DOM_CatchClause dom_catchclause;




    private DOM_Type dom_type;


    public DOM_SingleVariableDeclaration(
        String varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.dom_extendedmodifiers = new ArrayList<>();
    }

    public DOM_SingleVariableDeclaration(
        String varargs        ArrayList<DOM_ExtendedModifier> dom_extendedmodifiers    ) {
        this.varargs = varargs;
        this.dom_extendedmodifiers = dom_extendedmodifiers;
    }

    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }

    public List<DOM_ExtendedModifier> getDom_extendedmodifiers() {
        return dom_extendedmodifiers;
    }

    public void addDom_extendedmodifier(Dom_extendedmodifier dom_extendedmodifier) {
        this.dom_extendedmodifiers.add(dom_extendedmodifier);
    }
    public DOM_CatchClause getDom_catchclause() {
        return dom_catchclause;
    }

    public void setDom_catchclause(DOM_CatchClause dom_catchclause) {
        this.dom_catchclause = dom_catchclause;
    }
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }

}