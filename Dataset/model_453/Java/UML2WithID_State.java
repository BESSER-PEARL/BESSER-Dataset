





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_State extends RedefinableElement, Namespace, Vertex {

    private boolean isSubmachineState;
    private boolean isComposite;
    private boolean isOrthogonal;
    private boolean isSimple;





    private UML2WithID_Activity uml2withid_activity;




    private UML2WithID_Activity uml2withid_activity;




    private UML2WithID_Activity uml2withid_activity;




    private UML2WithID_Constraint uml2withid_constraint;




    private UML2WithID_State uml2withid_state;




    private UML2WithID_StateMachine uml2withid_statemachine;




    private UML2WithID_ObjectNode uml2withid_objectnode;




    private List<UML2WithID_Trigger> uml2withid_triggers;


    public UML2WithID_State(
        boolean isSubmachineState,        boolean isComposite,        boolean isOrthogonal,        boolean isSimple    ) {
        super(
        );
        this.isSubmachineState = isSubmachineState;
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSimple = isSimple;
        this.uml2withid_triggers = new ArrayList<>();
    }

    public UML2WithID_State(
        boolean isSubmachineState,        boolean isComposite,        boolean isOrthogonal,        boolean isSimple        ArrayList<UML2WithID_Trigger> uml2withid_triggers    ) {
        this.isSubmachineState = isSubmachineState;
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSimple = isSimple;
        this.uml2withid_triggers = uml2withid_triggers;
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
    public boolean getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(boolean isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }

    public UML2WithID_Activity getUml2withid_activity() {
        return uml2withid_activity;
    }

    public void setUml2withid_activity(UML2WithID_Activity uml2withid_activity) {
        this.uml2withid_activity = uml2withid_activity;
    }
    public UML2WithID_Activity getUml2withid_activity() {
        return uml2withid_activity;
    }

    public void setUml2withid_activity(UML2WithID_Activity uml2withid_activity) {
        this.uml2withid_activity = uml2withid_activity;
    }
    public UML2WithID_Activity getUml2withid_activity() {
        return uml2withid_activity;
    }

    public void setUml2withid_activity(UML2WithID_Activity uml2withid_activity) {
        this.uml2withid_activity = uml2withid_activity;
    }
    public UML2WithID_Constraint getUml2withid_constraint() {
        return uml2withid_constraint;
    }

    public void setUml2withid_constraint(UML2WithID_Constraint uml2withid_constraint) {
        this.uml2withid_constraint = uml2withid_constraint;
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public UML2WithID_StateMachine getUml2withid_statemachine() {
        return uml2withid_statemachine;
    }

    public void setUml2withid_statemachine(UML2WithID_StateMachine uml2withid_statemachine) {
        this.uml2withid_statemachine = uml2withid_statemachine;
    }
    public UML2WithID_ObjectNode getUml2withid_objectnode() {
        return uml2withid_objectnode;
    }

    public void setUml2withid_objectnode(UML2WithID_ObjectNode uml2withid_objectnode) {
        this.uml2withid_objectnode = uml2withid_objectnode;
    }
    public List<UML2WithID_Trigger> getUml2withid_triggers() {
        return uml2withid_triggers;
    }

    public void addUml2withid_trigger(Uml2withid_trigger uml2withid_trigger) {
        this.uml2withid_triggers.add(uml2withid_trigger);
    }

}