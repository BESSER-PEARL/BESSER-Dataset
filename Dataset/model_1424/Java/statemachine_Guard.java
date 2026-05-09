





import java.util.List;
import java.util.ArrayList;

public class statemachine_Guard  {






    private statemachine_Command statemachine_command;




    private statemachine_Event statemachine_event;


    public statemachine_Guard(
    ) {
    }



    public statemachine_Command getStatemachine_command() {
        return statemachine_command;
    }

    public void setStatemachine_command(statemachine_Command statemachine_command) {
        this.statemachine_command = statemachine_command;
    }
    public statemachine_Event getStatemachine_event() {
        return statemachine_event;
    }

    public void setStatemachine_event(statemachine_Event statemachine_event) {
        this.statemachine_event = statemachine_event;
    }

}