





import java.util.List;
import java.util.ArrayList;

public class sparql_ModifyQuery extends UpdateOperation {

    private String withGraph;





    private sparql_GroupGraphPattern sparql_groupgraphpattern;


    public sparql_ModifyQuery(
        String withGraph    ) {
        super(
        );
        this.withGraph = withGraph;
    }


    public String getWithgraph() {
        return withGraph;
    }

    public void setWithgraph(String withGraph) {
        this.withGraph = withGraph;
    }

    public sparql_GroupGraphPattern getSparql_groupgraphpattern() {
        return sparql_groupgraphpattern;
    }

    public void setSparql_groupgraphpattern(sparql_GroupGraphPattern sparql_groupgraphpattern) {
        this.sparql_groupgraphpattern = sparql_groupgraphpattern;
    }

}