





import java.util.List;
import java.util.ArrayList;

public class pivot_State extends Namespace, Vertex {

    private String isSubmachineState;
    private String isComposite;
    private String isOrthogonal;
    private String isSimple;





    private pivot_Behavior pivot_behavior;




    private pivot_Behavior pivot_behavior;




    private pivot_StateExp pivot_stateexp;




    private pivot_State pivot_state;




    private pivot_Constraint pivot_constraint;




    private List<pivot_Trigger> pivot_triggers;




    private pivot_Behavior pivot_behavior;


    public pivot_State(
        String isSubmachineState,        String isComposite,        String isOrthogonal,        String isSimple    ) {
        super(
        );
        this.isSubmachineState = isSubmachineState;
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSimple = isSimple;
        this.pivot_triggers = new ArrayList<>();
    }

    public pivot_State(
        String isSubmachineState,        String isComposite,        String isOrthogonal,        String isSimple        ArrayList<pivot_Trigger> pivot_triggers    ) {
        this.isSubmachineState = isSubmachineState;
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSimple = isSimple;
        this.pivot_triggers = pivot_triggers;
    }

    public String getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(String isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(String isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public String getIssimple() {
        return isSimple;
    }

    public void setIssimple(String isSimple) {
        this.isSimple = isSimple;
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
    public pivot_Behavior getPivot_behavior() {
        return pivot_behavior;
    }

    public void setPivot_behavior(pivot_Behavior pivot_behavior) {
        this.pivot_behavior = pivot_behavior;
    }

}