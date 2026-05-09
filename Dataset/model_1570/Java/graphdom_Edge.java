





import java.util.List;
import java.util.ArrayList;

public class graphdom_Edge  {

    private boolean marked;
    private String guid;
    private int weight;





    private List<graphdom_Node> graphdom_nodes;




    private graphdom_Node graphdom_node;




    private graphdom_Graph graphdom_graph;


    public graphdom_Edge(
        boolean marked,        String guid,        int weight    ) {
        this.marked = marked;
        this.guid = guid;
        this.weight = weight;
        this.graphdom_nodes = new ArrayList<>();
    }

    public graphdom_Edge(
        boolean marked,        String guid,        int weight        ArrayList<graphdom_Node> graphdom_nodes    ) {
        this.marked = marked;
        this.guid = guid;
        this.weight = weight;
        this.graphdom_nodes = graphdom_nodes;
    }

    public boolean getMarked() {
        return marked;
    }

    public void setMarked(boolean marked) {
        this.marked = marked;
    }
    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public List<graphdom_Node> getGraphdom_nodes() {
        return graphdom_nodes;
    }

    public void addGraphdom_node(Graphdom_node graphdom_node) {
        this.graphdom_nodes.add(graphdom_node);
    }
    public graphdom_Node getGraphdom_node() {
        return graphdom_node;
    }

    public void setGraphdom_node(graphdom_Node graphdom_node) {
        this.graphdom_node = graphdom_node;
    }
    public graphdom_Graph getGraphdom_graph() {
        return graphdom_graph;
    }

    public void setGraphdom_graph(graphdom_Graph graphdom_graph) {
        this.graphdom_graph = graphdom_graph;
    }

}