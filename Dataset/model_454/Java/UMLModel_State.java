





import java.util.List;
import java.util.ArrayList;

public class UMLModel_State extends Vertex, RedefinableElement, Namespace {

    private String isComposite;
    private String redefinedState;
    private String isSubmachineState;
    private String isSimple;
    private String isOrthogonal;
    private String submachine;





    private List<UMLModel_Pseudostate> umlmodel_pseudostates;




    private List<UMLModel_ConnectionPointReference> umlmodel_connectionpointreferences;


    public UMLModel_State(
        String isComposite,        String redefinedState,        String isSubmachineState,        String isSimple,        String isOrthogonal,        String submachine    ) {
        super(
        );
        this.isComposite = isComposite;
        this.redefinedState = redefinedState;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.submachine = submachine;
        this.umlmodel_pseudostates = new ArrayList<>();
        this.umlmodel_connectionpointreferences = new ArrayList<>();
    }

    public UMLModel_State(
        String isComposite,        String redefinedState,        String isSubmachineState,        String isSimple,        String isOrthogonal,        String submachine        ArrayList<UMLModel_Pseudostate> umlmodel_pseudostates,        ArrayList<UMLModel_ConnectionPointReference> umlmodel_connectionpointreferences    ) {
        this.isComposite = isComposite;
        this.redefinedState = redefinedState;
        this.isSubmachineState = isSubmachineState;
        this.isSimple = isSimple;
        this.isOrthogonal = isOrthogonal;
        this.submachine = submachine;
        this.umlmodel_pseudostates = umlmodel_pseudostates;
        this.umlmodel_connectionpointreferences = umlmodel_connectionpointreferences;
    }

    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getRedefinedstate() {
        return redefinedState;
    }

    public void setRedefinedstate(String redefinedState) {
        this.redefinedState = redefinedState;
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
    public String getIsorthogonal() {
        return isOrthogonal;
    }

    public void setIsorthogonal(String isOrthogonal) {
        this.isOrthogonal = isOrthogonal;
    }
    public String getSubmachine() {
        return submachine;
    }

    public void setSubmachine(String submachine) {
        this.submachine = submachine;
    }

    public List<UMLModel_Pseudostate> getUmlmodel_pseudostates() {
        return umlmodel_pseudostates;
    }

    public void addUmlmodel_pseudostate(Umlmodel_pseudostate umlmodel_pseudostate) {
        this.umlmodel_pseudostates.add(umlmodel_pseudostate);
    }
    public List<UMLModel_ConnectionPointReference> getUmlmodel_connectionpointreferences() {
        return umlmodel_connectionpointreferences;
    }

    public void addUmlmodel_connectionpointreference(Umlmodel_connectionpointreference umlmodel_connectionpointreference) {
        this.umlmodel_connectionpointreferences.add(umlmodel_connectionpointreference);
    }

}