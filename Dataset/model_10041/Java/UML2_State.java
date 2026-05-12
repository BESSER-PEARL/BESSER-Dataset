





import java.util.List;
import java.util.ArrayList;

public class UML2_State extends Vertex, Namespace, RedefinableElement {

    private boolean isSimple;
    private boolean isComposite;
    private boolean isOrthogonal;
    private boolean isSubmachineState;





    private UML2_State uml2_state;




    private UML2_Constraint uml2_constraint;




    private UML2_ObjectNode uml2_objectnode;




    private List<UML2_Trigger> uml2_triggers;


    public UML2_State(
        boolean isSimple,        boolean isComposite,        boolean isOrthogonal,        boolean isSubmachineState    ) {
        super(
        );
        this.isSimple = isSimple;
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSubmachineState = isSubmachineState;
        this.uml2_triggers = new ArrayList<>();
    }

    public UML2_State(
        boolean isSimple,        boolean isComposite,        boolean isOrthogonal,        boolean isSubmachineState        ArrayList<UML2_Trigger> uml2_triggers    ) {
        this.isSimple = isSimple;
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSubmachineState = isSubmachineState;
        this.uml2_triggers = uml2_triggers;
    }

    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
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
    public boolean getIssubmachinestate() {
        return isSubmachineState;
    }

    public void setIssubmachinestate(boolean isSubmachineState) {
        this.isSubmachineState = isSubmachineState;
    }

    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public UML2_ObjectNode getUml2_objectnode() {
        return uml2_objectnode;
    }

    public void setUml2_objectnode(UML2_ObjectNode uml2_objectnode) {
        this.uml2_objectnode = uml2_objectnode;
    }
    public List<UML2_Trigger> getUml2_triggers() {
        return uml2_triggers;
    }

    public void addUml2_trigger(Uml2_trigger uml2_trigger) {
        this.uml2_triggers.add(uml2_trigger);
    }

}