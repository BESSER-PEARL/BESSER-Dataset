





import java.util.List;
import java.util.ArrayList;

public class sparql_DeleteDataQuery extends ModifyQuery {

    private String graph;



    public sparql_DeleteDataQuery(
        String graph    ) {
        super(
        );
        this.graph = graph;
    }


    public String getGraph() {
        return graph;
    }

    public void setGraph(String graph) {
        this.graph = graph;
    }


}