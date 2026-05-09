





import java.util.List;
import java.util.ArrayList;

public class statemachine_mk2_Event  {

    private String description;





    private statemachine_mk2_Transition statemachine_mk2_transition;




    private List<statemachine_mk2_Transition> statemachine_mk2_transitions;




    private List<statemachine_mk2_State> statemachine_mk2_states;




    private statemachine_mk2_StateMachine statemachine_mk2_statemachine;


    public statemachine_mk2_Event(
        String description    ) {
        this.description = description;
        this.statemachine_mk2_transitions = new ArrayList<>();
        this.statemachine_mk2_states = new ArrayList<>();
    }

    public statemachine_mk2_Event(
        String description        ArrayList<statemachine_mk2_Transition> statemachine_mk2_transitions,        ArrayList<statemachine_mk2_State> statemachine_mk2_states    ) {
        this.description = description;
        this.statemachine_mk2_transitions = statemachine_mk2_transitions;
        this.statemachine_mk2_states = statemachine_mk2_states;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public statemachine_mk2_Transition getStatemachine_mk2_transition() {
        return statemachine_mk2_transition;
    }

    public void setStatemachine_mk2_transition(statemachine_mk2_Transition statemachine_mk2_transition) {
        this.statemachine_mk2_transition = statemachine_mk2_transition;
    }
    public List<statemachine_mk2_Transition> getStatemachine_mk2_transitions() {
        return statemachine_mk2_transitions;
    }

    public void addStatemachine_mk2_transition(Statemachine_mk2_transition statemachine_mk2_transition) {
        this.statemachine_mk2_transitions.add(statemachine_mk2_transition);
    }
    public List<statemachine_mk2_State> getStatemachine_mk2_states() {
        return statemachine_mk2_states;
    }

    public void addStatemachine_mk2_state(Statemachine_mk2_state statemachine_mk2_state) {
        this.statemachine_mk2_states.add(statemachine_mk2_state);
    }
    public statemachine_mk2_StateMachine getStatemachine_mk2_statemachine() {
        return statemachine_mk2_statemachine;
    }

    public void setStatemachine_mk2_statemachine(statemachine_mk2_StateMachine statemachine_mk2_statemachine) {
        this.statemachine_mk2_statemachine = statemachine_mk2_statemachine;
    }

}