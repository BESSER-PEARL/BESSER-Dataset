





import java.util.List;
import java.util.ArrayList;

public class ccsl_statements_Block extends Statement {

    private String statementsKind;





    private List<statements_Statement> statements_statements;


    public ccsl_statements_Block(
        String statementsKind    ) {
        super(
        );
        this.statementsKind = statementsKind;
        this.statements_statements = new ArrayList<>();
    }

    public ccsl_statements_Block(
        String statementsKind        ArrayList<statements_Statement> statements_statements    ) {
        this.statementsKind = statementsKind;
        this.statements_statements = statements_statements;
    }

    public String getStatementskind() {
        return statementsKind;
    }

    public void setStatementskind(String statementsKind) {
        this.statementsKind = statementsKind;
    }

    public List<statements_Statement> getStatements_statements() {
        return statements_statements;
    }

    public void addStatements_statement(Statements_statement statements_statement) {
        this.statements_statements.add(statements_statement);
    }

}