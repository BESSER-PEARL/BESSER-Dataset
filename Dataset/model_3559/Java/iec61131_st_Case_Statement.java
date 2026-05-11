





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_Case_Statement extends Selection_Statement {






    private Else_Statement else_statement;




    private Expression_Types expression_types;


    public iec61131_st_Case_Statement(
    ) {
        super(
        );
    }



    public Else_Statement getElse_statement() {
        return else_statement;
    }

    public void setElse_statement(Else_Statement else_statement) {
        this.else_statement = else_statement;
    }
    public Expression_Types getExpression_types() {
        return expression_types;
    }

    public void setExpression_types(Expression_Types expression_types) {
        this.expression_types = expression_types;
    }

}