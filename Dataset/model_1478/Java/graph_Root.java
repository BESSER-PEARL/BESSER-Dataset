





import java.util.List;
import java.util.ArrayList;

public class graph_Root  {






    private List<graph_Node> graph_nodes;




    private List<graph_Edge> graph_edges;


    public graph_Root(
    ) {
        this.graph_nodes = new ArrayList<>();
        this.graph_edges = new ArrayList<>();
    }

    public graph_Root(
        ArrayList<graph_Node> graph_nodes,        ArrayList<graph_Edge> graph_edges    ) {
        this.graph_nodes = graph_nodes;
        this.graph_edges = graph_edges;
    }


    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }
    public List<graph_Edge> getGraph_edges() {
        return graph_edges;
    }

    public void addGraph_edge(Graph_edge graph_edge) {
        this.graph_edges.add(graph_edge);
    }

}