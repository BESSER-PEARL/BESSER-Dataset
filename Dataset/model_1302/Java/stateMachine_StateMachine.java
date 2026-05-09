





import java.util.List;
import java.util.ArrayList;

public class stateMachine_StateMachine extends IDElement {






    private List<stateMachine_Transition> statemachine_transitions;




    private List<stateMachine_Event> statemachine_events;


    public stateMachine_StateMachine(
    ) {
        super(
        );
        this.statemachine_transitions = new ArrayList<>();
        this.statemachine_events = new ArrayList<>();
    }

    public stateMachine_StateMachine(
        ArrayList<stateMachine_Transition> statemachine_transitions,        ArrayList<stateMachine_Event> statemachine_events    ) {
        this.statemachine_transitions = statemachine_transitions;
        this.statemachine_events = statemachine_events;
    }


    public List<stateMachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public List<stateMachine_Event> getStatemachine_events() {
        return statemachine_events;
    }

    public void addStatemachine_event(Statemachine_event statemachine_event) {
        this.statemachine_events.add(statemachine_event);
    }

}