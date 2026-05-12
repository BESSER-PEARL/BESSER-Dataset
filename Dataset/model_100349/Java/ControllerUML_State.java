





import java.util.List;
import java.util.ArrayList;

public class ControllerUML_State  {






    private List<State> states;




    private List<StateTransition> statetransitions;




    private List<StateTransition> statetransitions;




    private State state;


    public ControllerUML_State(
    ) {
        this.states = new ArrayList<>();
        this.statetransitions = new ArrayList<>();
        this.statetransitions = new ArrayList<>();
    }

    public ControllerUML_State(
        ArrayList<State> states,        ArrayList<StateTransition> statetransitions,        ArrayList<StateTransition> statetransitions    ) {
        this.states = states;
        this.statetransitions = statetransitions;
        this.statetransitions = statetransitions;
    }


    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }
    public List<StateTransition> getStatetransitions() {
        return statetransitions;
    }

    public void addStatetransition(Statetransition statetransition) {
        this.statetransitions.add(statetransition);
    }
    public List<StateTransition> getStatetransitions() {
        return statetransitions;
    }

    public void addStatetransition(Statetransition statetransition) {
        this.statetransitions.add(statetransition);
    }
    public State getState() {
        return state;
    }

    public void setState(State state) {
        this.state = state;
    }

}