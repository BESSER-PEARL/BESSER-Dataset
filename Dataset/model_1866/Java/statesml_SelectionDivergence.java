





import java.util.List;
import java.util.ArrayList;

public class statesml_SelectionDivergence extends Node {






    private List<statesml_Transition> statesml_transitions;


    public statesml_SelectionDivergence(
    ) {
        super(
        );
        this.statesml_transitions = new ArrayList<>();
    }

    public statesml_SelectionDivergence(
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