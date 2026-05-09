





import java.util.List;
import java.util.ArrayList;

public class statemachine_Signal  {

    private String name;





    private statemachine_Statemachine statemachine_statemachine;




    private statemachine_Event statemachine_event;


    public statemachine_Signal(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public statemachine_Event getStatemachine_event() {
        return statemachine_event;
    }

    public void setStatemachine_event(statemachine_Event statemachine_event) {
        this.statemachine_event = statemachine_event;
    }

}