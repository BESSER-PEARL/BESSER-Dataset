





import java.util.List;
import java.util.ArrayList;

public class graph_Graph  {






    private List<graph_Subgraphs> graph_subgraphss;


    public graph_Graph(
    ) {
        this.graph_subgraphss = new ArrayList<>();
    }

    public graph_Graph(
        ArrayList<graph_Subgraphs> graph_subgraphss    ) {
        this.graph_subgraphss = graph_subgraphss;
    }


    public List<graph_Subgraphs> getGraph_subgraphss() {
        return graph_subgraphss;
    }

    public void addGraph_subgraphs(Graph_subgraphs graph_subgraphs) {
        this.graph_subgraphss.add(graph_subgraphs);
    }

}