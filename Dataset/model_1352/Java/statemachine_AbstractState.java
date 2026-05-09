





import java.util.List;
import java.util.ArrayList;

public class statemachine_AbstractState  {

    private String name;





    private List<statemachine_Transition> statemachine_transitions;




    private List<statemachine_Transition> statemachine_transitions;




    private statemachine_Transition statemachine_transition;




    private statemachine_Transition statemachine_transition;




    private statemachine_StateMachine statemachine_statemachine;


    public statemachine_AbstractState(
        String name    ) {
        this.name = name;
        this.statemachine_transitions = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_AbstractState(
        String name        ArrayList<statemachine_Transition> statemachine_transitions,        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.name = name;
        this.statemachine_transitions = statemachine_transitions;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public statemachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}