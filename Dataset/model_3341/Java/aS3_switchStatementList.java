





import java.util.List;
import java.util.ArrayList;

public class aS3_switchStatementList  {






    private aS3_Expression as3_expression;




    private List<aS3_Statement> as3_statements;


    public aS3_switchStatementList(
    ) {
        this.as3_statements = new ArrayList<>();
    }

    public aS3_switchStatementList(
        ArrayList<aS3_Statement> as3_statements    ) {
        this.as3_statements = as3_statements;
    }


    public aS3_Expression getAs3_expression() {
        return as3_expression;
    }

    public void setAs3_expression(aS3_Expression as3_expression) {
        this.as3_expression = as3_expression;
    }
    public List<aS3_Statement> getAs3_statements() {
        return as3_statements;
    }

    public void addAs3_statement(As3_statement as3_statement) {
        this.as3_statements.add(as3_statement);
    }

}