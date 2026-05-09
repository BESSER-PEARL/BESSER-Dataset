





import java.util.List;
import java.util.ArrayList;

public class graph3_Graph  {






    private List<graph3_Node> graph3_nodes;


    public graph3_Graph(
    ) {
        this.graph3_nodes = new ArrayList<>();
    }

    public graph3_Graph(
        ArrayList<graph3_Node> graph3_nodes    ) {
        this.graph3_nodes = graph3_nodes;
    }


    public List<graph3_Node> getGraph3_nodes() {
        return graph3_nodes;
    }

    public void addGraph3_node(Graph3_node graph3_node) {
        this.graph3_nodes.add(graph3_node);
    }

}