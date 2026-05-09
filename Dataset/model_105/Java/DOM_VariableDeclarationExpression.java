





import java.util.List;
import java.util.ArrayList;

public class DOM_VariableDeclarationExpression extends Expression {






    private DOM_Type dom_type;




    private List<DOM_VariableDeclarationFragment> dom_variabledeclarationfragments;




    private List<DOM_ExtendedModifier> dom_extendedmodifiers;


    public DOM_VariableDeclarationExpression(
    ) {
        super(
        );
        this.dom_variabledeclarationfragments = new ArrayList<>();
        this.dom_extendedmodifiers = new ArrayList<>();
    }

    public DOM_VariableDeclarationExpression(
        ArrayList<DOM_VariableDeclarationFragment> dom_variabledeclarationfragments,        ArrayList<DOM_ExtendedModifier> dom_extendedmodifiers    ) {
        this.dom_variabledeclarationfragments = dom_variabledeclarationfragments;
        this.dom_extendedmodifiers = dom_extendedmodifiers;
    }


    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }
    public List<DOM_VariableDeclarationFragment> getDom_variabledeclarationfragments() {
        return dom_variabledeclarationfragments;
    }

    public void addDom_variabledeclarationfragment(Dom_variabledeclarationfragment dom_variabledeclarationfragment) {
        this.dom_variabledeclarationfragments.add(dom_variabledeclarationfragment);
    }
    public List<DOM_ExtendedModifier> getDom_extendedmodifiers() {
        return dom_extendedmodifiers;
    }

    public void addDom_extendedmodifier(Dom_extendedmodifier dom_extendedmodifier) {
        this.dom_extendedmodifiers.add(dom_extendedmodifier);
    }

}