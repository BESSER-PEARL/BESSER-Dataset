





import java.util.List;
import java.util.ArrayList;

public class dbl_QuotedStatements extends QuotedCode {






    private List<dbl_Statement> dbl_statements;


    public dbl_QuotedStatements(
    ) {
        super(
        );
        this.dbl_statements = new ArrayList<>();
    }

    public dbl_QuotedStatements(
        ArrayList<dbl_Statement> dbl_statements    ) {
        this.dbl_statements = dbl_statements;
    }


    public List<dbl_Statement> getDbl_statements() {
        return dbl_statements;
    }

    public void addDbl_statement(Dbl_statement dbl_statement) {
        this.dbl_statements.add(dbl_statement);
    }

}