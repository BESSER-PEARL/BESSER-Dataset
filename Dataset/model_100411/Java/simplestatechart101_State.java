





import java.util.List;
import java.util.ArrayList;

public class simplestatechart101_State extends NamedElement {

    private String label;
    private String type;
    private String activity;





    private simplestatechart101_Transition simplestatechart101_transition;




    private List<simplestatechart101_State> simplestatechart101_states;




    private simplestatechart101_State simplestatechart101_state;




    private simplestatechart101_Transition simplestatechart101_transition;




    private List<simplestatechart101_Transition> simplestatechart101_transitions;


    public simplestatechart101_State(
        String label,        String type,        String activity    ) {
        super(
        );
        this.label = label;
        this.type = type;
        this.activity = activity;
        this.simplestatechart101_states = new ArrayList<>();
        this.simplestatechart101_transitions = new ArrayList<>();
    }

    public simplestatechart101_State(
        String label,        String type,        String activity        ArrayList<simplestatechart101_State> simplestatechart101_states,        ArrayList<simplestatechart101_Transition> simplestatechart101_transitions    ) {
        this.label = label;
        this.type = type;
        this.activity = activity;
        this.simplestatechart101_states = simplestatechart101_states;
        this.simplestatechart101_transitions = simplestatechart101_transitions;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }

    public simplestatechart101_Transition getSimplestatechart101_transition() {
        return simplestatechart101_transition;
    }

    public void setSimplestatechart101_transition(simplestatechart101_Transition simplestatechart101_transition) {
        this.simplestatechart101_transition = simplestatechart101_transition;
    }
    public List<simplestatechart101_State> getSimplestatechart101_states() {
        return simplestatechart101_states;
    }

    public void addSimplestatechart101_state(Simplestatechart101_state simplestatechart101_state) {
        this.simplestatechart101_states.add(simplestatechart101_state);
    }
    public simplestatechart101_State getSimplestatechart101_state() {
        return simplestatechart101_state;
    }

    public void setSimplestatechart101_state(simplestatechart101_State simplestatechart101_state) {
        this.simplestatechart101_state = simplestatechart101_state;
    }
    public simplestatechart101_Transition getSimplestatechart101_transition() {
        return simplestatechart101_transition;
    }

    public void setSimplestatechart101_transition(simplestatechart101_Transition simplestatechart101_transition) {
        this.simplestatechart101_transition = simplestatechart101_transition;
    }
    public List<simplestatechart101_Transition> getSimplestatechart101_transitions() {
        return simplestatechart101_transitions;
    }

    public void addSimplestatechart101_transition(Simplestatechart101_transition simplestatechart101_transition) {
        this.simplestatechart101_transitions.add(simplestatechart101_transition);
    }

}