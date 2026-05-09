





import java.util.List;
import java.util.ArrayList;

public class graphmodel_Node extends Entity {






    private graphmodel_Edge graphmodel_edge;




    private graphmodel_Edge graphmodel_edge;




    private List<graphmodel_Node> graphmodel_nodes;




    private graphmodel_Node graphmodel_node;




    private graphmodel_Graph graphmodel_graph;


    public graphmodel_Node(
    ) {
        super(
        );
        this.graphmodel_nodes = new ArrayList<>();
    }

    public graphmodel_Node(
        ArrayList<graphmodel_Node> graphmodel_nodes    ) {
        this.graphmodel_nodes = graphmodel_nodes;
    }


    public graphmodel_Edge getGraphmodel_edge() {
        return graphmodel_edge;
    }

    public void setGraphmodel_edge(graphmodel_Edge graphmodel_edge) {
        this.graphmodel_edge = graphmodel_edge;
    }
    public graphmodel_Edge getGraphmodel_edge() {
        return graphmodel_edge;
    }

    public void setGraphmodel_edge(graphmodel_Edge graphmodel_edge) {
        this.graphmodel_edge = graphmodel_edge;
    }
    public List<graphmodel_Node> getGraphmodel_nodes() {
        return graphmodel_nodes;
    }

    public void addGraphmodel_node(Graphmodel_node graphmodel_node) {
        this.graphmodel_nodes.add(graphmodel_node);
    }
    public graphmodel_Node getGraphmodel_node() {
        return graphmodel_node;
    }

    public void setGraphmodel_node(graphmodel_Node graphmodel_node) {
        this.graphmodel_node = graphmodel_node;
    }
    public graphmodel_Graph getGraphmodel_graph() {
        return graphmodel_graph;
    }

    public void setGraphmodel_graph(graphmodel_Graph graphmodel_graph) {
        this.graphmodel_graph = graphmodel_graph;
    }

}