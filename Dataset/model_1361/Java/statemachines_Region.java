





import java.util.List;
import java.util.ArrayList;

public class statemachines_Region extends NamedElement {






    private statemachines_StateMachine statemachines_statemachine;




    private statemachines_Vertex statemachines_vertex;




    private statemachines_StateMachine statemachines_statemachine;




    private List<statemachines_Vertex> statemachines_vertexs;


    public statemachines_Region(
    ) {
        super(
        );
        this.statemachines_vertexs = new ArrayList<>();
    }

    public statemachines_Region(
        ArrayList<statemachines_Vertex> statemachines_vertexs    ) {
        this.statemachines_vertexs = statemachines_vertexs;
    }


    public statemachines_StateMachine getStatemachines_statemachine() {
        return statemachines_statemachine;
    }

    public void setStatemachines_statemachine(statemachines_StateMachine statemachines_statemachine) {
        this.statemachines_statemachine = statemachines_statemachine;
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
    public List<statemachines_Vertex> getStatemachines_vertexs() {
        return statemachines_vertexs;
    }

    public void addStatemachines_vertex(Statemachines_vertex statemachines_vertex) {
        this.statemachines_vertexs.add(statemachines_vertex);
    }

}