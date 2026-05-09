





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Condition  {






    private List<stateMachine_Event> statemachine_events;


    public stateMachine_Condition(
    ) {
        this.statemachine_events = new ArrayList<>();
    }

    public stateMachine_Condition(
        ArrayList<stateMachine_Event> statemachine_events    ) {
        this.statemachine_events = statemachine_events;
    }


    public List<stateMachine_Event> getStatemachine_events() {
        return statemachine_events;
    }

    public void addStatemachine_event(Statemachine_event statemachine_event) {
        this.statemachine_events.add(statemachine_event);
    }

}