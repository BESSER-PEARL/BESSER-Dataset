





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private String name;





    private statemachine_Transition statemachine_transition;




    private statemachine_State statemachine_state;




    private statemachine_Statemachine statemachine_statemachine;




    private List<statemachine_Transition> statemachine_transitions;


    public statemachine_State(
        String name    ) {
        this.name = name;
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_State(
        String name        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.name = name;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}