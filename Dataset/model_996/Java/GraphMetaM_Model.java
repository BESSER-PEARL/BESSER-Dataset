





import java.util.List;
import java.util.ArrayList;

public class GraphMetaM_Model  {

    private String name;





    private List<GraphMetaM_Graph> graphmetam_graphs;


    public GraphMetaM_Model(
        String name    ) {
        this.name = name;
        this.graphmetam_graphs = new ArrayList<>();
    }

    public GraphMetaM_Model(
        String name        ArrayList<GraphMetaM_Graph> graphmetam_graphs    ) {
        this.name = name;
        this.graphmetam_graphs = graphmetam_graphs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<GraphMetaM_Graph> getGraphmetam_graphs() {
        return graphmetam_graphs;
    }

    public void addGraphmetam_graph(Graphmetam_graph graphmetam_graph) {
        this.graphmetam_graphs.add(graphmetam_graph);
    }

}