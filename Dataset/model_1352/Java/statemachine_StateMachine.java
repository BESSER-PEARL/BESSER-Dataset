





import java.util.List;
import java.util.ArrayList;

public class statemachine_StateMachine  {






    private List<statemachine_Transition> statemachine_transitions;


    public statemachine_StateMachine(
    ) {
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_StateMachine(
        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.statemachine_transitions = statemachine_transitions;
    }


    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}