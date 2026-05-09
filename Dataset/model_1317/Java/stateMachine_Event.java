





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Event  {

    private String name;





    private stateMachine_Events statemachine_events;


    public stateMachine_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateMachine_Events getStatemachine_events() {
        return statemachine_events;
    }

    public void setStatemachine_events(stateMachine_Events statemachine_events) {
        this.statemachine_events = statemachine_events;
    }

}