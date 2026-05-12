





import java.util.List;
import java.util.ArrayList;

public class sparql_LoadGraphQuery extends UpdateOperation {

    private String intoGraph;
    private String graph;



    public sparql_LoadGraphQuery(
        String intoGraph,        String graph    ) {
        super(
        );
        this.intoGraph = intoGraph;
        this.graph = graph;
    }


    public String getIntograph() {
        return intoGraph;
    }

    public void setIntograph(String intoGraph) {
        this.intoGraph = intoGraph;
    }
    public String getGraph() {
        return graph;
    }

    public void setGraph(String graph) {
        this.graph = graph;
    }


}