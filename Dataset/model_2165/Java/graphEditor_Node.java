





import java.util.List;
import java.util.ArrayList;

public class graphEditor_Node extends GraphElement {

    private String name;





    private graphEditor_Graph grapheditor_graph;


    public graphEditor_Node(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphEditor_Graph getGrapheditor_graph() {
        return grapheditor_graph;
    }

    public void setGrapheditor_graph(graphEditor_Graph grapheditor_graph) {
        this.grapheditor_graph = grapheditor_graph;
    }

}