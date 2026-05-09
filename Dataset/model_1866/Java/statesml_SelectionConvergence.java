





import java.util.List;
import java.util.ArrayList;

public class statesml_SelectionConvergence extends Node {






    private List<statesml_Transition> statesml_transitions;


    public statesml_SelectionConvergence(
    ) {
        super(
        );
        this.statesml_transitions = new ArrayList<>();
    }

    public statesml_SelectionConvergence(
        ArrayList<statesml_Transition> statesml_transitions    ) {
        this.statesml_transitions = statesml_transitions;
    }


    public List<statesml_Transition> getStatesml_transitions() {
        return statesml_transitions;
    }

    public void addStatesml_transition(Statesml_transition statesml_transition) {
        this.statesml_transitions.add(statesml_transition);
    }

}