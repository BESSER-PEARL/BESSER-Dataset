





import java.util.List;
import java.util.ArrayList;

public class sm1_StateMachine  {






    private List<sm1_Transition> sm1_transitions;


    public sm1_StateMachine(
    ) {
        this.sm1_transitions = new ArrayList<>();
    }

    public sm1_StateMachine(
        ArrayList<sm1_Transition> sm1_transitions    ) {
        this.sm1_transitions = sm1_transitions;
    }


    public List<sm1_Transition> getSm1_transitions() {
        return sm1_transitions;
    }

    public void addSm1_transition(Sm1_transition sm1_transition) {
        this.sm1_transitions.add(sm1_transition);
    }

}