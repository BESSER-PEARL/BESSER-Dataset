





import java.util.List;
import java.util.ArrayList;

public class pascal_simple_statement  {

    private String function_noargs;





    private pascal_function_designator pascal_function_designator;




    private pascal_goto_statement pascal_goto_statement;




    private pascal_statement pascal_statement;




    private pascal_assignment_statement pascal_assignment_statement;


    public pascal_simple_statement(
        String function_noargs    ) {
        this.function_noargs = function_noargs;
    }


    public String getFunction_noargs() {
        return function_noargs;
    }

    public void setFunction_noargs(String function_noargs) {
        this.function_noargs = function_noargs;
    }

    public pascal_function_designator getPascal_function_designator() {
        return pascal_function_designator;
    }

    public void setPascal_function_designator(pascal_function_designator pascal_function_designator) {
        this.pascal_function_designator = pascal_function_designator;
    }
    public pascal_goto_statement getPascal_goto_statement() {
        return pascal_goto_statement;
    }

    public void setPascal_goto_statement(pascal_goto_statement pascal_goto_statement) {
        this.pascal_goto_statement = pascal_goto_statement;
    }
    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }
    public pascal_assignment_statement getPascal_assignment_statement() {
        return pascal_assignment_statement;
    }

    public void setPascal_assignment_statement(pascal_assignment_statement pascal_assignment_statement) {
        this.pascal_assignment_statement = pascal_assignment_statement;
    }

}