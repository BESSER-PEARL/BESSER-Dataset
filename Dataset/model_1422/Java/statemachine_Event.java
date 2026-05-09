





import java.util.List;
import java.util.ArrayList;

public class statemachine_Event  {

    private boolean value;





    private statemachine_Condition statemachine_condition;




    private statemachine_Signal statemachine_signal;


    public statemachine_Event(
        boolean value    ) {
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public statemachine_Condition getStatemachine_condition() {
        return statemachine_condition;
    }

    public void setStatemachine_condition(statemachine_Condition statemachine_condition) {
        this.statemachine_condition = statemachine_condition;
    }
    public statemachine_Signal getStatemachine_signal() {
        return statemachine_signal;
    }

    public void setStatemachine_signal(statemachine_Signal statemachine_signal) {
        this.statemachine_signal = statemachine_signal;
    }

}