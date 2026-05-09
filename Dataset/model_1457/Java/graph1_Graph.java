





import java.util.List;
import java.util.ArrayList;

public class graph1_Graph  {






    private List<graph1_Edge> graph1_edges;




    private List<graph1_Node> graph1_nodes;


    public graph1_Graph(
    ) {
        this.graph1_edges = new ArrayList<>();
        this.graph1_nodes = new ArrayList<>();
    }

    public graph1_Graph(
        ArrayList<graph1_Edge> graph1_edges,        ArrayList<graph1_Node> graph1_nodes    ) {
        this.graph1_edges = graph1_edges;
        this.graph1_nodes = graph1_nodes;
    }


    public List<graph1_Edge> getGraph1_edges() {
        return graph1_edges;
    }

    public void addGraph1_edge(Graph1_edge graph1_edge) {
        this.graph1_edges.add(graph1_edge);
    }
    public List<graph1_Node> getGraph1_nodes() {
        return graph1_nodes;
    }

    public void addGraph1_node(Graph1_node graph1_node) {
        this.graph1_nodes.add(graph1_node);
    }

}