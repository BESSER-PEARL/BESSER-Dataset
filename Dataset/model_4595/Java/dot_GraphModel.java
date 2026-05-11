





import java.util.List;
import java.util.ArrayList;

public class dot_GraphModel  {






    private List<dot_Graph> dot_graphs;


    public dot_GraphModel(
    ) {
        this.dot_graphs = new ArrayList<>();
    }

    public dot_GraphModel(
        ArrayList<dot_Graph> dot_graphs    ) {
        this.dot_graphs = dot_graphs;
    }


    public List<dot_Graph> getDot_graphs() {
        return dot_graphs;
    }

    public void addDot_graph(Dot_graph dot_graph) {
        this.dot_graphs.add(dot_graph);
    }

}