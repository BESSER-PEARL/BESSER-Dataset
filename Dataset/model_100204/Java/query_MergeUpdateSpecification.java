





import java.util.List;
import java.util.ArrayList;

public class query_MergeUpdateSpecification extends MergeOperationSpecification {






    private List<query_UpdateAssignmentExpression> query_updateassignmentexpressions;




    private query_UpdateAssignmentExpression query_updateassignmentexpression;


    public query_MergeUpdateSpecification(
    ) {
        super(
        );
        this.query_updateassignmentexpressions = new ArrayList<>();
    }

    public query_MergeUpdateSpecification(
        ArrayList<query_UpdateAssignmentExpression> query_updateassignmentexpressions    ) {
        this.query_updateassignmentexpressions = query_updateassignmentexpressions;
    }


    public List<query_UpdateAssignmentExpression> getQuery_updateassignmentexpressions() {
        return query_updateassignmentexpressions;
    }

    public void addQuery_updateassignmentexpression(Query_updateassignmentexpression query_updateassignmentexpression) {
        this.query_updateassignmentexpressions.add(query_updateassignmentexpression);
    }
    public query_UpdateAssignmentExpression getQuery_updateassignmentexpression() {
        return query_updateassignmentexpression;
    }

    public void setQuery_updateassignmentexpression(query_UpdateAssignmentExpression query_updateassignmentexpression) {
        this.query_updateassignmentexpression = query_updateassignmentexpression;
    }

}