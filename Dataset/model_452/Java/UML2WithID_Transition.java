





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Transition extends RedefinableElement {

    private String kind;





    private UML2WithID_Transition uml2withid_transition;


    public UML2WithID_Transition(
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

    public UML2WithID_Transition getUml2withid_transition() {
        return uml2withid_transition;
    }

    public void setUml2withid_transition(UML2WithID_Transition uml2withid_transition) {
        this.uml2withid_transition = uml2withid_transition;
    }

}