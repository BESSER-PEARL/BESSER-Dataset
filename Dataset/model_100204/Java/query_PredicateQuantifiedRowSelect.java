





import java.util.List;
import java.util.ArrayList;

public class query_PredicateQuantifiedRowSelect extends PredicateQuantified {

    private String quantifiedType;





    private query_QueryExpressionRoot query_queryexpressionroot;




    private query_QueryExpressionRoot query_queryexpressionroot;




    private List<query_QueryValueExpression> query_queryvalueexpressions;




    private query_QueryValueExpression query_queryvalueexpression;


    public query_PredicateQuantifiedRowSelect(
        String quantifiedType    ) {
        super(
        );
        this.quantifiedType = quantifiedType;
        this.query_queryvalueexpressions = new ArrayList<>();
    }

    public query_PredicateQuantifiedRowSelect(
        String quantifiedType        ArrayList<query_QueryValueExpression> query_queryvalueexpressions    ) {
        this.quantifiedType = quantifiedType;
        this.query_queryvalueexpressions = query_queryvalueexpressions;
    }

    public String getQuantifiedtype() {
        return quantifiedType;
    }

    public void setQuantifiedtype(String quantifiedType) {
        this.quantifiedType = quantifiedType;
    }

    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
    }
    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
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