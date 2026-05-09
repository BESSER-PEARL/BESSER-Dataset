





import java.util.List;
import java.util.ArrayList;

public class graph3_Node  {

    private String text;





    private graph3_Node graph3_node;




    private graph3_Graph graph3_graph;


    public graph3_Node(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public graph3_Node getGraph3_node() {
        return graph3_node;
    }

    public void setGraph3_node(graph3_Node graph3_node) {
        this.graph3_node = graph3_node;
    }
    public graph3_Graph getGraph3_graph() {
        return graph3_graph;
    }

    public void setGraph3_graph(graph3_Graph graph3_graph) {
        this.graph3_graph = graph3_graph;
    }

}