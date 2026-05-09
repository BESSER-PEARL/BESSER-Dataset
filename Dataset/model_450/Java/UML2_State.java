





import java.util.List;
import java.util.ArrayList;

public class UML2_State extends Namespace, Vertex, RedefinableElement {

    private boolean isSubmachineState;
    private boolean isComposite;
    private boolean isOrthogonal;
    private boolean isSimple;





    private UML2_State uml2_state;




    private UML2_Constraint uml2_constraint;


    public UML2_State(
        boolean isSubmachineState,        boolean isComposite,        boolean isOrthogonal,        boolean isSimple    ) {
        super(
        );
        this.isSubmachineState = isSubmachineState;
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSimple = isSimple;
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

}