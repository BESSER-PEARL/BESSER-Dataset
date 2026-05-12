





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_ExecuteImmediateStatement extends BindingStatement {

    private String variable;



    public syntax_dbl_ExecuteImmediateStatement(
        String variable    ) {
        super(
        );
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }


}