





import java.util.List;
import java.util.ArrayList;

public class ast_ClassifierMemberStatement extends EJBase {






    private ast_ClassBlock ast_classblock;




    private ast_ClassifierStatement ast_classifierstatement;


    public ast_ClassifierMemberStatement(
    ) {
        super(
        );
    }



    public ast_ClassBlock getAst_classblock() {
        return ast_classblock;
    }

    public void setAst_classblock(ast_ClassBlock ast_classblock) {
        this.ast_classblock = ast_classblock;
    }
    public ast_ClassifierStatement getAst_classifierstatement() {
        return ast_classifierstatement;
    }

    public void setAst_classifierstatement(ast_ClassifierStatement ast_classifierstatement) {
        this.ast_classifierstatement = ast_classifierstatement;
    }

}