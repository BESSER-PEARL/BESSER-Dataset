





import java.util.List;
import java.util.ArrayList;

public class statemachine_StateMachine  {

    private String name;





    private List<statemachine_State> statemachine_states;




    private List<statemachine_Resource> statemachine_resources;




    private List<statemachine_Transition> statemachine_transitions;


    public statemachine_StateMachine(
        String name    ) {
        this.name = name;
        this.statemachine_states = new ArrayList<>();
        this.statemachine_resources = new ArrayList<>();
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_StateMachine(
        String name        ArrayList<statemachine_State> statemachine_states,        ArrayList<statemachine_Resource> statemachine_resources,        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.name = name;
        this.statemachine_states = statemachine_states;
        this.statemachine_resources = statemachine_resources;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statemachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }
    public List<statemachine_Resource> getStatemachine_resources() {
        return statemachine_resources;
    }

    public void addStatemachine_resource(Statemachine_resource statemachine_resource) {
        this.statemachine_resources.add(statemachine_resource);
    }
    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}