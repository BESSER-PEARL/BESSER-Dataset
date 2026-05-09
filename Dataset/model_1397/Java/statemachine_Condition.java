





import java.util.List;
import java.util.ArrayList;

public class statemachine_Condition  {






    private statemachine_Transition statemachine_transition;




    private List<statemachine_Event> statemachine_events;


    public statemachine_Condition(
    ) {
        this.statemachine_events = new ArrayList<>();
    }

    public statemachine_Condition(
        ArrayList<statemachine_Event> statemachine_events    ) {
        this.statemachine_events = statemachine_events;
    }


    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public List<statemachine_Event> getStatemachine_events() {
        return statemachine_events;
    }

    public void addStatemachine_event(Statemachine_event statemachine_event) {
        this.statemachine_events.add(statemachine_event);
    }

}