





import java.util.List;
import java.util.ArrayList;

public class pascal_expression  {

    private String operators;





    private pascal_if_statement pascal_if_statement;




    private pascal_case_statement pascal_case_statement;




    private pascal_for_statement pascal_for_statement;




    private pascal_repeat_statement pascal_repeat_statement;




    private pascal_assignment_statement pascal_assignment_statement;




    private pascal_while_statement pascal_while_statement;




    private pascal_for_statement pascal_for_statement;


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

    public pascal_if_statement getPascal_if_statement() {
        return pascal_if_statement;
    }

    public void setPascal_if_statement(pascal_if_statement pascal_if_statement) {
        this.pascal_if_statement = pascal_if_statement;
    }
    public pascal_case_statement getPascal_case_statement() {
        return pascal_case_statement;
    }

    public void setPascal_case_statement(pascal_case_statement pascal_case_statement) {
        this.pascal_case_statement = pascal_case_statement;
    }
    public pascal_for_statement getPascal_for_statement() {
        return pascal_for_statement;
    }

    public void setPascal_for_statement(pascal_for_statement pascal_for_statement) {
        this.pascal_for_statement = pascal_for_statement;
    }
    public pascal_repeat_statement getPascal_repeat_statement() {
        return pascal_repeat_statement;
    }

    public void setPascal_repeat_statement(pascal_repeat_statement pascal_repeat_statement) {
        this.pascal_repeat_statement = pascal_repeat_statement;
    }
    public pascal_assignment_statement getPascal_assignment_statement() {
        return pascal_assignment_statement;
    }

    public void setPascal_assignment_statement(pascal_assignment_statement pascal_assignment_statement) {
        this.pascal_assignment_statement = pascal_assignment_statement;
    }
    public pascal_while_statement getPascal_while_statement() {
        return pascal_while_statement;
    }

    public void setPascal_while_statement(pascal_while_statement pascal_while_statement) {
        this.pascal_while_statement = pascal_while_statement;
    }
    public pascal_for_statement getPascal_for_statement() {
        return pascal_for_statement;
    }

    public void setPascal_for_statement(pascal_for_statement pascal_for_statement) {
        this.pascal_for_statement = pascal_for_statement;
    }

}