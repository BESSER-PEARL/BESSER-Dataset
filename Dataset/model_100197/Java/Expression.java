





import java.util.List;
import java.util.ArrayList;

public class Expression  {






    private SQLDML_BinaryExp sqldml_binaryexp;




    private SQLDML_NotExp sqldml_notexp;




    private SQLDML_BinaryExp sqldml_binaryexp;




    private SQLDML_NotExp sqldml_notexp;




    private SQLDML_WhereClause sqldml_whereclause;




    private SQLDML_InsertStmt sqldml_insertstmt;




    private SQLDML_QueryStmtCol sqldml_querystmtcol;


    public Expression(
    ) {
    }



    public SQLDML_BinaryExp getSqldml_binaryexp() {
        return sqldml_binaryexp;
    }

    public void setSqldml_binaryexp(SQLDML_BinaryExp sqldml_binaryexp) {
        this.sqldml_binaryexp = sqldml_binaryexp;
    }
    public SQLDML_NotExp getSqldml_notexp() {
        return sqldml_notexp;
    }

    public void setSqldml_notexp(SQLDML_NotExp sqldml_notexp) {
        this.sqldml_notexp = sqldml_notexp;
    }
    public SQLDML_BinaryExp getSqldml_binaryexp() {
        return sqldml_binaryexp;
    }

    public void setSqldml_binaryexp(SQLDML_BinaryExp sqldml_binaryexp) {
        this.sqldml_binaryexp = sqldml_binaryexp;
    }
    public SQLDML_NotExp getSqldml_notexp() {
        return sqldml_notexp;
    }

    public void setSqldml_notexp(SQLDML_NotExp sqldml_notexp) {
        this.sqldml_notexp = sqldml_notexp;
    }
    public SQLDML_WhereClause getSqldml_whereclause() {
        return sqldml_whereclause;
    }

    public void setSqldml_whereclause(SQLDML_WhereClause sqldml_whereclause) {
        this.sqldml_whereclause = sqldml_whereclause;
    }
    public SQLDML_InsertStmt getSqldml_insertstmt() {
        return sqldml_insertstmt;
    }

    public void setSqldml_insertstmt(SQLDML_InsertStmt sqldml_insertstmt) {
        this.sqldml_insertstmt = sqldml_insertstmt;
    }
    public SQLDML_QueryStmtCol getSqldml_querystmtcol() {
        return sqldml_querystmtcol;
    }

    public void setSqldml_querystmtcol(SQLDML_QueryStmtCol sqldml_querystmtcol) {
        this.sqldml_querystmtcol = sqldml_querystmtcol;
    }

}