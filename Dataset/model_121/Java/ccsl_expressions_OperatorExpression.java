





import java.util.List;
import java.util.ArrayList;

public class ccsl_expressions_OperatorExpression extends Statement {






    private List<statements_Statement> statements_statements;


    public ccsl_expressions_OperatorExpression(
    ) {
        super(
        );
        this.statements_statements = new ArrayList<>();
    }

    public ccsl_expressions_OperatorExpression(
        ArrayList<statements_Statement> statements_statements    ) {
        this.statements_statements = statements_statements;
    }


    public List<statements_Statement> getStatements_statements() {
        return statements_statements;
    }

    public void addStatements_statement(Statements_statement statements_statement) {
        this.statements_statements.add(statements_statement);
    }

}