





import java.util.List;
import java.util.ArrayList;

public class pivot_State extends Vertex, Namespace {

    private String isSubmachineState;
    private String isOrthogonal;
    private String isComposite;
    private String isSimple;





    private pivot_Constraint pivot_constraint;




    private pivot_Behavior pivot_behavior;




    private pivot_Behavior pivot_behavior;




    private pivot_Behavior pivot_behavior;




    private pivot_Constraint pivot_constraint;




    private pivot_StateMachine pivot_statemachine;




    private pivot_Region pivot_region;




    private pivot_StateExp pivot_stateexp;




    private pivot_State pivot_state;




    private List<pivot_Region> pivot_regions;




    private pivot_Trigger pivot_trigger;




    private pivot_StateMachine pivot_statemachine;




    private List<pivot_Trigger> pivot_triggers;


    public pivot_State(
        String isSubmachineState,        String isOrthogonal,        String isComposite,        String isSimple    ) {
        super(
        );
        this.isSubmachineState = isSubmachineState;
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSimple = isSimple;
        this.pivot_regions = new ArrayList<>();
        this.pivot_triggers = new ArrayList<>();
    }

    public pivot_State(
        String isSubmachineState,        String isOrthogonal,        String isComposite,        String isSimple        ArrayList<pivot_Region> pivot_regions,        ArrayList<pivot_Trigger> pivot_triggers    ) {
        this.isSubmachineState = isSubmachineState;
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSimple = isSimple;
        this.pivot_regions = pivot_regions;
        this.pivot_triggers = pivot_triggers;
    }

    public String getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(String isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }
    public String getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(String isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIssimple() {
        return isSimple;
    }

    public void setIssimple(String isSimple) {
        this.isSimple = isSimple;
    }

    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_Behavior getPivot_behavior() {
        return pivot_behavior;
    }

    public void setPivot_behavior(pivot_Behavior pivot_behavior) {
        this.pivot_behavior = pivot_behavior;
    }
    public pivot_Behavior getPivot_behavior() {
        return pivot_behavior;
    }

    public void setPivot_behavior(pivot_Behavior pivot_behavior) {
        this.pivot_behavior = pivot_behavior;
    }
    public pivot_Behavior getPivot_behavior() {
        return pivot_behavior;
    }

    public void setPivot_behavior(pivot_Behavior pivot_behavior) {
        this.pivot_behavior = pivot_behavior;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_StateMachine getPivot_statemachine() {
        return pivot_statemachine;
    }

    public void setPivot_statemachine(pivot_StateMachine pivot_statemachine) {
        this.pivot_statemachine = pivot_statemachine;
    }
    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public pivot_StateExp getPivot_stateexp() {
        return pivot_stateexp;
    }

    public void setPivot_stateexp(pivot_StateExp pivot_stateexp) {
        this.pivot_stateexp = pivot_stateexp;
    }
    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }
    public List<pivot_Region> getPivot_regions() {
        return pivot_regions;
    }

    public void addPivot_region(Pivot_region pivot_region) {
        this.pivot_regions.add(pivot_region);
    }
    public pivot_Trigger getPivot_trigger() {
        return pivot_trigger;
    }

    public void setPivot_trigger(pivot_Trigger pivot_trigger) {
        this.pivot_trigger = pivot_trigger;
    }
    public pivot_StateMachine getPivot_statemachine() {
        return pivot_statemachine;
    }

    public void setPivot_statemachine(pivot_StateMachine pivot_statemachine) {
        this.pivot_statemachine = pivot_statemachine;
    }
    public List<pivot_Trigger> getPivot_triggers() {
        return pivot_triggers;
    }

    public void addPivot_trigger(Pivot_trigger pivot_trigger) {
        this.pivot_triggers.add(pivot_trigger);
    }

}