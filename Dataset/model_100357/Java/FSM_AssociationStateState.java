





import java.util.List;
import java.util.ArrayList;

public class FSM_AssociationStateState  {






    private List<State> states;




    private Transition transition;




    private List<State> states;


    public FSM_AssociationStateState(
    ) {
        this.states = new ArrayList<>();
        this.states = new ArrayList<>();
    }

    public FSM_AssociationStateState(
        ArrayList<State> states,        ArrayList<State> states    ) {
        this.states = states;
        this.states = states;
    }


    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }
    public Transition getTransition() {
        return transition;
    }

    public void setTransition(Transition transition) {
        this.transition = transition;
    }
    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }

}