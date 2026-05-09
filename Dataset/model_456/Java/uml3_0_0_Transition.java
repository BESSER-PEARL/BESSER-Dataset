





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Transition extends Namespace, RedefinableElement {

    private String kind;





    private uml3_0_0_Transition uml3_0_0_transition;


    public uml3_0_0_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public uml3_0_0_Transition getUml3_0_0_transition() {
        return uml3_0_0_transition;
    }

    public void setUml3_0_0_transition(uml3_0_0_Transition uml3_0_0_transition) {
        this.uml3_0_0_transition = uml3_0_0_transition;
    }

}