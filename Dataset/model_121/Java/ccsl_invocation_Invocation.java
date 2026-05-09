





import java.util.List;
import java.util.ArrayList;

public class ccsl_invocation_Invocation extends Statement {

    private String argsKind;





    private List<statements_Statement> statements_statements;


    public ccsl_invocation_Invocation(
        String argsKind    ) {
        super(
        );
        this.argsKind = argsKind;
        this.statements_statements = new ArrayList<>();
    }

    public ccsl_invocation_Invocation(
        String argsKind        ArrayList<statements_Statement> statements_statements    ) {
        this.argsKind = argsKind;
        this.statements_statements = statements_statements;
    }

    public String getArgskind() {
        return argsKind;
    }

    public void setArgskind(String argsKind) {
        this.argsKind = argsKind;
    }

    public List<statements_Statement> getStatements_statements() {
        return statements_statements;
    }

    public void addStatements_statement(Statements_statement statements_statement) {
        this.statements_statements.add(statements_statement);
    }

}