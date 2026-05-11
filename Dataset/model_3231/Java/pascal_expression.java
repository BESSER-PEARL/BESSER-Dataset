





import java.util.List;
import java.util.ArrayList;

public class pascal_expression  {

    private String operators;





    private pascal_assignment_statement pascal_assignment_statement;


    public pascal_expression(
        String operators    ) {
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public pascal_assignment_statement getPascal_assignment_statement() {
        return pascal_assignment_statement;
    }

    public void setPascal_assignment_statement(pascal_assignment_statement pascal_assignment_statement) {
        this.pascal_assignment_statement = pascal_assignment_statement;
    }

}