





import java.util.List;
import java.util.ArrayList;

public class graph_Node  {

    private String name;





    private graph_Node graph_node;




    private List<graph_Node> graph_nodes;




    private graph_Graph graph_graph;


    public graph_Node(
        String name    ) {
        this.name = name;
        this.graph_nodes = new ArrayList<>();
    }

    public graph_Node(
        String name        ArrayList<graph_Node> graph_nodes    ) {
        this.name = name;
        this.graph_nodes = graph_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }
    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }

}