





import java.util.List;
import java.util.ArrayList;

public class graph2_GraphComponent  {

    private String text;





    private graph2_Graph graph2_graph;


    public graph2_GraphComponent(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public graph2_Graph getGraph2_graph() {
        return graph2_graph;
    }

    public void setGraph2_graph(graph2_Graph graph2_graph) {
        this.graph2_graph = graph2_graph;
    }

}