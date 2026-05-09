





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ASTNode  {






    private JDTAST_Comment jdtast_comment;




    private JDTAST_AST jdtast_ast;




    private JDTAST_TagElement jdtast_tagelement;


    public JDTAST_ASTNode(
    ) {
    }



    public JDTAST_Comment getJdtast_comment() {
        return jdtast_comment;
    }

    public void setJdtast_comment(JDTAST_Comment jdtast_comment) {
        this.jdtast_comment = jdtast_comment;
    }
    public JDTAST_AST getJdtast_ast() {
        return jdtast_ast;
    }

    public void setJdtast_ast(JDTAST_AST jdtast_ast) {
        this.jdtast_ast = jdtast_ast;
    }
    public JDTAST_TagElement getJdtast_tagelement() {
        return jdtast_tagelement;
    }

    public void setJdtast_tagelement(JDTAST_TagElement jdtast_tagelement) {
        this.jdtast_tagelement = jdtast_tagelement;
    }

}