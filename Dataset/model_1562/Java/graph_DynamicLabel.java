





import java.util.List;
import java.util.ArrayList;

public class graph_DynamicLabel extends Label {

    private boolean nextValueValid;





    private graph_Graph graph_graph;




    private graph_LabelValue graph_labelvalue;




    private graph_Decorator graph_decorator;


    public graph_DynamicLabel(
        boolean nextValueValid    ) {
        super(
        );
        this.nextValueValid = nextValueValid;
    }


    public boolean getNextvaluevalid() {
        return nextValueValid;
    }

    public void setNextvaluevalid(boolean nextValueValid) {
        this.nextValueValid = nextValueValid;
    }

    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }
    public graph_LabelValue getGraph_labelvalue() {
        return graph_labelvalue;
    }

    public void setGraph_labelvalue(graph_LabelValue graph_labelvalue) {
        this.graph_labelvalue = graph_labelvalue;
    }
    public graph_Decorator getGraph_decorator() {
        return graph_decorator;
    }

    public void setGraph_decorator(graph_Decorator graph_decorator) {
        this.graph_decorator = graph_decorator;
    }

}