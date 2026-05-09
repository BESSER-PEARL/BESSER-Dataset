





import java.util.List;
import java.util.ArrayList;

public class graph_Node extends Identifiable {






    private graph_Edge graph_edge;




    private List<graph_Edge> graph_edges;




    private graph_Edge graph_edge;


    public graph_Node(
    ) {
        super(
        );
        this.graph_edges = new ArrayList<>();
    }

    public graph_Node(
        ArrayList<graph_Edge> graph_edges    ) {
        this.graph_edges = graph_edges;
    }


    public graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }
    public List<graph_Edge> getGraph_edges() {
        return graph_edges;
    }

    public void addGraph_edge(Graph_edge graph_edge) {
        this.graph_edges.add(graph_edge);
    }
    public graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }

}