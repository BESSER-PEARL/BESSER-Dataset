





import java.util.List;
import java.util.ArrayList;

public class statemachine_Command  {

    private boolean newValue;





    private statemachine_State statemachine_state;




    private statemachine_Signal statemachine_signal;


    public statemachine_Command(
        boolean newValue    ) {
        this.newValue = newValue;
    }


    public boolean getNewvalue() {
        return newValue;
    }

    public void setNewvalue(boolean newValue) {
        this.newValue = newValue;
    }

    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public statemachine_Signal getStatemachine_signal() {
        return statemachine_signal;
    }

    public void setStatemachine_signal(statemachine_Signal statemachine_signal) {
        this.statemachine_signal = statemachine_signal;
    }

}