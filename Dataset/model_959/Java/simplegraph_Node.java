





import java.util.List;
import java.util.ArrayList;

public class simplegraph_Node  {

    private String name;





    private simplegraph_Edge simplegraph_edge;




    private List<simplegraph_Edge> simplegraph_edges;




    private simplegraph_Edge simplegraph_edge;




    private simplegraph_Graph simplegraph_graph;




    private List<simplegraph_Edge> simplegraph_edges;


    public simplegraph_Node(
        String name    ) {
        this.name = name;
        this.simplegraph_edges = new ArrayList<>();
        this.simplegraph_edges = new ArrayList<>();
    }

    public simplegraph_Node(
        String name        ArrayList<simplegraph_Edge> simplegraph_edges,        ArrayList<simplegraph_Edge> simplegraph_edges    ) {
        this.name = name;
        this.simplegraph_edges = simplegraph_edges;
        this.simplegraph_edges = simplegraph_edges;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplegraph_Edge getSimplegraph_edge() {
        return simplegraph_edge;
    }

    public void setSimplegraph_edge(simplegraph_Edge simplegraph_edge) {
        this.simplegraph_edge = simplegraph_edge;
    }
    public List<simplegraph_Edge> getSimplegraph_edges() {
        return simplegraph_edges;
    }

    public void addSimplegraph_edge(Simplegraph_edge simplegraph_edge) {
        this.simplegraph_edges.add(simplegraph_edge);
    }
    public simplegraph_Edge getSimplegraph_edge() {
        return simplegraph_edge;
    }

    public void setSimplegraph_edge(simplegraph_Edge simplegraph_edge) {
        this.simplegraph_edge = simplegraph_edge;
    }
    public simplegraph_Graph getSimplegraph_graph() {
        return simplegraph_graph;
    }

    public void setSimplegraph_graph(simplegraph_Graph simplegraph_graph) {
        this.simplegraph_graph = simplegraph_graph;
    }
    public List<simplegraph_Edge> getSimplegraph_edges() {
        return simplegraph_edges;
    }

    public void addSimplegraph_edge(Simplegraph_edge simplegraph_edge) {
        this.simplegraph_edges.add(simplegraph_edge);
    }

}