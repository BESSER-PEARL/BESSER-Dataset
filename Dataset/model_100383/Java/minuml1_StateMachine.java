





import java.util.List;
import java.util.ArrayList;

public class minuml1_StateMachine extends ModelElement {






    private List<minuml1_Transition> minuml1_transitions;


    public minuml1_StateMachine(
    ) {
        super(
        );
        this.minuml1_transitions = new ArrayList<>();
    }

    public minuml1_StateMachine(
        ArrayList<minuml1_Transition> minuml1_transitions    ) {
        this.minuml1_transitions = minuml1_transitions;
    }


    public List<minuml1_Transition> getMinuml1_transitions() {
        return minuml1_transitions;
    }

    public void addMinuml1_transition(Minuml1_transition minuml1_transition) {
        this.minuml1_transitions.add(minuml1_transition);
    }

}