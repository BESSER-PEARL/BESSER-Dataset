





import java.util.List;
import java.util.ArrayList;

public class delphi_exceptionBlock extends CSTrace {






    private List<delphi_ident> delphi_idents;




    private List<delphi_statement> delphi_statements;




    private delphi_tryStmt delphi_trystmt;




    private List<delphi_type> delphi_types;




    private delphi_stmtList delphi_stmtlist;


    public delphi_exceptionBlock(
    ) {
        super(
        );
        this.delphi_idents = new ArrayList<>();
        this.delphi_statements = new ArrayList<>();
        this.delphi_types = new ArrayList<>();
    }

    public delphi_exceptionBlock(
        ArrayList<delphi_ident> delphi_idents,        ArrayList<delphi_statement> delphi_statements,        ArrayList<delphi_type> delphi_types    ) {
        this.delphi_idents = delphi_idents;
        this.delphi_statements = delphi_statements;
        this.delphi_types = delphi_types;
    }


    public List<delphi_ident> getDelphi_idents() {
        return delphi_idents;
    }

    public void addDelphi_ident(Delphi_ident delphi_ident) {
        this.delphi_idents.add(delphi_ident);
    }
    public List<delphi_statement> getDelphi_statements() {
        return delphi_statements;
    }

    public void addDelphi_statement(Delphi_statement delphi_statement) {
        this.delphi_statements.add(delphi_statement);
    }
    public delphi_tryStmt getDelphi_trystmt() {
        return delphi_trystmt;
    }

    public void setDelphi_trystmt(delphi_tryStmt delphi_trystmt) {
        this.delphi_trystmt = delphi_trystmt;
    }
    public List<delphi_type> getDelphi_types() {
        return delphi_types;
    }

    public void addDelphi_type(Delphi_type delphi_type) {
        this.delphi_types.add(delphi_type);
    }
    public delphi_stmtList getDelphi_stmtlist() {
        return delphi_stmtlist;
    }

    public void setDelphi_stmtlist(delphi_stmtList delphi_stmtlist) {
        this.delphi_stmtlist = delphi_stmtlist;
    }

}