





import java.util.List;
import java.util.ArrayList;

public class statechart_State extends StateVertex {






    private statechart_StateMachine statechart_statemachine;




    private statechart_StateMachine statechart_statemachine;




    private List<statechart_Transition> statechart_transitions;




    private statechart_Transition statechart_transition;




    private List<statechart_Event> statechart_events;




    private statechart_StateMachine statechart_statemachine;


    public statechart_State(
    ) {
        super(
        );
        this.statechart_transitions = new ArrayList<>();
        this.statechart_events = new ArrayList<>();
    }

    public statechart_State(
        ArrayList<statechart_Transition> statechart_transitions,        ArrayList<statechart_Event> statechart_events    ) {
        this.statechart_transitions = statechart_transitions;
        this.statechart_events = statechart_events;
    }


    public statechart_StateMachine getStatechart_statemachine() {
        return statechart_statemachine;
    }

    public void setStatechart_statemachine(statechart_StateMachine statechart_statemachine) {
        this.statechart_statemachine = statechart_statemachine;
    }
    public statechart_StateMachine getStatechart_statemachine() {
        return statechart_statemachine;
    }

    public void setStatechart_statemachine(statechart_StateMachine statechart_statemachine) {
        this.statechart_statemachine = statechart_statemachine;
    }
    public List<statechart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }
    public statechart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(statechart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public List<statechart_Event> getStatechart_events() {
        return statechart_events;
    }

    public void addStatechart_event(Statechart_event statechart_event) {
        this.statechart_events.add(statechart_event);
    }
    public statechart_StateMachine getStatechart_statemachine() {
        return statechart_statemachine;
    }

    public void setStatechart_statemachine(statechart_StateMachine statechart_statemachine) {
        this.statechart_statemachine = statechart_statemachine;
    }

}