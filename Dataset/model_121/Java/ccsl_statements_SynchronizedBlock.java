





import java.util.List;
import java.util.ArrayList;

public class ccsl_statements_SynchronizedBlock extends Statement {






    private statements_Statement statements_statement;




    private List<statements_Statement> statements_statements;


    public ccsl_statements_SynchronizedBlock(
    ) {
        super(
        );
        this.statements_statements = new ArrayList<>();
    }

    public ccsl_statements_SynchronizedBlock(
        ArrayList<statements_Statement> statements_statements    ) {
        this.statements_statements = statements_statements;
    }


    public statements_Statement getStatements_statement() {
        return statements_statement;
    }

    public void setStatements_statement(statements_Statement statements_statement) {
        this.statements_statement = statements_statement;
    }
    public List<statements_Statement> getStatements_statements() {
        return statements_statements;
    }

    public void addStatements_statement(Statements_statement statements_statement) {
        this.statements_statements.add(statements_statement);
    }

}