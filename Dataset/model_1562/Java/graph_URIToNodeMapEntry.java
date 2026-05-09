





import java.util.List;
import java.util.ArrayList;

public class graph_URIToNodeMapEntry  {

    private String key;





    private graph_Graph graph_graph;




    private graph_Node graph_node;


    public graph_URIToNodeMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }

}