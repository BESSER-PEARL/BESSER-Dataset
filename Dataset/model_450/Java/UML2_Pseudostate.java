





import java.util.List;
import java.util.ArrayList;

public class UML2_Pseudostate extends Vertex {

    private String kind;





    private UML2_StateMachine uml2_statemachine;


    public UML2_Pseudostate(
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

    public UML2_StateMachine getUml2_statemachine() {
        return uml2_statemachine;
    }

    public void setUml2_statemachine(UML2_StateMachine uml2_statemachine) {
        this.uml2_statemachine = uml2_statemachine;
    }

}