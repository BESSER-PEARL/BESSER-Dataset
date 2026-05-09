





import java.util.List;
import java.util.ArrayList;

public class Graph_Graph  {






    private List<Graph_Node> graph_nodes;


    public Graph_Graph(
    ) {
        this.graph_nodes = new ArrayList<>();
    }

    public Graph_Graph(
        ArrayList<Graph_Node> graph_nodes    ) {
        this.graph_nodes = graph_nodes;
    }


    public List<Graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }

}