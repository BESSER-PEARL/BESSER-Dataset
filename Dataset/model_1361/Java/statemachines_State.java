





import java.util.List;
import java.util.ArrayList;

public class statemachines_State extends Vertex {






    private statemachines_Behavior statemachines_behavior;




    private statemachines_Behavior statemachines_behavior;




    private List<statemachines_Region> statemachines_regions;




    private List<statemachines_Trigger> statemachines_triggers;




    private statemachines_Region statemachines_region;




    private statemachines_Behavior statemachines_behavior;


    public statemachines_State(
    ) {
        super(
        );
        this.statemachines_regions = new ArrayList<>();
        this.statemachines_triggers = new ArrayList<>();
    }

    public statemachines_State(
        ArrayList<statemachines_Region> statemachines_regions,        ArrayList<statemachines_Trigger> statemachines_triggers    ) {
        this.statemachines_regions = statemachines_regions;
        this.statemachines_triggers = statemachines_triggers;
    }


    public statemachines_Behavior getStatemachines_behavior() {
        return statemachines_behavior;
    }

    public void setStatemachines_behavior(statemachines_Behavior statemachines_behavior) {
        this.statemachines_behavior = statemachines_behavior;
    }
    public statemachines_Behavior getStatemachines_behavior() {
        return statemachines_behavior;
    }

    public void setStatemachines_behavior(statemachines_Behavior statemachines_behavior) {
        this.statemachines_behavior = statemachines_behavior;
    }
    public List<statemachines_Region> getStatemachines_regions() {
        return statemachines_regions;
    }

    public void addStatemachines_region(Statemachines_region statemachines_region) {
        this.statemachines_regions.add(statemachines_region);
    }
    public List<statemachines_Trigger> getStatemachines_triggers() {
        return statemachines_triggers;
    }

    public void addStatemachines_trigger(Statemachines_trigger statemachines_trigger) {
        this.statemachines_triggers.add(statemachines_trigger);
    }
    public statemachines_Region getStatemachines_region() {
        return statemachines_region;
    }

    public void setStatemachines_region(statemachines_Region statemachines_region) {
        this.statemachines_region = statemachines_region;
    }
    public statemachines_Behavior getStatemachines_behavior() {
        return statemachines_behavior;
    }

    public void setStatemachines_behavior(statemachines_Behavior statemachines_behavior) {
        this.statemachines_behavior = statemachines_behavior;
    }

}