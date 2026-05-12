





import java.util.List;
import java.util.ArrayList;

public class query_PredicateInValueList extends PredicateIn {






    private query_QueryValueExpression query_queryvalueexpression;




    private query_QueryValueExpression query_queryvalueexpression;




    private query_QueryValueExpression query_queryvalueexpression;




    private List<query_QueryValueExpression> query_queryvalueexpressions;


    public query_PredicateInValueList(
    ) {
        super(
        );
        this.query_queryvalueexpressions = new ArrayList<>();
    }

    public query_PredicateInValueList(
        ArrayList<query_QueryValueExpression> query_queryvalueexpressions    ) {
        this.query_queryvalueexpressions = query_queryvalueexpressions;
    }


    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public List<query_QueryValueExpression> getQuery_queryvalueexpressions() {
        return query_queryvalueexpressions;
    }

    public void addQuery_queryvalueexpression(Query_queryvalueexpression query_queryvalueexpression) {
        this.query_queryvalueexpressions.add(query_queryvalueexpression);
    }

}