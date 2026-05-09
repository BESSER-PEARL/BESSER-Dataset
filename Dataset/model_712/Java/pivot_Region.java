





import java.util.List;
import java.util.ArrayList;

public class pivot_Region extends Namespace {






    private pivot_Region pivot_region;




    private pivot_State pivot_state;




    private List<pivot_Transition> pivot_transitions;




    private pivot_State pivot_state;




    private pivot_Vertex pivot_vertex;




    private List<pivot_Vertex> pivot_vertexs;




    private pivot_Transition pivot_transition;


    public pivot_Region(
    ) {
        super(
        );
        this.pivot_transitions = new ArrayList<>();
        this.pivot_vertexs = new ArrayList<>();
    }

    public pivot_Region(
        ArrayList<pivot_Transition> pivot_transitions,        ArrayList<pivot_Vertex> pivot_vertexs    ) {
        this.pivot_transitions = pivot_transitions;
        this.pivot_vertexs = pivot_vertexs;
    }


    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }
    public List<pivot_Transition> getPivot_transitions() {
        return pivot_transitions;
    }

    public void addPivot_transition(Pivot_transition pivot_transition) {
        this.pivot_transitions.add(pivot_transition);
    }
    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }
    public pivot_Vertex getPivot_vertex() {
        return pivot_vertex;
    }

    public void setPivot_vertex(pivot_Vertex pivot_vertex) {
        this.pivot_vertex = pivot_vertex;
    }
    public List<pivot_Vertex> getPivot_vertexs() {
        return pivot_vertexs;
    }

    public void addPivot_vertex(Pivot_vertex pivot_vertex) {
        this.pivot_vertexs.add(pivot_vertex);
    }
    public pivot_Transition getPivot_transition() {
        return pivot_transition;
    }

    public void setPivot_transition(pivot_Transition pivot_transition) {
        this.pivot_transition = pivot_transition;
    }

}