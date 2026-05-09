





import java.util.List;
import java.util.ArrayList;

public class statemachines_State extends Vertex {

    private boolean isDoActivityCompleted;
    private boolean isExitCompleted;
    private boolean isEntryCompleted;





    private statemachines_Behavior statemachines_behavior;




    private statemachines_Behavior statemachines_behavior;




    private List<statemachines_Trigger> statemachines_triggers;




    private List<statemachines_Region> statemachines_regions;




    private statemachines_Behavior statemachines_behavior;




    private statemachines_Region statemachines_region;


    public statemachines_State(
        boolean isDoActivityCompleted,        boolean isExitCompleted,        boolean isEntryCompleted    ) {
        super(
        );
        this.isDoActivityCompleted = isDoActivityCompleted;
        this.isExitCompleted = isExitCompleted;
        this.isEntryCompleted = isEntryCompleted;
        this.statemachines_triggers = new ArrayList<>();
        this.statemachines_regions = new ArrayList<>();
    }

    public statemachines_State(
        boolean isDoActivityCompleted,        boolean isExitCompleted,        boolean isEntryCompleted        ArrayList<statemachines_Trigger> statemachines_triggers,        ArrayList<statemachines_Region> statemachines_regions    ) {
        this.isDoActivityCompleted = isDoActivityCompleted;
        this.isExitCompleted = isExitCompleted;
        this.isEntryCompleted = isEntryCompleted;
        this.statemachines_triggers = statemachines_triggers;
        this.statemachines_regions = statemachines_regions;
    }

    public boolean getIsdoactivitycompleted() {
        return isDoActivityCompleted;
    }

    public void setIsdoactivitycompleted(boolean isDoActivityCompleted) {
        this.isDoActivityCompleted = isDoActivityCompleted;
    }
    public boolean getIsexitcompleted() {
        return isExitCompleted;
    }

    public void setIsexitcompleted(boolean isExitCompleted) {
        this.isExitCompleted = isExitCompleted;
    }
    public boolean getIsentrycompleted() {
        return isEntryCompleted;
    }

    public void setIsentrycompleted(boolean isEntryCompleted) {
        this.isEntryCompleted = isEntryCompleted;
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
    public List<statemachines_Trigger> getStatemachines_triggers() {
        return statemachines_triggers;
    }

    public void addStatemachines_trigger(Statemachines_trigger statemachines_trigger) {
        this.statemachines_triggers.add(statemachines_trigger);
    }
    public List<statemachines_Region> getStatemachines_regions() {
        return statemachines_regions;
    }

    public void addStatemachines_region(Statemachines_region statemachines_region) {
        this.statemachines_regions.add(statemachines_region);
    }
    public statemachines_Behavior getStatemachines_behavior() {
        return statemachines_behavior;
    }

    public void setStatemachines_behavior(statemachines_Behavior statemachines_behavior) {
        this.statemachines_behavior = statemachines_behavior;
    }
    public statemachines_Region getStatemachines_region() {
        return statemachines_region;
    }

    public void setStatemachines_region(statemachines_Region statemachines_region) {
        this.statemachines_region = statemachines_region;
    }

}