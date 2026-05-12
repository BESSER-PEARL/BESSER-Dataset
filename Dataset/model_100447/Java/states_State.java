





import java.util.List;
import java.util.ArrayList;

public class states_State  {

    private String name;
    private boolean initial;





    private states_Transition states_transition;




    private List<states_Transition> states_transitions;




    private states_Statemachine states_statemachine;


    public states_State(
        String name,        boolean initial    ) {
        this.name = name;
        this.initial = initial;
        this.states_transitions = new ArrayList<>();
    }

    public states_State(
        String name,        boolean initial        ArrayList<states_Transition> states_transitions    ) {
        this.name = name;
        this.initial = initial;
        this.states_transitions = states_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public states_Transition getStates_transition() {
        return states_transition;
    }

    public void setStates_transition(states_Transition states_transition) {
        this.states_transition = states_transition;
    }
    public List<states_Transition> getStates_transitions() {
        return states_transitions;
    }

    public void addStates_transition(States_transition states_transition) {
        this.states_transitions.add(states_transition);
    }
    public states_Statemachine getStates_statemachine() {
        return states_statemachine;
    }

    public void setStates_statemachine(states_Statemachine states_statemachine) {
        this.states_statemachine = states_statemachine;
    }

}