





import java.util.List;
import java.util.ArrayList;

public class pivot_State extends Vertex, Namespace {

    private String isComposite;
    private String isSubmachineState;
    private String isOrthogonal;
    private String isSimple;





    private pivot_State pivot_state;


    public pivot_State(
        String isComposite,        String isSubmachineState,        String isOrthogonal,        String isSimple    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isSubmachineState = isSubmachineState;
        this.isOrthogonal = isOrthogonal;
        this.isSimple = isSimple;
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

    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }

}