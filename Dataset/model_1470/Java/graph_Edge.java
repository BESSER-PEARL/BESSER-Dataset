





import java.util.List;
import java.util.ArrayList;

public class graph_Edge  {

    private String label;





    private graph_Node graph_node;




    private graph_GraphModel graph_graphmodel;




    private graph_Node graph_node;


    public graph_Edge(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public graph_GraphModel getGraph_graphmodel() {
        return graph_graphmodel;
    }

    public void setGraph_graphmodel(graph_GraphModel graph_graphmodel) {
        this.graph_graphmodel = graph_graphmodel;
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }

}