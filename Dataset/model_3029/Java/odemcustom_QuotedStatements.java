





import java.util.List;
import java.util.ArrayList;

public class odemcustom_QuotedStatements extends QuotedCode {






    private List<odemcustom_Statement> odemcustom_statements;


    public odemcustom_QuotedStatements(
    ) {
        super(
        );
        this.odemcustom_statements = new ArrayList<>();
    }

    public odemcustom_QuotedStatements(
        ArrayList<odemcustom_Statement> odemcustom_statements    ) {
        this.odemcustom_statements = odemcustom_statements;
    }


    public List<odemcustom_Statement> getOdemcustom_statements() {
        return odemcustom_statements;
    }

    public void addOdemcustom_statement(Odemcustom_statement odemcustom_statement) {
        this.odemcustom_statements.add(odemcustom_statement);
    }

}