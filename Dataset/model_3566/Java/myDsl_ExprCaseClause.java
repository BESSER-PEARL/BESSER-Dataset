





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExprCaseClause  {






    private myDsl_StatementList mydsl_statementlist;




    private myDsl_ExprSwitchStmt mydsl_exprswitchstmt;


    public myDsl_ExprCaseClause(
    ) {
    }



    public myDsl_StatementList getMydsl_statementlist() {
        return mydsl_statementlist;
    }

    public void setMydsl_statementlist(myDsl_StatementList mydsl_statementlist) {
        this.mydsl_statementlist = mydsl_statementlist;
    }
    public myDsl_ExprSwitchStmt getMydsl_exprswitchstmt() {
        return mydsl_exprswitchstmt;
    }

    public void setMydsl_exprswitchstmt(myDsl_ExprSwitchStmt mydsl_exprswitchstmt) {
        this.mydsl_exprswitchstmt = mydsl_exprswitchstmt;
    }

}