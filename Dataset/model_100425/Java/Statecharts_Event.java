





import java.util.List;
import java.util.ArrayList;

public class Statecharts_Event  {






    private List<Transition> transitions;




    private List<State> states;


    public Statecharts_Event(
    ) {
        this.transitions = new ArrayList<>();
        this.states = new ArrayList<>();
    }

    public Statecharts_Event(
        ArrayList<Transition> transitions,        ArrayList<State> states    ) {
        this.transitions = transitions;
        this.states = states;
    }


    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }
    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }

}