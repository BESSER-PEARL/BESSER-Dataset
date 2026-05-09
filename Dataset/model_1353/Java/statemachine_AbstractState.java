





import java.util.List;
import java.util.ArrayList;

public class statemachine_AbstractState extends ObeoDSMObject {






    private List<statemachine_Transition> statemachine_transitions;




    private List<statemachine_Transition> statemachine_transitions;




    private statemachine_Transition statemachine_transition;




    private statemachine_Transition statemachine_transition;


    public statemachine_AbstractState(
    ) {
        super(
        );
        this.statemachine_transitions = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_AbstractState(
        ArrayList<statemachine_Transition> statemachine_transitions,        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.statemachine_transitions = statemachine_transitions;
        this.statemachine_transitions = statemachine_transitions;
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

}