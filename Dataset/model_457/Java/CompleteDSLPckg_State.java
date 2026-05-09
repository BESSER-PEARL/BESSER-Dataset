





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_State extends Vertex, Namespace, RedefinableElement {

    private boolean isSubmachineState;
    private boolean isComposite;
    private boolean isSimple;
    private boolean isOrthogonal;





    private CompleteDSLPckg_Constraint completedslpckg_constraint;




    private CompleteDSLPckg_State completedslpckg_state;




    private List<CompleteDSLPckg_Trigger> completedslpckg_triggers;


    public CompleteDSLPckg_State(
        boolean isSubmachineState,        boolean isComposite,        boolean isSimple,        boolean isOrthogonal    ) {
        super(
        );
        this.isSubmachineState = isSubmachineState;
        this.isComposite = isComposite;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.completedslpckg_triggers = new ArrayList<>();
    }

    public CompleteDSLPckg_State(
        boolean isSubmachineState,        boolean isComposite,        boolean isSimple,        boolean isOrthogonal        ArrayList<CompleteDSLPckg_Trigger> completedslpckg_triggers    ) {
        this.isSubmachineState = isSubmachineState;
        this.isComposite = isComposite;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.completedslpckg_triggers = completedslpckg_triggers;
    }

    public boolean getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(boolean isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }
    public boolean getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(boolean isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }

    public CompleteDSLPckg_Constraint getCompletedslpckg_constraint() {
        return completedslpckg_constraint;
    }

    public void setCompletedslpckg_constraint(CompleteDSLPckg_Constraint completedslpckg_constraint) {
        this.completedslpckg_constraint = completedslpckg_constraint;
    }
    public CompleteDSLPckg_State getCompletedslpckg_state() {
        return completedslpckg_state;
    }

    public void setCompletedslpckg_state(CompleteDSLPckg_State completedslpckg_state) {
        this.completedslpckg_state = completedslpckg_state;
    }
    public List<CompleteDSLPckg_Trigger> getCompletedslpckg_triggers() {
        return completedslpckg_triggers;
    }

    public void addCompletedslpckg_trigger(Completedslpckg_trigger completedslpckg_trigger) {
        this.completedslpckg_triggers.add(completedslpckg_trigger);
    }

}