





import java.util.List;
import java.util.ArrayList;

public class graph_Node  {

    private String id;





    private List<graph_Node> graph_nodes;




    private List<graph_Node> graph_nodes;


    public graph_Node(
        String id    ) {
        this.id = id;
        this.graph_nodes = new ArrayList<>();
        this.graph_nodes = new ArrayList<>();
    }

    public graph_Node(
        String id        ArrayList<graph_Node> graph_nodes,        ArrayList<graph_Node> graph_nodes    ) {
        this.id = id;
        this.graph_nodes = graph_nodes;
        this.graph_nodes = graph_nodes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }
    public List<graph_Node> getGraph_nodes() {
        return graph_nodes;
    }

    public void addGraph_node(Graph_node graph_node) {
        this.graph_nodes.add(graph_node);
    }

}