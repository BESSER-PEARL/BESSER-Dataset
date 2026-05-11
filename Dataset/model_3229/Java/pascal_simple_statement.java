





import java.util.List;
import java.util.ArrayList;

public class pascal_simple_statement  {

    private String function_noargs;





    private pascal_statement pascal_statement;


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

    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }

}