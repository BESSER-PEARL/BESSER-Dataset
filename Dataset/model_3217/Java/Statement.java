





import java.util.List;
import java.util.ArrayList;

public class Statement  {






    private gast_statements_LoopStatement gast_statements_loopstatement;




    private gast_statements_Branch gast_statements_branch;




    private gast_statements_BlockStatement gast_statements_blockstatement;


    public Statement(
    ) {
    }



    public gast_statements_LoopStatement getGast_statements_loopstatement() {
        return gast_statements_loopstatement;
    }

    public void setGast_statements_loopstatement(gast_statements_LoopStatement gast_statements_loopstatement) {
        this.gast_statements_loopstatement = gast_statements_loopstatement;
    }
    public gast_statements_Branch getGast_statements_branch() {
        return gast_statements_branch;
    }

    public void setGast_statements_branch(gast_statements_Branch gast_statements_branch) {
        this.gast_statements_branch = gast_statements_branch;
    }
    public gast_statements_BlockStatement getGast_statements_blockstatement() {
        return gast_statements_blockstatement;
    }

    public void setGast_statements_blockstatement(gast_statements_BlockStatement gast_statements_blockstatement) {
        this.gast_statements_blockstatement = gast_statements_blockstatement;
    }

}