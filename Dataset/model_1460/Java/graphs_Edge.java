





import java.util.List;
import java.util.ArrayList;

public class graphs_Edge  {

    private int weight;





    private List<graphs_Node> graphs_nodes;




    private graphs_Node graphs_node;




    private graphs_Graph graphs_graph;




    private graphs_Node graphs_node;


    public graphs_Edge(
        int weight    ) {
        this.weight = weight;
        this.graphs_nodes = new ArrayList<>();
    }

    public graphs_Edge(
        int weight        ArrayList<graphs_Node> graphs_nodes    ) {
        this.weight = weight;
        this.graphs_nodes = graphs_nodes;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public List<graphs_Node> getGraphs_nodes() {
        return graphs_nodes;
    }

    public void addGraphs_node(Graphs_node graphs_node) {
        this.graphs_nodes.add(graphs_node);
    }
    public graphs_Node getGraphs_node() {
        return graphs_node;
    }

    public void setGraphs_node(graphs_Node graphs_node) {
        this.graphs_node = graphs_node;
    }
    public graphs_Graph getGraphs_graph() {
        return graphs_graph;
    }

    public void setGraphs_graph(graphs_Graph graphs_graph) {
        this.graphs_graph = graphs_graph;
    }
    public graphs_Node getGraphs_node() {
        return graphs_node;
    }

    public void setGraphs_node(graphs_Node graphs_node) {
        this.graphs_node = graphs_node;
    }

}