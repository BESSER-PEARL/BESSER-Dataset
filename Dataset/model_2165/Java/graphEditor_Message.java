





import java.util.List;
import java.util.ArrayList;

public class graphEditor_Message extends GraphElement {

    private String type;
    private int count;





    private graphEditor_Graph grapheditor_graph;




    private graphEditor_Node grapheditor_node;




    private graphEditor_Node grapheditor_node;


    public graphEditor_Message(
        String type,        int count    ) {
        super(
        );
        this.type = type;
        this.count = count;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public graphEditor_Graph getGrapheditor_graph() {
        return grapheditor_graph;
    }

    public void setGrapheditor_graph(graphEditor_Graph grapheditor_graph) {
        this.grapheditor_graph = grapheditor_graph;
    }
    public graphEditor_Node getGrapheditor_node() {
        return grapheditor_node;
    }

    public void setGrapheditor_node(graphEditor_Node grapheditor_node) {
        this.grapheditor_node = grapheditor_node;
    }
    public graphEditor_Node getGrapheditor_node() {
        return grapheditor_node;
    }

    public void setGrapheditor_node(graphEditor_Node grapheditor_node) {
        this.grapheditor_node = grapheditor_node;
    }

}