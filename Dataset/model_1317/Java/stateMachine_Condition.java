





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Condition  {

    private String op;
    private int value;





    private stateMachine_Variable statemachine_variable;


    public stateMachine_Condition(
        String op,        int value    ) {
        this.op = op;
        this.value = value;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public stateMachine_Variable getStatemachine_variable() {
        return statemachine_variable;
    }

    public void setStatemachine_variable(stateMachine_Variable statemachine_variable) {
        this.statemachine_variable = statemachine_variable;
    }

}