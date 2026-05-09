





import java.util.List;
import java.util.ArrayList;

public class graph_URIToEdgeMapEntry  {

    private String key;





    private graph_Graph graph_graph;




    private graph_Edge graph_edge;


    public graph_URIToEdgeMapEntry(
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
    public graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }

}