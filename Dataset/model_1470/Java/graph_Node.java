





import java.util.List;
import java.util.ArrayList;

public class graph_Node  {

    private String value;





    private graph_GraphModel graph_graphmodel;


    public graph_Node(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public graph_GraphModel getGraph_graphmodel() {
        return graph_graphmodel;
    }

    public void setGraph_graphmodel(graph_GraphModel graph_graphmodel) {
        this.graph_graphmodel = graph_graphmodel;
    }

}