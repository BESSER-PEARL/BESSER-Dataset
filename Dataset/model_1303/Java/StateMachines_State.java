





import java.util.List;
import java.util.ArrayList;

public class StateMachines_State extends Vertex {






    private List<StateMachines_Region> statemachines_regions;




    private List<StateMachines_Trigger> statemachines_triggers;




    private StateMachines_StateMachine statemachines_statemachine;




    private List<StateMachines_ConnectionPointReference> statemachines_connectionpointreferences;




    private List<StateMachines_Pseudostate> statemachines_pseudostates;


    public StateMachines_State(
    ) {
        super(
        );
        this.statemachines_regions = new ArrayList<>();
        this.statemachines_triggers = new ArrayList<>();
        this.statemachines_connectionpointreferences = new ArrayList<>();
        this.statemachines_pseudostates = new ArrayList<>();
    }

    public StateMachines_State(
        ArrayList<StateMachines_Region> statemachines_regions,        ArrayList<StateMachines_Trigger> statemachines_triggers,        ArrayList<StateMachines_ConnectionPointReference> statemachines_connectionpointreferences,        ArrayList<StateMachines_Pseudostate> statemachines_pseudostates    ) {
        this.statemachines_regions = statemachines_regions;
        this.statemachines_triggers = statemachines_triggers;
        this.statemachines_connectionpointreferences = statemachines_connectionpointreferences;
        this.statemachines_pseudostates = statemachines_pseudostates;
    }


    public List<StateMachines_Region> getStatemachines_regions() {
        return statemachines_regions;
    }

    public void addStatemachines_region(Statemachines_region statemachines_region) {
        this.statemachines_regions.add(statemachines_region);
    }
    public List<StateMachines_Trigger> getStatemachines_triggers() {
        return statemachines_triggers;
    }

    public void addStatemachines_trigger(Statemachines_trigger statemachines_trigger) {
        this.statemachines_triggers.add(statemachines_trigger);
    }
    public StateMachines_StateMachine getStatemachines_statemachine() {
        return statemachines_statemachine;
    }

    public void setStatemachines_statemachine(StateMachines_StateMachine statemachines_statemachine) {
        this.statemachines_statemachine = statemachines_statemachine;
    }
    public List<StateMachines_ConnectionPointReference> getStatemachines_connectionpointreferences() {
        return statemachines_connectionpointreferences;
    }

    public void addStatemachines_connectionpointreference(Statemachines_connectionpointreference statemachines_connectionpointreference) {
        this.statemachines_connectionpointreferences.add(statemachines_connectionpointreference);
    }
    public List<StateMachines_Pseudostate> getStatemachines_pseudostates() {
        return statemachines_pseudostates;
    }

    public void addStatemachines_pseudostate(Statemachines_pseudostate statemachines_pseudostate) {
        this.statemachines_pseudostates.add(statemachines_pseudostate);
    }

}