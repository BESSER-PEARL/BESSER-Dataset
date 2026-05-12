





import java.util.List;
import java.util.ArrayList;

public class uml_Region  {






    private List<uml_Transition> uml_transitions;




    private List<uml_Vertex> uml_vertexs;




    private uml_StateMachine uml_statemachine;




    private uml_Vertex uml_vertex;


    public uml_Region(
    ) {
        this.uml_transitions = new ArrayList<>();
        this.uml_vertexs = new ArrayList<>();
    }

    public uml_Region(
        ArrayList<uml_Transition> uml_transitions,        ArrayList<uml_Vertex> uml_vertexs    ) {
        this.uml_transitions = uml_transitions;
        this.uml_vertexs = uml_vertexs;
    }


    public List<uml_Transition> getUml_transitions() {
        return uml_transitions;
    }

    public void addUml_transition(Uml_transition uml_transition) {
        this.uml_transitions.add(uml_transition);
    }
    public List<uml_Vertex> getUml_vertexs() {
        return uml_vertexs;
    }

    public void addUml_vertex(Uml_vertex uml_vertex) {
        this.uml_vertexs.add(uml_vertex);
    }
    public uml_StateMachine getUml_statemachine() {
        return uml_statemachine;
    }

    public void setUml_statemachine(uml_StateMachine uml_statemachine) {
        this.uml_statemachine = uml_statemachine;
    }
    public uml_Vertex getUml_vertex() {
        return uml_vertex;
    }

    public void setUml_vertex(uml_Vertex uml_vertex) {
        this.uml_vertex = uml_vertex;
    }

}