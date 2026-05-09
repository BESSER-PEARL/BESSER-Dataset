





import java.util.List;
import java.util.ArrayList;

public class dsl_Expression extends IfStatement {

    private String assignOp;





    private dsl_VariableInitializer dsl_variableinitializer;




    private dsl_Expression dsl_expression;


    public dsl_Expression(
        String assignOp    ) {
        super(
        );
        this.assignOp = assignOp;
    }


    public String getAssignop() {
        return assignOp;
    }

    public void setAssignop(String assignOp) {
        this.assignOp = assignOp;
    }

    public dsl_VariableInitializer getDsl_variableinitializer() {
        return dsl_variableinitializer;
    }

    public void setDsl_variableinitializer(dsl_VariableInitializer dsl_variableinitializer) {
        this.dsl_variableinitializer = dsl_variableinitializer;
    }
    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }

}