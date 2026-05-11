





import java.util.List;
import java.util.ArrayList;

public class go_CommClause  {






    private go_SelectStmt go_selectstmt;




    private go_StatementList go_statementlist;


    public go_CommClause(
    ) {
    }



    public go_SelectStmt getGo_selectstmt() {
        return go_selectstmt;
    }

    public void setGo_selectstmt(go_SelectStmt go_selectstmt) {
        this.go_selectstmt = go_selectstmt;
    }
    public go_StatementList getGo_statementlist() {
        return go_statementlist;
    }

    public void setGo_statementlist(go_StatementList go_statementlist) {
        this.go_statementlist = go_statementlist;
    }

}