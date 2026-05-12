





import java.util.List;
import java.util.ArrayList;

public class query_UpdateSourceExprList extends UpdateSource {






    private List<query_QueryValueExpression> query_queryvalueexpressions;




    private query_QueryValueExpression query_queryvalueexpression;


    public query_UpdateSourceExprList(
    ) {
        super(
        );
        this.query_queryvalueexpressions = new ArrayList<>();
    }

    public query_UpdateSourceExprList(
        ArrayList<query_QueryValueExpression> query_queryvalueexpressions    ) {
        this.query_queryvalueexpressions = query_queryvalueexpressions;
    }


    public List<query_QueryValueExpression> getQuery_queryvalueexpressions() {
        return query_queryvalueexpressions;
    }

    public void addQuery_queryvalueexpression(Query_queryvalueexpression query_queryvalueexpression) {
        this.query_queryvalueexpressions.add(query_queryvalueexpression);
    }
    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }

}