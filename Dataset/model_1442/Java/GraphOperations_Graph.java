





import java.util.List;
import java.util.ArrayList;

public class GraphOperations_Graph  {






    private List<GraphOperations_Node> graphoperations_nodes;




    private GraphOperations_Node graphoperations_node;


    public GraphOperations_Graph(
    ) {
        this.graphoperations_nodes = new ArrayList<>();
    }

    public GraphOperations_Graph(
        ArrayList<GraphOperations_Node> graphoperations_nodes    ) {
        this.graphoperations_nodes = graphoperations_nodes;
    }


    public List<GraphOperations_Node> getGraphoperations_nodes() {
        return graphoperations_nodes;
    }

    public void addGraphoperations_node(Graphoperations_node graphoperations_node) {
        this.graphoperations_nodes.add(graphoperations_node);
    }
    public GraphOperations_Node getGraphoperations_node() {
        return graphoperations_node;
    }

    public void setGraphoperations_node(GraphOperations_Node graphoperations_node) {
        this.graphoperations_node = graphoperations_node;
    }

}