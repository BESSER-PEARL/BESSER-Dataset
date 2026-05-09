





import java.util.List;
import java.util.ArrayList;

public class graph_Edge extends Named {

    private boolean exact;
    private String pathDiscoveredByHeuristic;





    private graph_Node graph_node;




    private graph_Node graph_node;




    private graph_Node graph_node;




    private graph_Graph graph_graph;


    public graph_Edge(
        boolean exact,        String pathDiscoveredByHeuristic    ) {
        super(
        );
        this.exact = exact;
        this.pathDiscoveredByHeuristic = pathDiscoveredByHeuristic;
    }


    public boolean getExact() {
        return exact;
    }

    public void setExact(boolean exact) {
        this.exact = exact;
    }
    public String getPathdiscoveredbyheuristic() {
        return pathDiscoveredByHeuristic;
    }

    public void setPathdiscoveredbyheuristic(String pathDiscoveredByHeuristic) {
        this.pathDiscoveredByHeuristic = pathDiscoveredByHeuristic;
    }

    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }

}