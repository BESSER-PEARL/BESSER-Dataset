





import java.util.List;
import java.util.ArrayList;

public class graph_Vertice  {

    private String label;





    private graph_Graph graph_graph;


    public graph_Vertice(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }

}