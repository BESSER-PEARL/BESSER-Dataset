





import java.util.List;
import java.util.ArrayList;

public class sparql_DropGraphQuery extends UpdateOperation {

    private String graph;
    private String isSilent;



    public sparql_DropGraphQuery(
        String graph,        String isSilent    ) {
        super(
        );
        this.graph = graph;
        this.isSilent = isSilent;
    }


    public String getGraph() {
        return graph;
    }

    public void setGraph(String graph) {
        this.graph = graph;
    }
    public String getIssilent() {
        return isSilent;
    }

    public void setIssilent(String isSilent) {
        this.isSilent = isSilent;
    }


}