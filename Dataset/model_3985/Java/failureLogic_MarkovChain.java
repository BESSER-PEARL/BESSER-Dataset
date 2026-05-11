





import java.util.List;
import java.util.ArrayList;

public class failureLogic_MarkovChain extends FailureModel {






    private List<failureLogic_Transition> failurelogic_transitions;




    private List<failureLogic_State> failurelogic_states;


    public failureLogic_MarkovChain(
    ) {
        super(
        );
        this.failurelogic_transitions = new ArrayList<>();
        this.failurelogic_states = new ArrayList<>();
    }

    public failureLogic_MarkovChain(
        ArrayList<failureLogic_Transition> failurelogic_transitions,        ArrayList<failureLogic_State> failurelogic_states    ) {
        this.failurelogic_transitions = failurelogic_transitions;
        this.failurelogic_states = failurelogic_states;
    }


    public List<failureLogic_Transition> getFailurelogic_transitions() {
        return failurelogic_transitions;
    }

    public void addFailurelogic_transition(Failurelogic_transition failurelogic_transition) {
        this.failurelogic_transitions.add(failurelogic_transition);
    }
    public List<failureLogic_State> getFailurelogic_states() {
        return failurelogic_states;
    }

    public void addFailurelogic_state(Failurelogic_state failurelogic_state) {
        this.failurelogic_states.add(failurelogic_state);
    }

}