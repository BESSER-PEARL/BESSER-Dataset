





import java.util.List;
import java.util.ArrayList;

public class sparql_InsertQuery extends ModifyQuery {

    private String graph;





    private sparql_WhereClause sparql_whereclause;


    public sparql_InsertQuery(
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

    public sparql_WhereClause getSparql_whereclause() {
        return sparql_whereclause;
    }

    public void setSparql_whereclause(sparql_WhereClause sparql_whereclause) {
        this.sparql_whereclause = sparql_whereclause;
    }

}