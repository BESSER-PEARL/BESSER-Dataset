





import java.util.List;
import java.util.ArrayList;

public class sparql_DescribeQuery extends Query {






    private sparql_WhereClause sparql_whereclause;




    private sparql_SolutionModifier sparql_solutionmodifier;




    private List<sparql_DatasetClause> sparql_datasetclauses;


    public sparql_DescribeQuery(
    ) {
        super(
        );
        this.sparql_datasetclauses = new ArrayList<>();
    }

    public sparql_DescribeQuery(
        ArrayList<sparql_DatasetClause> sparql_datasetclauses    ) {
        this.sparql_datasetclauses = sparql_datasetclauses;
    }


    public sparql_WhereClause getSparql_whereclause() {
        return sparql_whereclause;
    }

    public void setSparql_whereclause(sparql_WhereClause sparql_whereclause) {
        this.sparql_whereclause = sparql_whereclause;
    }
    public sparql_SolutionModifier getSparql_solutionmodifier() {
        return sparql_solutionmodifier;
    }

    public void setSparql_solutionmodifier(sparql_SolutionModifier sparql_solutionmodifier) {
        this.sparql_solutionmodifier = sparql_solutionmodifier;
    }
    public List<sparql_DatasetClause> getSparql_datasetclauses() {
        return sparql_datasetclauses;
    }

    public void addSparql_datasetclause(Sparql_datasetclause sparql_datasetclause) {
        this.sparql_datasetclauses.add(sparql_datasetclause);
    }

}