





import java.util.List;
import java.util.ArrayList;

public class simplestatechart_State extends NamedElement {

    private String label;
    private String activity;
    private String type;





    private List<simplestatechart_Transition> simplestatechart_transitions;




    private List<simplestatechart_State> simplestatechart_states;




    private simplestatechart_Transition simplestatechart_transition;




    private simplestatechart_Transition simplestatechart_transition;




    private simplestatechart_State simplestatechart_state;


    public simplestatechart_State(
        String label,        String activity,        String type    ) {
        super(
        );
        this.label = label;
        this.activity = activity;
        this.type = type;
        this.simplestatechart_transitions = new ArrayList<>();
        this.simplestatechart_states = new ArrayList<>();
    }

    public simplestatechart_State(
        String label,        String activity,        String type        ArrayList<simplestatechart_Transition> simplestatechart_transitions,        ArrayList<simplestatechart_State> simplestatechart_states    ) {
        this.label = label;
        this.activity = activity;
        this.type = type;
        this.simplestatechart_transitions = simplestatechart_transitions;
        this.simplestatechart_states = simplestatechart_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<simplestatechart_Transition> getSimplestatechart_transitions() {
        return simplestatechart_transitions;
    }

    public void addSimplestatechart_transition(Simplestatechart_transition simplestatechart_transition) {
        this.simplestatechart_transitions.add(simplestatechart_transition);
    }
    public List<simplestatechart_State> getSimplestatechart_states() {
        return simplestatechart_states;
    }

    public void addSimplestatechart_state(Simplestatechart_state simplestatechart_state) {
        this.simplestatechart_states.add(simplestatechart_state);
    }
    public simplestatechart_Transition getSimplestatechart_transition() {
        return simplestatechart_transition;
    }

    public void setSimplestatechart_transition(simplestatechart_Transition simplestatechart_transition) {
        this.simplestatechart_transition = simplestatechart_transition;
    }
    public simplestatechart_Transition getSimplestatechart_transition() {
        return simplestatechart_transition;
    }

    public void setSimplestatechart_transition(simplestatechart_Transition simplestatechart_transition) {
        this.simplestatechart_transition = simplestatechart_transition;
    }
    public simplestatechart_State getSimplestatechart_state() {
        return simplestatechart_state;
    }

    public void setSimplestatechart_state(simplestatechart_State simplestatechart_state) {
        this.simplestatechart_state = simplestatechart_state;
    }

}