





import java.util.List;
import java.util.ArrayList;

public class query_ValueExpressionColumn extends ValueExpressionAtomic {






    private query_UpdateAssignmentExpression query_updateassignmentexpression;




    private query_TableInDatabase query_tableindatabase;




    private query_QueryInsertStatement query_queryinsertstatement;




    private List<query_UpdateAssignmentExpression> query_updateassignmentexpressions;




    private List<query_QueryInsertStatement> query_queryinsertstatements;




    private query_TableInDatabase query_tableindatabase;


    public query_ValueExpressionColumn(
    ) {
        super(
        );
        this.query_updateassignmentexpressions = new ArrayList<>();
        this.query_queryinsertstatements = new ArrayList<>();
    }

    public query_ValueExpressionColumn(
        ArrayList<query_UpdateAssignmentExpression> query_updateassignmentexpressions,        ArrayList<query_QueryInsertStatement> query_queryinsertstatements    ) {
        this.query_updateassignmentexpressions = query_updateassignmentexpressions;
        this.query_queryinsertstatements = query_queryinsertstatements;
    }


    public query_UpdateAssignmentExpression getQuery_updateassignmentexpression() {
        return query_updateassignmentexpression;
    }

    public void setQuery_updateassignmentexpression(query_UpdateAssignmentExpression query_updateassignmentexpression) {
        this.query_updateassignmentexpression = query_updateassignmentexpression;
    }
    public query_TableInDatabase getQuery_tableindatabase() {
        return query_tableindatabase;
    }

    public void setQuery_tableindatabase(query_TableInDatabase query_tableindatabase) {
        this.query_tableindatabase = query_tableindatabase;
    }
    public query_QueryInsertStatement getQuery_queryinsertstatement() {
        return query_queryinsertstatement;
    }

    public void setQuery_queryinsertstatement(query_QueryInsertStatement query_queryinsertstatement) {
        this.query_queryinsertstatement = query_queryinsertstatement;
    }
    public List<query_UpdateAssignmentExpression> getQuery_updateassignmentexpressions() {
        return query_updateassignmentexpressions;
    }

    public void addQuery_updateassignmentexpression(Query_updateassignmentexpression query_updateassignmentexpression) {
        this.query_updateassignmentexpressions.add(query_updateassignmentexpression);
    }
    public List<query_QueryInsertStatement> getQuery_queryinsertstatements() {
        return query_queryinsertstatements;
    }

    public void addQuery_queryinsertstatement(Query_queryinsertstatement query_queryinsertstatement) {
        this.query_queryinsertstatements.add(query_queryinsertstatement);
    }
    public query_TableInDatabase getQuery_tableindatabase() {
        return query_tableindatabase;
    }

    public void setQuery_tableindatabase(query_TableInDatabase query_tableindatabase) {
        this.query_tableindatabase = query_tableindatabase;
    }

}