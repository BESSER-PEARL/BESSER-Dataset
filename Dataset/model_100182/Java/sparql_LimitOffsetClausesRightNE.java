





import java.util.List;
import java.util.ArrayList;

public class sparql_LimitOffsetClausesRightNE extends LimitOffsetClauses {






    private sparql_LimitClause sparql_limitclause;




    private sparql_OffsetClause sparql_offsetclause;


    public sparql_LimitOffsetClausesRightNE(
    ) {
        super(
        );
    }



    public sparql_LimitClause getSparql_limitclause() {
        return sparql_limitclause;
    }

    public void setSparql_limitclause(sparql_LimitClause sparql_limitclause) {
        this.sparql_limitclause = sparql_limitclause;
    }
    public sparql_OffsetClause getSparql_offsetclause() {
        return sparql_offsetclause;
    }

    public void setSparql_offsetclause(sparql_OffsetClause sparql_offsetclause) {
        this.sparql_offsetclause = sparql_offsetclause;
    }

}