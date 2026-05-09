





import java.util.List;
import java.util.ArrayList;

public class ccsl_assignment_Assignment extends AbstractAssignment {

    private String operator;





    private statements_Statement statements_statement;


    public ccsl_assignment_Assignment(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public statements_Statement getStatements_statement() {
        return statements_statement;
    }

    public void setStatements_statement(statements_Statement statements_statement) {
        this.statements_statement = statements_statement;
    }

}