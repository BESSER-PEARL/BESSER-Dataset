





import java.util.List;
import java.util.ArrayList;

public class query_QueryExpressionBody extends TableExpression {

    private int rowFetchLimit;





    private query_QueryExpressionRoot query_queryexpressionroot;




    private query_WithTableSpecification query_withtablespecification;




    private query_QueryCombined query_querycombined;




    private query_QueryCombined query_querycombined;




    private query_QueryCombined query_querycombined;




    private query_WithTableSpecification query_withtablespecification;




    private query_QueryExpressionRoot query_queryexpressionroot;




    private query_QueryCombined query_querycombined;




    private List<query_OrderBySpecification> query_orderbyspecifications;




    private query_OrderBySpecification query_orderbyspecification;


    public query_QueryExpressionBody(
        int rowFetchLimit    ) {
        super(
        );
        this.rowFetchLimit = rowFetchLimit;
        this.query_orderbyspecifications = new ArrayList<>();
    }

    public query_QueryExpressionBody(
        int rowFetchLimit        ArrayList<query_OrderBySpecification> query_orderbyspecifications    ) {
        this.rowFetchLimit = rowFetchLimit;
        this.query_orderbyspecifications = query_orderbyspecifications;
    }

    public int getRowfetchlimit() {
        return rowFetchLimit;
    }

    public void setRowfetchlimit(int rowFetchLimit) {
        this.rowFetchLimit = rowFetchLimit;
    }

    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
    }
    public query_WithTableSpecification getQuery_withtablespecification() {
        return query_withtablespecification;
    }

    public void setQuery_withtablespecification(query_WithTableSpecification query_withtablespecification) {
        this.query_withtablespecification = query_withtablespecification;
    }
    public query_QueryCombined getQuery_querycombined() {
        return query_querycombined;
    }

    public void setQuery_querycombined(query_QueryCombined query_querycombined) {
        this.query_querycombined = query_querycombined;
    }
    public query_QueryCombined getQuery_querycombined() {
        return query_querycombined;
    }

    public void setQuery_querycombined(query_QueryCombined query_querycombined) {
        this.query_querycombined = query_querycombined;
    }
    public query_QueryCombined getQuery_querycombined() {
        return query_querycombined;
    }

    public void setQuery_querycombined(query_QueryCombined query_querycombined) {
        this.query_querycombined = query_querycombined;
    }
    public query_WithTableSpecification getQuery_withtablespecification() {
        return query_withtablespecification;
    }

    public void setQuery_withtablespecification(query_WithTableSpecification query_withtablespecification) {
        this.query_withtablespecification = query_withtablespecification;
    }
    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
    }
    public query_QueryCombined getQuery_querycombined() {
        return query_querycombined;
    }

    public void setQuery_querycombined(query_QueryCombined query_querycombined) {
        this.query_querycombined = query_querycombined;
    }
    public List<query_OrderBySpecification> getQuery_orderbyspecifications() {
        return query_orderbyspecifications;
    }

    public void addQuery_orderbyspecification(Query_orderbyspecification query_orderbyspecification) {
        this.query_orderbyspecifications.add(query_orderbyspecification);
    }
    public query_OrderBySpecification getQuery_orderbyspecification() {
        return query_orderbyspecification;
    }

    public void setQuery_orderbyspecification(query_OrderBySpecification query_orderbyspecification) {
        this.query_orderbyspecification = query_orderbyspecification;
    }

}