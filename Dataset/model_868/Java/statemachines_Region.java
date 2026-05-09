





import java.util.List;
import java.util.ArrayList;

public class statemachines_Region extends NamedElement {






    private List<statemachines_Transition> statemachines_transitions;




    private statemachines_Vertex statemachines_vertex;




    private List<statemachines_Vertex> statemachines_vertexs;




    private statemachines_Vertex statemachines_vertex;




    private statemachines_StateMachine statemachines_statemachine;




    private statemachines_StateMachine statemachines_statemachine;




    private statemachines_Transition statemachines_transition;


    public statemachines_Region(
    ) {
        super(
        );
        this.statemachines_transitions = new ArrayList<>();
        this.statemachines_vertexs = new ArrayList<>();
    }

    public statemachines_Region(
        ArrayList<statemachines_Transition> statemachines_transitions,        ArrayList<statemachines_Vertex> statemachines_vertexs    ) {
        this.statemachines_transitions = statemachines_transitions;
        this.statemachines_vertexs = statemachines_vertexs;
    }


    public List<statemachines_Transition> getStatemachines_transitions() {
        return statemachines_transitions;
    }

    public void addStatemachines_transition(Statemachines_transition statemachines_transition) {
        this.statemachines_transitions.add(statemachines_transition);
    }
    public statemachines_Vertex getStatemachines_vertex() {
        return statemachines_vertex;
    }

    public void setStatemachines_vertex(statemachines_Vertex statemachines_vertex) {
        this.statemachines_vertex = statemachines_vertex;
    }
    public List<statemachines_Vertex> getStatemachines_vertexs() {
        return statemachines_vertexs;
    }

    public void addStatemachines_vertex(Statemachines_vertex statemachines_vertex) {
        this.statemachines_vertexs.add(statemachines_vertex);
    }
    public statemachines_Vertex getStatemachines_vertex() {
        return statemachines_vertex;
    }

    public void setStatemachines_vertex(statemachines_Vertex statemachines_vertex) {
        this.statemachines_vertex = statemachines_vertex;
    }
    public statemachines_StateMachine getStatemachines_statemachine() {
        return statemachines_statemachine;
    }

    public void setStatemachines_statemachine(statemachines_StateMachine statemachines_statemachine) {
        this.statemachines_statemachine = statemachines_statemachine;
    }
    public statemachines_StateMachine getStatemachines_statemachine() {
        return statemachines_statemachine;
    }

    public void setStatemachines_statemachine(statemachines_StateMachine statemachines_statemachine) {
        this.statemachines_statemachine = statemachines_statemachine;
    }
    public statemachines_Transition getStatemachines_transition() {
        return statemachines_transition;
    }

    public void setStatemachines_transition(statemachines_Transition statemachines_transition) {
        this.statemachines_transition = statemachines_transition;
    }

}