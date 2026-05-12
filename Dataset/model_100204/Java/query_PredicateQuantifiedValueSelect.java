





import java.util.List;
import java.util.ArrayList;

public class query_PredicateQuantifiedValueSelect extends PredicateQuantified {

    private String comparisonOperator;
    private String quantifiedType;





    private query_QueryValueExpression query_queryvalueexpression;




    private query_QueryExpressionRoot query_queryexpressionroot;




    private query_QueryValueExpression query_queryvalueexpression;




    private query_QueryExpressionRoot query_queryexpressionroot;


    public query_PredicateQuantifiedValueSelect(
        String comparisonOperator,        String quantifiedType    ) {
        super(
        );
        this.comparisonOperator = comparisonOperator;
        this.quantifiedType = quantifiedType;
    }


    public String getComparisonoperator() {
        return comparisonOperator;
    }

    public void setComparisonoperator(String comparisonOperator) {
        this.comparisonOperator = comparisonOperator;
    }
    public String getQuantifiedtype() {
        return quantifiedType;
    }

    public void setQuantifiedtype(String quantifiedType) {
        this.quantifiedType = quantifiedType;
    }

    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
    }
    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
    }

}