





import java.util.List;
import java.util.ArrayList;

public class dom_VariableStatement extends Statement, IForInitializer {






    private List<dom_VariableDeclaration> dom_variabledeclarations;


    public dom_VariableStatement(
    ) {
        super(
        );
        this.dom_variabledeclarations = new ArrayList<>();
    }

    public dom_VariableStatement(
        ArrayList<dom_VariableDeclaration> dom_variabledeclarations    ) {
        this.dom_variabledeclarations = dom_variabledeclarations;
    }


    public List<dom_VariableDeclaration> getDom_variabledeclarations() {
        return dom_variabledeclarations;
    }

    public void addDom_variabledeclaration(Dom_variabledeclaration dom_variabledeclaration) {
        this.dom_variabledeclarations.add(dom_variabledeclaration);
    }

}