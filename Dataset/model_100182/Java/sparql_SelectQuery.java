





import java.util.List;
import java.util.ArrayList;

public class sparql_SelectQuery extends Query {






    private sparql_SolutionsDisplayNE sparql_solutionsdisplayne;




    private sparql_WhereClause sparql_whereclause;




    private List<sparql_DatasetClause> sparql_datasetclauses;




    private sparql_SolutionModifier sparql_solutionmodifier;




    private List<sparql_Var> sparql_vars;


    public sparql_SelectQuery(
    ) {
        super(
        );
        this.sparql_datasetclauses = new ArrayList<>();
        this.sparql_vars = new ArrayList<>();
    }

    public sparql_SelectQuery(
        ArrayList<sparql_DatasetClause> sparql_datasetclauses,        ArrayList<sparql_Var> sparql_vars    ) {
        this.sparql_datasetclauses = sparql_datasetclauses;
        this.sparql_vars = sparql_vars;
    }


    public sparql_SolutionsDisplayNE getSparql_solutionsdisplayne() {
        return sparql_solutionsdisplayne;
    }

    public void setSparql_solutionsdisplayne(sparql_SolutionsDisplayNE sparql_solutionsdisplayne) {
        this.sparql_solutionsdisplayne = sparql_solutionsdisplayne;
    }
    public sparql_WhereClause getSparql_whereclause() {
        return sparql_whereclause;
    }

    public void setSparql_whereclause(sparql_WhereClause sparql_whereclause) {
        this.sparql_whereclause = sparql_whereclause;
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
    public List<sparql_Var> getSparql_vars() {
        return sparql_vars;
    }

    public void addSparql_var(Sparql_var sparql_var) {
        this.sparql_vars.add(sparql_var);
    }

}