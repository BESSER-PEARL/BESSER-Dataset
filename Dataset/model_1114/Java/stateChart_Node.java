





import java.util.List;
import java.util.ArrayList;

public class stateChart_Node  {

    private String metadata;
    private String actions;
    private String activity;
    private String type;
    private String label;
    private String name;





    private stateChart_Transition statechart_transition;




    private stateChart_Model statechart_model;




    private stateChart_Node statechart_node;




    private List<stateChart_Variable> statechart_variables;




    private stateChart_Transition statechart_transition;




    private List<stateChart_Transition> statechart_transitions;




    private stateChart_Transition statechart_transition;




    private List<stateChart_Node> statechart_nodes;


    public stateChart_Node(
        String metadata,        String actions,        String activity,        String type,        String label,        String name    ) {
        this.metadata = metadata;
        this.actions = actions;
        this.activity = activity;
        this.type = type;
        this.label = label;
        this.name = name;
        this.statechart_variables = new ArrayList<>();
        this.statechart_transitions = new ArrayList<>();
        this.statechart_nodes = new ArrayList<>();
    }

    public stateChart_Node(
        String metadata,        String actions,        String activity,        String type,        String label,        String name        ArrayList<stateChart_Variable> statechart_variables,        ArrayList<stateChart_Transition> statechart_transitions,        ArrayList<stateChart_Node> statechart_nodes    ) {
        this.metadata = metadata;
        this.actions = actions;
        this.activity = activity;
        this.type = type;
        this.label = label;
        this.name = name;
        this.statechart_variables = statechart_variables;
        this.statechart_transitions = statechart_transitions;
        this.statechart_nodes = statechart_nodes;
    }

    public String getMetadata() {
        return metadata;
    }

    public void setMetadata(String metadata) {
        this.metadata = metadata;
    }
    public String getActions() {
        return actions;
    }

    public void setActions(String actions) {
        this.actions = actions;
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
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public stateChart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(stateChart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public stateChart_Model getStatechart_model() {
        return statechart_model;
    }

    public void setStatechart_model(stateChart_Model statechart_model) {
        this.statechart_model = statechart_model;
    }
    public stateChart_Node getStatechart_node() {
        return statechart_node;
    }

    public void setStatechart_node(stateChart_Node statechart_node) {
        this.statechart_node = statechart_node;
    }
    public List<stateChart_Variable> getStatechart_variables() {
        return statechart_variables;
    }

    public void addStatechart_variable(Statechart_variable statechart_variable) {
        this.statechart_variables.add(statechart_variable);
    }
    public stateChart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(stateChart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public List<stateChart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }
    public stateChart_Transition getStatechart_transition() {
        return statechart_transition;
    }

    public void setStatechart_transition(stateChart_Transition statechart_transition) {
        this.statechart_transition = statechart_transition;
    }
    public List<stateChart_Node> getStatechart_nodes() {
        return statechart_nodes;
    }

    public void addStatechart_node(Statechart_node statechart_node) {
        this.statechart_nodes.add(statechart_node);
    }

}