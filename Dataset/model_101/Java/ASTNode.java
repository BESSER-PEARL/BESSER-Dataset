





import java.util.List;
import java.util.ArrayList;

public class ASTNode  {






    private DOM_AST dom_ast;




    private DOM_TagElement dom_tagelement;




    private DOM_Comment dom_comment;


    public ASTNode(
    ) {
    }



    public DOM_AST getDom_ast() {
        return dom_ast;
    }

    public void setDom_ast(DOM_AST dom_ast) {
        this.dom_ast = dom_ast;
    }
    public DOM_TagElement getDom_tagelement() {
        return dom_tagelement;
    }

    public void setDom_tagelement(DOM_TagElement dom_tagelement) {
        this.dom_tagelement = dom_tagelement;
    }
    public DOM_Comment getDom_comment() {
        return dom_comment;
    }

    public void setDom_comment(DOM_Comment dom_comment) {
        this.dom_comment = dom_comment;
    }

}