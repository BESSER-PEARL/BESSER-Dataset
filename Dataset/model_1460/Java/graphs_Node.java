





import java.util.List;
import java.util.ArrayList;

public class graphs_Node  {

    private String name;





    private graphs_Graph graphs_graph;


    public graphs_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphs_Graph getGraphs_graph() {
        return graphs_graph;
    }

    public void setGraphs_graph(graphs_Graph graphs_graph) {
        this.graphs_graph = graphs_graph;
    }

}