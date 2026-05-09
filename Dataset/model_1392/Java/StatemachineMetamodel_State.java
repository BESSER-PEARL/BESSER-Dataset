





import java.util.List;
import java.util.ArrayList;

public class StatemachineMetamodel_State  {

    private String name;





    private StatemachineMetamodel_Transition statemachinemetamodel_transition;




    private List<StatemachineMetamodel_Transition> statemachinemetamodel_transitions;




    private StatemachineMetamodel_Statemachine statemachinemetamodel_statemachine;


    public StatemachineMetamodel_State(
        String name    ) {
        this.name = name;
        this.statemachinemetamodel_transitions = new ArrayList<>();
    }

    public StatemachineMetamodel_State(
        String name        ArrayList<StatemachineMetamodel_Transition> statemachinemetamodel_transitions    ) {
        this.name = name;
        this.statemachinemetamodel_transitions = statemachinemetamodel_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StatemachineMetamodel_Transition getStatemachinemetamodel_transition() {
        return statemachinemetamodel_transition;
    }

    public void setStatemachinemetamodel_transition(StatemachineMetamodel_Transition statemachinemetamodel_transition) {
        this.statemachinemetamodel_transition = statemachinemetamodel_transition;
    }
    public List<StatemachineMetamodel_Transition> getStatemachinemetamodel_transitions() {
        return statemachinemetamodel_transitions;
    }

    public void addStatemachinemetamodel_transition(Statemachinemetamodel_transition statemachinemetamodel_transition) {
        this.statemachinemetamodel_transitions.add(statemachinemetamodel_transition);
    }
    public StatemachineMetamodel_Statemachine getStatemachinemetamodel_statemachine() {
        return statemachinemetamodel_statemachine;
    }

    public void setStatemachinemetamodel_statemachine(StatemachineMetamodel_Statemachine statemachinemetamodel_statemachine) {
        this.statemachinemetamodel_statemachine = statemachinemetamodel_statemachine;
    }

}