





import java.util.List;
import java.util.ArrayList;

public class delphi_stmtList extends CSTrace {






    private delphi_tryStmt delphi_trystmt;




    private delphi_compoundStmt delphi_compoundstmt;




    private delphi_initSection delphi_initsection;




    private delphi_caseStmt delphi_casestmt;




    private delphi_tryStmt delphi_trystmt;




    private delphi_initSection delphi_initsection;




    private List<delphi_statement> delphi_statements;


    public delphi_stmtList(
    ) {
        super(
        );
        this.delphi_statements = new ArrayList<>();
    }

    public delphi_stmtList(
        ArrayList<delphi_statement> delphi_statements    ) {
        this.delphi_statements = delphi_statements;
    }


    public delphi_tryStmt getDelphi_trystmt() {
        return delphi_trystmt;
    }

    public void setDelphi_trystmt(delphi_tryStmt delphi_trystmt) {
        this.delphi_trystmt = delphi_trystmt;
    }
    public delphi_compoundStmt getDelphi_compoundstmt() {
        return delphi_compoundstmt;
    }

    public void setDelphi_compoundstmt(delphi_compoundStmt delphi_compoundstmt) {
        this.delphi_compoundstmt = delphi_compoundstmt;
    }
    public delphi_initSection getDelphi_initsection() {
        return delphi_initsection;
    }

    public void setDelphi_initsection(delphi_initSection delphi_initsection) {
        this.delphi_initsection = delphi_initsection;
    }
    public delphi_caseStmt getDelphi_casestmt() {
        return delphi_casestmt;
    }

    public void setDelphi_casestmt(delphi_caseStmt delphi_casestmt) {
        this.delphi_casestmt = delphi_casestmt;
    }
    public delphi_tryStmt getDelphi_trystmt() {
        return delphi_trystmt;
    }

    public void setDelphi_trystmt(delphi_tryStmt delphi_trystmt) {
        this.delphi_trystmt = delphi_trystmt;
    }
    public delphi_initSection getDelphi_initsection() {
        return delphi_initsection;
    }

    public void setDelphi_initsection(delphi_initSection delphi_initsection) {
        this.delphi_initsection = delphi_initsection;
    }
    public List<delphi_statement> getDelphi_statements() {
        return delphi_statements;
    }

    public void addDelphi_statement(Delphi_statement delphi_statement) {
        this.delphi_statements.add(delphi_statement);
    }

}