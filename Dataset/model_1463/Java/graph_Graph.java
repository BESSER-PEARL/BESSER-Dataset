





import java.util.List;
import java.util.ArrayList;

public class graph_Graph  {






    private List<graph_Graph> graph_graphs;


    public graph_Graph(
    ) {
        this.graph_graphs = new ArrayList<>();
    }

    public graph_Graph(
        ArrayList<graph_Graph> graph_graphs    ) {
        this.graph_graphs = graph_graphs;
    }


    public List<graph_Graph> getGraph_graphs() {
        return graph_graphs;
    }

    public void addGraph_graph(Graph_graph graph_graph) {
        this.graph_graphs.add(graph_graph);
    }

}