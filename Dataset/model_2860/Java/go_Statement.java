





import java.util.List;
import java.util.ArrayList;

public class go_Statement  {

    private String FallthroughStmt;





    private go_Block go_block;




    private go_StatementList go_statementlist;


    public go_Statement(
        String FallthroughStmt    ) {
        this.FallthroughStmt = FallthroughStmt;
    }


    public String getFallthroughstmt() {
        return FallthroughStmt;
    }

    public void setFallthroughstmt(String FallthroughStmt) {
        this.FallthroughStmt = FallthroughStmt;
    }

    public go_Block getGo_block() {
        return go_block;
    }

    public void setGo_block(go_Block go_block) {
        this.go_block = go_block;
    }
    public go_StatementList getGo_statementlist() {
        return go_statementlist;
    }

    public void setGo_statementlist(go_StatementList go_statementlist) {
        this.go_statementlist = go_statementlist;
    }

}