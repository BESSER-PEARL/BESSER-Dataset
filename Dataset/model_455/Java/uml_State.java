





import java.util.List;
import java.util.ArrayList;

public class uml_State extends Namespace, Vertex, RedefinableElement {

    private String isComposite;
    private String isOrthogonal;
    private String isSubmachineState;
    private String isSimple;





    private uml_State uml_state;


    public uml_State(
        String isComposite,        String isOrthogonal,        String isSubmachineState,        String isSimple    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isOrthogonal = isOrthogonal;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
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

    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }

}