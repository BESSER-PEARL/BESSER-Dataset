





import java.util.List;
import java.util.ArrayList;

public class sparql_AskQuery extends Query {






    private List<sparql_DatasetClause> sparql_datasetclauses;




    private sparql_WhereClause sparql_whereclause;


    public sparql_AskQuery(
    ) {
        super(
        );
        this.sparql_datasetclauses = new ArrayList<>();
    }

    public sparql_AskQuery(
        ArrayList<sparql_DatasetClause> sparql_datasetclauses    ) {
        this.sparql_datasetclauses = sparql_datasetclauses;
    }


    public List<sparql_DatasetClause> getSparql_datasetclauses() {
        return sparql_datasetclauses;
    }

    public void addSparql_datasetclause(Sparql_datasetclause sparql_datasetclause) {
        this.sparql_datasetclauses.add(sparql_datasetclause);
    }
    public sparql_WhereClause getSparql_whereclause() {
        return sparql_whereclause;
    }

    public void setSparql_whereclause(sparql_WhereClause sparql_whereclause) {
        this.sparql_whereclause = sparql_whereclause;
    }

}