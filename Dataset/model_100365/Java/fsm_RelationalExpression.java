





import java.util.List;
import java.util.ArrayList;

public class fsm_RelationalExpression extends Expression {

    private String operator;





    private fsm_Expression fsm_expression;




    private fsm_Expression fsm_expression;


    public fsm_RelationalExpression(
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

    public fsm_Expression getFsm_expression() {
        return fsm_expression;
    }

    public void setFsm_expression(fsm_Expression fsm_expression) {
        this.fsm_expression = fsm_expression;
    }
    public fsm_Expression getFsm_expression() {
        return fsm_expression;
    }

    public void setFsm_expression(fsm_Expression fsm_expression) {
        this.fsm_expression = fsm_expression;
    }

}