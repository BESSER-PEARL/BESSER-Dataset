





import java.util.List;
import java.util.ArrayList;

public class query_GroupingSetsElementSublist extends GroupingSetsElement {






    private query_GroupingSetsElementExpression query_groupingsetselementexpression;




    private List<query_GroupingSetsElementExpression> query_groupingsetselementexpressions;


    public query_GroupingSetsElementSublist(
    ) {
        super(
        );
        this.query_groupingsetselementexpressions = new ArrayList<>();
    }

    public query_GroupingSetsElementSublist(
        ArrayList<query_GroupingSetsElementExpression> query_groupingsetselementexpressions    ) {
        this.query_groupingsetselementexpressions = query_groupingsetselementexpressions;
    }


    public query_GroupingSetsElementExpression getQuery_groupingsetselementexpression() {
        return query_groupingsetselementexpression;
    }

    public void setQuery_groupingsetselementexpression(query_GroupingSetsElementExpression query_groupingsetselementexpression) {
        this.query_groupingsetselementexpression = query_groupingsetselementexpression;
    }
    public List<query_GroupingSetsElementExpression> getQuery_groupingsetselementexpressions() {
        return query_groupingsetselementexpressions;
    }

    public void addQuery_groupingsetselementexpression(Query_groupingsetselementexpression query_groupingsetselementexpression) {
        this.query_groupingsetselementexpressions.add(query_groupingsetselementexpression);
    }

}