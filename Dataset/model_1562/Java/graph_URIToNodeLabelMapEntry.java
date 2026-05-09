





import java.util.List;
import java.util.ArrayList;

public class graph_URIToNodeLabelMapEntry  {

    private String key;





    private graph_Graph graph_graph;




    private graph_NodeLabel graph_nodelabel;


    public graph_URIToNodeLabelMapEntry(
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
    public graph_NodeLabel getGraph_nodelabel() {
        return graph_nodelabel;
    }

    public void setGraph_nodelabel(graph_NodeLabel graph_nodelabel) {
        this.graph_nodelabel = graph_nodelabel;
    }

}