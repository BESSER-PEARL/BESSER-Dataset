





import java.util.List;
import java.util.ArrayList;

public class pivot_State extends Namespace, Vertex {

    private String isOrthogonal;
    private String isComposite;
    private String isSubmachineState;
    private String isSimple;





    private pivot_Constraint pivot_constraint;




    private pivot_Constraint pivot_constraint;




    private List<pivot_Trigger> pivot_triggers;




    private pivot_Trigger pivot_trigger;




    private List<pivot_Region> pivot_regions;




    private pivot_State pivot_state;




    private pivot_Region pivot_region;




    private pivot_StateExp pivot_stateexp;


    public pivot_State(
        String isOrthogonal,        String isComposite,        String isSubmachineState,        String isSimple    ) {
        super(
        );
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.pivot_triggers = new ArrayList<>();
        this.pivot_regions = new ArrayList<>();
    }

    public pivot_State(
        String isOrthogonal,        String isComposite,        String isSubmachineState,        String isSimple        ArrayList<pivot_Trigger> pivot_triggers,        ArrayList<pivot_Region> pivot_regions    ) {
        this.isOrthogonal = isOrthogonal;
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.pivot_triggers = pivot_triggers;
        this.pivot_regions = pivot_regions;
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
    public String getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(String isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
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
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public List<pivot_Trigger> getPivot_triggers() {
        return pivot_triggers;
    }

    public void addPivot_trigger(Pivot_trigger pivot_trigger) {
        this.pivot_triggers.add(pivot_trigger);
    }
    public pivot_Trigger getPivot_trigger() {
        return pivot_trigger;
    }

    public void setPivot_trigger(pivot_Trigger pivot_trigger) {
        this.pivot_trigger = pivot_trigger;
    }
    public List<pivot_Region> getPivot_regions() {
        return pivot_regions;
    }

    public void addPivot_region(Pivot_region pivot_region) {
        this.pivot_regions.add(pivot_region);
    }
    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
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

}