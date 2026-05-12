





import java.util.List;
import java.util.ArrayList;

public class minuml1_StateVertex extends ModelElement {






    private List<minuml1_Transition> minuml1_transitions;




    private List<minuml1_Transition> minuml1_transitions;




    private minuml1_Transition minuml1_transition;




    private minuml1_Transition minuml1_transition;


    public minuml1_StateVertex(
    ) {
        super(
        );
        this.minuml1_transitions = new ArrayList<>();
        this.minuml1_transitions = new ArrayList<>();
    }

    public minuml1_StateVertex(
        ArrayList<minuml1_Transition> minuml1_transitions,        ArrayList<minuml1_Transition> minuml1_transitions    ) {
        this.minuml1_transitions = minuml1_transitions;
        this.minuml1_transitions = minuml1_transitions;
    }


    public List<minuml1_Transition> getMinuml1_transitions() {
        return minuml1_transitions;
    }

    public void addMinuml1_transition(Minuml1_transition minuml1_transition) {
        this.minuml1_transitions.add(minuml1_transition);
    }
    public List<minuml1_Transition> getMinuml1_transitions() {
        return minuml1_transitions;
    }

    public void addMinuml1_transition(Minuml1_transition minuml1_transition) {
        this.minuml1_transitions.add(minuml1_transition);
    }
    public minuml1_Transition getMinuml1_transition() {
        return minuml1_transition;
    }

    public void setMinuml1_transition(minuml1_Transition minuml1_transition) {
        this.minuml1_transition = minuml1_transition;
    }
    public minuml1_Transition getMinuml1_transition() {
        return minuml1_transition;
    }

    public void setMinuml1_transition(minuml1_Transition minuml1_transition) {
        this.minuml1_transition = minuml1_transition;
    }

}