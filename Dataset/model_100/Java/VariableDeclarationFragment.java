





import java.util.List;
import java.util.ArrayList;

public class VariableDeclarationFragment  {






    private DOM_FieldDeclaration dom_fielddeclaration;




    private DOM_VariableDeclarationExpression dom_variabledeclarationexpression;


    public VariableDeclarationFragment(
    ) {
    }



    public DOM_FieldDeclaration getDom_fielddeclaration() {
        return dom_fielddeclaration;
    }

    public void setDom_fielddeclaration(DOM_FieldDeclaration dom_fielddeclaration) {
        this.dom_fielddeclaration = dom_fielddeclaration;
    }
    public DOM_VariableDeclarationExpression getDom_variabledeclarationexpression() {
        return dom_variabledeclarationexpression;
    }

    public void setDom_variabledeclarationexpression(DOM_VariableDeclarationExpression dom_variabledeclarationexpression) {
        this.dom_variabledeclarationexpression = dom_variabledeclarationexpression;
    }

}