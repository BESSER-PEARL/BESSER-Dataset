





import java.util.List;
import java.util.ArrayList;

public class statemachine_StateMachineDescription extends NamedElement {






    private List<statemachine_AbstractState> statemachine_abstractstates;




    private List<statemachine_Transition> statemachine_transitions;


    public statemachine_StateMachineDescription(
    ) {
        super(
        );
        this.statemachine_abstractstates = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_StateMachineDescription(
        ArrayList<statemachine_AbstractState> statemachine_abstractstates,        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.statemachine_abstractstates = statemachine_abstractstates;
        this.statemachine_transitions = statemachine_transitions;
    }


    public List<statemachine_AbstractState> getStatemachine_abstractstates() {
        return statemachine_abstractstates;
    }

    public void addStatemachine_abstractstate(Statemachine_abstractstate statemachine_abstractstate) {
        this.statemachine_abstractstates.add(statemachine_abstractstate);
    }
    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}