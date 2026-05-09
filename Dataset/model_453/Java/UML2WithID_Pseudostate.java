





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Pseudostate extends Vertex {

    private String kind;





    private UML2WithID_StateMachine uml2withid_statemachine;


    public UML2WithID_Pseudostate(
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

    public UML2WithID_StateMachine getUml2withid_statemachine() {
        return uml2withid_statemachine;
    }

    public void setUml2withid_statemachine(UML2WithID_StateMachine uml2withid_statemachine) {
        this.uml2withid_statemachine = uml2withid_statemachine;
    }

}