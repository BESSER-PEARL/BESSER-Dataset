





import java.util.List;
import java.util.ArrayList;

public class graph_Node extends Named {

    private String type;
    private String uri;
    private boolean derivedOrNotExists;





    private graph_Graph graph_graph;


    public graph_Node(
        String type,        String uri,        boolean derivedOrNotExists    ) {
        super(
        );
        this.type = type;
        this.uri = uri;
        this.derivedOrNotExists = derivedOrNotExists;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public boolean getDerivedornotexists() {
        return derivedOrNotExists;
    }

    public void setDerivedornotexists(boolean derivedOrNotExists) {
        this.derivedOrNotExists = derivedOrNotExists;
    }

    public graph_Graph getGraph_graph() {
        return graph_graph;
    }

    public void setGraph_graph(graph_Graph graph_graph) {
        this.graph_graph = graph_graph;
    }

}