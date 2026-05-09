





import java.util.List;
import java.util.ArrayList;

public class graph_Dependency  {

    private String id;
    private String locality;





    private List<graph_Cause> graph_causes;




    private graph_Node graph_node;




    private graph_Node graph_node;




    private graph_Node graph_node;


    public graph_Dependency(
        String id,        String locality    ) {
        this.id = id;
        this.locality = locality;
        this.graph_causes = new ArrayList<>();
    }

    public graph_Dependency(
        String id,        String locality        ArrayList<graph_Cause> graph_causes    ) {
        this.id = id;
        this.locality = locality;
        this.graph_causes = graph_causes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLocality() {
        return locality;
    }

    public void setLocality(String locality) {
        this.locality = locality;
    }

    public List<graph_Cause> getGraph_causes() {
        return graph_causes;
    }

    public void addGraph_cause(Graph_cause graph_cause) {
        this.graph_causes.add(graph_cause);
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }
    public graph_Node getGraph_node() {
        return graph_node;
    }

    public void setGraph_node(graph_Node graph_node) {
        this.graph_node = graph_node;
    }

}