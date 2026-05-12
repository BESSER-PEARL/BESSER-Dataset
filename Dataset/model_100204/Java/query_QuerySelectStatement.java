





import java.util.List;
import java.util.ArrayList;

public class query_QuerySelectStatement extends QueryStatement {






    private query_QueryExpressionRoot query_queryexpressionroot;




    private query_UpdatabilityExpression query_updatabilityexpression;




    private query_UpdatabilityExpression query_updatabilityexpression;




    private query_QueryExpressionRoot query_queryexpressionroot;




    private List<query_OrderBySpecification> query_orderbyspecifications;




    private query_OrderBySpecification query_orderbyspecification;


    public query_QuerySelectStatement(
    ) {
        super(
        );
        this.query_orderbyspecifications = new ArrayList<>();
    }

    public query_QuerySelectStatement(
        ArrayList<query_OrderBySpecification> query_orderbyspecifications    ) {
        this.query_orderbyspecifications = query_orderbyspecifications;
    }


    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
    }
    public query_UpdatabilityExpression getQuery_updatabilityexpression() {
        return query_updatabilityexpression;
    }

    public void setQuery_updatabilityexpression(query_UpdatabilityExpression query_updatabilityexpression) {
        this.query_updatabilityexpression = query_updatabilityexpression;
    }
    public query_UpdatabilityExpression getQuery_updatabilityexpression() {
        return query_updatabilityexpression;
    }

    public void setQuery_updatabilityexpression(query_UpdatabilityExpression query_updatabilityexpression) {
        this.query_updatabilityexpression = query_updatabilityexpression;
    }
    public query_QueryExpressionRoot getQuery_queryexpressionroot() {
        return query_queryexpressionroot;
    }

    public void setQuery_queryexpressionroot(query_QueryExpressionRoot query_queryexpressionroot) {
        this.query_queryexpressionroot = query_queryexpressionroot;
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