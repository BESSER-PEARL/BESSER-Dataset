





import java.util.List;
import java.util.ArrayList;

public class sm6_StateMachine  {






    private List<sm6_Transition> sm6_transitions;


    public sm6_StateMachine(
    ) {
        this.sm6_transitions = new ArrayList<>();
    }

    public sm6_StateMachine(
        ArrayList<sm6_Transition> sm6_transitions    ) {
        this.sm6_transitions = sm6_transitions;
    }


    public List<sm6_Transition> getSm6_transitions() {
        return sm6_transitions;
    }

    public void addSm6_transition(Sm6_transition sm6_transition) {
        this.sm6_transitions.add(sm6_transition);
    }

}