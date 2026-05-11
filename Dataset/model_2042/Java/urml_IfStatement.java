





import java.util.List;
import java.util.ArrayList;

public class urml_IfStatement extends Statement {






    private List<urml_Statement> urml_statements;




    private urml_Expression urml_expression;




    private List<urml_Statement> urml_statements;


    public urml_IfStatement(
    ) {
        super(
        );
        this.urml_statements = new ArrayList<>();
        this.urml_statements = new ArrayList<>();
    }

    public urml_IfStatement(
        ArrayList<urml_Statement> urml_statements,        ArrayList<urml_Statement> urml_statements    ) {
        this.urml_statements = urml_statements;
        this.urml_statements = urml_statements;
    }


    public List<urml_Statement> getUrml_statements() {
        return urml_statements;
    }

    public void addUrml_statement(Urml_statement urml_statement) {
        this.urml_statements.add(urml_statement);
    }
    public urml_Expression getUrml_expression() {
        return urml_expression;
    }

    public void setUrml_expression(urml_Expression urml_expression) {
        this.urml_expression = urml_expression;
    }
    public List<urml_Statement> getUrml_statements() {
        return urml_statements;
    }

    public void addUrml_statement(Urml_statement urml_statement) {
        this.urml_statements.add(urml_statement);
    }

}