





import java.util.List;
import java.util.ArrayList;

public class UMLModel_StateMachine extends Behavior {

    private String extendedStateMachine;
    private String submachineState;





    private List<UMLModel_Pseudostate> umlmodel_pseudostates;


    public UMLModel_StateMachine(
        String extendedStateMachine,        String submachineState    ) {
        super(
        );
        this.extendedStateMachine = extendedStateMachine;
        this.submachineState = submachineState;
        this.umlmodel_pseudostates = new ArrayList<>();
    }

    public UMLModel_StateMachine(
        String extendedStateMachine,        String submachineState        ArrayList<UMLModel_Pseudostate> umlmodel_pseudostates    ) {
        this.extendedStateMachine = extendedStateMachine;
        this.submachineState = submachineState;
        this.umlmodel_pseudostates = umlmodel_pseudostates;
    }

    public String getExtendedstatemachine() {
        return extendedStateMachine;
    }

    public void setExtendedstatemachine(String extendedStateMachine) {
        this.extendedStateMachine = extendedStateMachine;
    }
    public String getSubmachinestate() {
        return submachineState;
    }

    public void setSubmachinestate(String submachineState) {
        this.submachineState = submachineState;
    }

    public List<UMLModel_Pseudostate> getUmlmodel_pseudostates() {
        return umlmodel_pseudostates;
    }

    public void addUmlmodel_pseudostate(Umlmodel_pseudostate umlmodel_pseudostate) {
        this.umlmodel_pseudostates.add(umlmodel_pseudostate);
    }

}