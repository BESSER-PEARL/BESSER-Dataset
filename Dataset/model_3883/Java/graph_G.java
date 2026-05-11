





import java.util.List;
import java.util.ArrayList;

public class graph_G  {






    private List<graph_Node> graph_nodes;


    public graph_G(
    ) {
        this.graph_nodes = new ArrayList<>();
    }

    public graph_G(
        ArrayList<graph_Node> graph_nodes    ) {
        this.graph_nodes = graph_nodes;
    }


    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }

}