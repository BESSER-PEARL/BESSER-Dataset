





import java.util.List;
import java.util.ArrayList;

public class VariableDeclarationFragment  {






    private DOM_VariableDeclarationExpression dom_variabledeclarationexpression;




    private DOM_FieldDeclaration dom_fielddeclaration;




    private DOM_VariableDeclarationStatement dom_variabledeclarationstatement;


    public VariableDeclarationFragment(
    ) {
    }



    public DOM_VariableDeclarationExpression getDom_variabledeclarationexpression() {
        return dom_variabledeclarationexpression;
    }

    public void setDom_variabledeclarationexpression(DOM_VariableDeclarationExpression dom_variabledeclarationexpression) {
        this.dom_variabledeclarationexpression = dom_variabledeclarationexpression;
    }
    public DOM_FieldDeclaration getDom_fielddeclaration() {
        return dom_fielddeclaration;
    }

    public void setDom_fielddeclaration(DOM_FieldDeclaration dom_fielddeclaration) {
        this.dom_fielddeclaration = dom_fielddeclaration;
    }
    public DOM_VariableDeclarationStatement getDom_variabledeclarationstatement() {
        return dom_variabledeclarationstatement;
    }

    public void setDom_variabledeclarationstatement(DOM_VariableDeclarationStatement dom_variabledeclarationstatement) {
        this.dom_variabledeclarationstatement = dom_variabledeclarationstatement;
    }

}