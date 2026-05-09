





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Pseudostate extends Vertex {

    private String stateMachine;
    private String state;
    private String kind;



    public UMLModel_Pseudostate(
        String stateMachine,        String state,        String kind    ) {
        super(
        );
        this.stateMachine = stateMachine;
        this.state = state;
        this.kind = kind;
    }


    public String getStatemachine() {
        return stateMachine;
    }

    public void setStatemachine(String stateMachine) {
        this.stateMachine = stateMachine;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}