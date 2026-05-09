





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Region extends RedefinableElement, Namespace {

    private String extendedRegion;
    private String stateMachine;
    private String state;





    private List<UMLModel_Transition> umlmodel_transitions;




    private UMLModel_StateMachine umlmodel_statemachine;




    private List<UMLModel_Vertex> umlmodel_vertexs;




    private UMLModel_State umlmodel_state;


    public UMLModel_Region(
        String extendedRegion,        String stateMachine,        String state    ) {
        super(
        );
        this.extendedRegion = extendedRegion;
        this.stateMachine = stateMachine;
        this.state = state;
        this.umlmodel_transitions = new ArrayList<>();
        this.umlmodel_vertexs = new ArrayList<>();
    }

    public UMLModel_Region(
        String extendedRegion,        String stateMachine,        String state        ArrayList<UMLModel_Transition> umlmodel_transitions,        ArrayList<UMLModel_Vertex> umlmodel_vertexs    ) {
        this.extendedRegion = extendedRegion;
        this.stateMachine = stateMachine;
        this.state = state;
        this.umlmodel_transitions = umlmodel_transitions;
        this.umlmodel_vertexs = umlmodel_vertexs;
    }

    public String getExtendedregion() {
        return extendedRegion;
    }

    public void setExtendedregion(String extendedRegion) {
        this.extendedRegion = extendedRegion;
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

    public List<UMLModel_Transition> getUmlmodel_transitions() {
        return umlmodel_transitions;
    }

    public void addUmlmodel_transition(Umlmodel_transition umlmodel_transition) {
        this.umlmodel_transitions.add(umlmodel_transition);
    }
    public UMLModel_StateMachine getUmlmodel_statemachine() {
        return umlmodel_statemachine;
    }

    public void setUmlmodel_statemachine(UMLModel_StateMachine umlmodel_statemachine) {
        this.umlmodel_statemachine = umlmodel_statemachine;
    }
    public List<UMLModel_Vertex> getUmlmodel_vertexs() {
        return umlmodel_vertexs;
    }

    public void addUmlmodel_vertex(Umlmodel_vertex umlmodel_vertex) {
        this.umlmodel_vertexs.add(umlmodel_vertex);
    }
    public UMLModel_State getUmlmodel_state() {
        return umlmodel_state;
    }

    public void setUmlmodel_state(UMLModel_State umlmodel_state) {
        this.umlmodel_state = umlmodel_state;
    }

}