





import java.util.List;
import java.util.ArrayList;

public class graph2_Graph  {






    private List<graph2_GraphComponent> graph2_graphcomponents;


    public graph2_Graph(
    ) {
        this.graph2_graphcomponents = new ArrayList<>();
    }

    public graph2_Graph(
        ArrayList<graph2_GraphComponent> graph2_graphcomponents    ) {
        this.graph2_graphcomponents = graph2_graphcomponents;
    }


    public List<graph2_GraphComponent> getGraph2_graphcomponents() {
        return graph2_graphcomponents;
    }

    public void addGraph2_graphcomponent(Graph2_graphcomponent graph2_graphcomponent) {
        this.graph2_graphcomponents.add(graph2_graphcomponent);
    }

}