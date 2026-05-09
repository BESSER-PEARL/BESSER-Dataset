





import java.util.List;
import java.util.ArrayList;

public class Block  {






    private DOM_MethodDeclaration dom_methoddeclaration;




    private DOM_Initializer dom_initializer;




    private DOM_CatchClause dom_catchclause;


    public Block(
    ) {
    }



    public DOM_MethodDeclaration getDom_methoddeclaration() {
        return dom_methoddeclaration;
    }

    public void setDom_methoddeclaration(DOM_MethodDeclaration dom_methoddeclaration) {
        this.dom_methoddeclaration = dom_methoddeclaration;
    }
    public DOM_Initializer getDom_initializer() {
        return dom_initializer;
    }

    public void setDom_initializer(DOM_Initializer dom_initializer) {
        this.dom_initializer = dom_initializer;
    }
    public DOM_CatchClause getDom_catchclause() {
        return dom_catchclause;
    }

    public void setDom_catchclause(DOM_CatchClause dom_catchclause) {
        this.dom_catchclause = dom_catchclause;
    }

}