





import java.util.List;
import java.util.ArrayList;

public class statemachines_Vertex extends NamedElement {






    private List<statemachines_Transition> statemachines_transitions;




    private List<statemachines_Transition> statemachines_transitions;




    private statemachines_Transition statemachines_transition;




    private statemachines_Transition statemachines_transition;


    public statemachines_Vertex(
    ) {
        super(
        );
        this.statemachines_transitions = new ArrayList<>();
        this.statemachines_transitions = new ArrayList<>();
    }

    public statemachines_Vertex(
        ArrayList<statemachines_Transition> statemachines_transitions,        ArrayList<statemachines_Transition> statemachines_transitions    ) {
        this.statemachines_transitions = statemachines_transitions;
        this.statemachines_transitions = statemachines_transitions;
    }


    public List<statemachines_Transition> getStatemachines_transitions() {
        return statemachines_transitions;
    }

    public void addStatemachines_transition(Statemachines_transition statemachines_transition) {
        this.statemachines_transitions.add(statemachines_transition);
    }
    public List<statemachines_Transition> getStatemachines_transitions() {
        return statemachines_transitions;
    }

    public void addStatemachines_transition(Statemachines_transition statemachines_transition) {
        this.statemachines_transitions.add(statemachines_transition);
    }
    public statemachines_Transition getStatemachines_transition() {
        return statemachines_transition;
    }

    public void setStatemachines_transition(statemachines_Transition statemachines_transition) {
        this.statemachines_transition = statemachines_transition;
    }
    public statemachines_Transition getStatemachines_transition() {
        return statemachines_transition;
    }

    public void setStatemachines_transition(statemachines_Transition statemachines_transition) {
        this.statemachines_transition = statemachines_transition;
    }

}