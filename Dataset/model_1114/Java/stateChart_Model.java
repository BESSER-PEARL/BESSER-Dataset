





import java.util.List;
import java.util.ArrayList;

public class stateChart_Model  {

    private String name;
    private String description;
    private String metadata;





    private List<stateChart_Variable> statechart_variables;




    private List<stateChart_Transition> statechart_transitions;


    public stateChart_Model(
        String name,        String description,        String metadata    ) {
        this.name = name;
        this.description = description;
        this.metadata = metadata;
        this.statechart_variables = new ArrayList<>();
        this.statechart_transitions = new ArrayList<>();
    }

    public stateChart_Model(
        String name,        String description,        String metadata        ArrayList<stateChart_Variable> statechart_variables,        ArrayList<stateChart_Transition> statechart_transitions    ) {
        this.name = name;
        this.description = description;
        this.metadata = metadata;
        this.statechart_variables = statechart_variables;
        this.statechart_transitions = statechart_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getMetadata() {
        return metadata;
    }

    public void setMetadata(String metadata) {
        this.metadata = metadata;
    }

    public List<stateChart_Variable> getStatechart_variables() {
        return statechart_variables;
    }

    public void addStatechart_variable(Statechart_variable statechart_variable) {
        this.statechart_variables.add(statechart_variable);
    }
    public List<stateChart_Transition> getStatechart_transitions() {
        return statechart_transitions;
    }

    public void addStatechart_transition(Statechart_transition statechart_transition) {
        this.statechart_transitions.add(statechart_transition);
    }

}