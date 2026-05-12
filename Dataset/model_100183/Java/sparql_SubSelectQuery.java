





import java.util.List;
import java.util.ArrayList;

public class sparql_SubSelectQuery extends GroupGraphPattern {






    private sparql_GroupClause sparql_groupclause;




    private sparql_HavingClause sparql_havingclause;




    private List<sparql_Variable> sparql_variables;




    private sparql_WhereClause sparql_whereclause;


    public sparql_SubSelectQuery(
    ) {
        super(
        );
        this.sparql_variables = new ArrayList<>();
    }

    public sparql_SubSelectQuery(
        ArrayList<sparql_Variable> sparql_variables    ) {
        this.sparql_variables = sparql_variables;
    }


    public sparql_GroupClause getSparql_groupclause() {
        return sparql_groupclause;
    }

    public void setSparql_groupclause(sparql_GroupClause sparql_groupclause) {
        this.sparql_groupclause = sparql_groupclause;
    }
    public sparql_HavingClause getSparql_havingclause() {
        return sparql_havingclause;
    }

    public void setSparql_havingclause(sparql_HavingClause sparql_havingclause) {
        this.sparql_havingclause = sparql_havingclause;
    }
    public List<sparql_Variable> getSparql_variables() {
        return sparql_variables;
    }

    public void addSparql_variable(Sparql_variable sparql_variable) {
        this.sparql_variables.add(sparql_variable);
    }
    public sparql_WhereClause getSparql_whereclause() {
        return sparql_whereclause;
    }

    public void setSparql_whereclause(sparql_WhereClause sparql_whereclause) {
        this.sparql_whereclause = sparql_whereclause;
    }

}