





import java.util.List;
import java.util.ArrayList;

public class sm_Graph  {

    private String name;





    private sm_Mark sm_mark;




    private sm_Edge sm_edge;




    private List<sm_Node> sm_nodes;




    private List<sm_Edge> sm_edges;




    private List<sm_Mark> sm_marks;




    private sm_Node sm_node;


    public sm_Graph(
        String name    ) {
        this.name = name;
        this.sm_nodes = new ArrayList<>();
        this.sm_edges = new ArrayList<>();
        this.sm_marks = new ArrayList<>();
    }

    public sm_Graph(
        String name        ArrayList<sm_Node> sm_nodes,        ArrayList<sm_Edge> sm_edges,        ArrayList<sm_Mark> sm_marks    ) {
        this.name = name;
        this.sm_nodes = sm_nodes;
        this.sm_edges = sm_edges;
        this.sm_marks = sm_marks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sm_Mark getSm_mark() {
        return sm_mark;
    }

    public void setSm_mark(sm_Mark sm_mark) {
        this.sm_mark = sm_mark;
    }
    public sm_Edge getSm_edge() {
        return sm_edge;
    }

    public void setSm_edge(sm_Edge sm_edge) {
        this.sm_edge = sm_edge;
    }
    public List<sm_Node> getSm_nodes() {
        return sm_nodes;
    }

    public void addSm_node(Sm_node sm_node) {
        this.sm_nodes.add(sm_node);
    }
    public List<sm_Edge> getSm_edges() {
        return sm_edges;
    }

    public void addSm_edge(Sm_edge sm_edge) {
        this.sm_edges.add(sm_edge);
    }
    public List<sm_Mark> getSm_marks() {
        return sm_marks;
    }

    public void addSm_mark(Sm_mark sm_mark) {
        this.sm_marks.add(sm_mark);
    }
    public sm_Node getSm_node() {
        return sm_node;
    }

    public void setSm_node(sm_Node sm_node) {
        this.sm_node = sm_node;
    }

}