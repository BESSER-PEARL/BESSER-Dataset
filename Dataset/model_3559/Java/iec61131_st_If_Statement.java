





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_If_Statement extends Selection_Statement {






    private List<Else_If_Statement> else_if_statements;




    private Expression_Types expression_types;




    private Else_Statement else_statement;


    public iec61131_st_If_Statement(
    ) {
        super(
        );
        this.else_if_statements = new ArrayList<>();
    }

    public iec61131_st_If_Statement(
        ArrayList<Else_If_Statement> else_if_statements    ) {
        this.else_if_statements = else_if_statements;
    }


    public List<Else_If_Statement> getElse_if_statements() {
        return else_if_statements;
    }

    public void addElse_if_statement(Else_if_statement else_if_statement) {
        this.else_if_statements.add(else_if_statement);
    }
    public Expression_Types getExpression_types() {
        return expression_types;
    }

    public void setExpression_types(Expression_Types expression_types) {
        this.expression_types = expression_types;
    }
    public Else_Statement getElse_statement() {
        return else_statement;
    }

    public void setElse_statement(Else_Statement else_statement) {
        this.else_statement = else_statement;
    }

}