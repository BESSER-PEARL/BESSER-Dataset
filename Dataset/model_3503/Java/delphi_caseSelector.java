





import java.util.List;
import java.util.ArrayList;

public class delphi_caseSelector extends CSTrace {






    private delphi_statement delphi_statement;




    private delphi_caseStmt delphi_casestmt;


    public delphi_caseSelector(
    ) {
        super(
        );
    }



    public delphi_statement getDelphi_statement() {
        return delphi_statement;
    }

    public void setDelphi_statement(delphi_statement delphi_statement) {
        this.delphi_statement = delphi_statement;
    }
    public delphi_caseStmt getDelphi_casestmt() {
        return delphi_casestmt;
    }

    public void setDelphi_casestmt(delphi_caseStmt delphi_casestmt) {
        this.delphi_casestmt = delphi_casestmt;
    }

}