





import java.util.List;
import java.util.ArrayList;

public class sparql_ConstructQuery extends Query {






    private List<sparql_DatasetClause> sparql_datasetclauses;




    private sparql_SolutionModifier sparql_solutionmodifier;




    private sparql_ConstructTemplate sparql_constructtemplate;




    private sparql_WhereClause sparql_whereclause;


    public sparql_ConstructQuery(
    ) {
        super(
        );
        this.sparql_datasetclauses = new ArrayList<>();
    }

    public sparql_ConstructQuery(
        ArrayList<sparql_DatasetClause> sparql_datasetclauses    ) {
        this.sparql_datasetclauses = sparql_datasetclauses;
    }


    public List<sparql_DatasetClause> getSparql_datasetclauses() {
        return sparql_datasetclauses;
    }

    public void addSparql_datasetclause(Sparql_datasetclause sparql_datasetclause) {
        this.sparql_datasetclauses.add(sparql_datasetclause);
    }
    public sparql_SolutionModifier getSparql_solutionmodifier() {
        return sparql_solutionmodifier;
    }

    public void setSparql_solutionmodifier(sparql_SolutionModifier sparql_solutionmodifier) {
        this.sparql_solutionmodifier = sparql_solutionmodifier;
    }
    public sparql_ConstructTemplate getSparql_constructtemplate() {
        return sparql_constructtemplate;
    }

    public void setSparql_constructtemplate(sparql_ConstructTemplate sparql_constructtemplate) {
        this.sparql_constructtemplate = sparql_constructtemplate;
    }
    public sparql_WhereClause getSparql_whereclause() {
        return sparql_whereclause;
    }

    public void setSparql_whereclause(sparql_WhereClause sparql_whereclause) {
        this.sparql_whereclause = sparql_whereclause;
    }

}