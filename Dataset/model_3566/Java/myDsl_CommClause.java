





import java.util.List;
import java.util.ArrayList;

public class myDsl_CommClause  {






    private myDsl_SelectStmt mydsl_selectstmt;




    private myDsl_StatementList mydsl_statementlist;


    public myDsl_CommClause(
    ) {
    }



    public myDsl_SelectStmt getMydsl_selectstmt() {
        return mydsl_selectstmt;
    }

    public void setMydsl_selectstmt(myDsl_SelectStmt mydsl_selectstmt) {
        this.mydsl_selectstmt = mydsl_selectstmt;
    }
    public myDsl_StatementList getMydsl_statementlist() {
        return mydsl_statementlist;
    }

    public void setMydsl_statementlist(myDsl_StatementList mydsl_statementlist) {
        this.mydsl_statementlist = mydsl_statementlist;
    }

}