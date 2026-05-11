





import java.util.List;
import java.util.ArrayList;

public class ast_Statement  {






    private ast_DoWhileStatement ast_dowhilestatement;




    private ast_IfStatement ast_ifstatement;




    private ast_IfStatement ast_ifstatement;




    private ast_WhileStatement ast_whilestatement;




    private ast_Compound ast_compound;




    private ast_ForStatement ast_forstatement;


    public ast_Statement(
    ) {
    }



    public ast_DoWhileStatement getAst_dowhilestatement() {
        return ast_dowhilestatement;
    }

    public void setAst_dowhilestatement(ast_DoWhileStatement ast_dowhilestatement) {
        this.ast_dowhilestatement = ast_dowhilestatement;
    }
    public ast_IfStatement getAst_ifstatement() {
        return ast_ifstatement;
    }

    public void setAst_ifstatement(ast_IfStatement ast_ifstatement) {
        this.ast_ifstatement = ast_ifstatement;
    }
    public ast_IfStatement getAst_ifstatement() {
        return ast_ifstatement;
    }

    public void setAst_ifstatement(ast_IfStatement ast_ifstatement) {
        this.ast_ifstatement = ast_ifstatement;
    }
    public ast_WhileStatement getAst_whilestatement() {
        return ast_whilestatement;
    }

    public void setAst_whilestatement(ast_WhileStatement ast_whilestatement) {
        this.ast_whilestatement = ast_whilestatement;
    }
    public ast_Compound getAst_compound() {
        return ast_compound;
    }

    public void setAst_compound(ast_Compound ast_compound) {
        this.ast_compound = ast_compound;
    }
    public ast_ForStatement getAst_forstatement() {
        return ast_forstatement;
    }

    public void setAst_forstatement(ast_ForStatement ast_forstatement) {
        this.ast_forstatement = ast_forstatement;
    }

}