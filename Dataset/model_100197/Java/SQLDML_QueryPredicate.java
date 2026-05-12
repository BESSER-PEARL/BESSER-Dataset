





import java.util.List;
import java.util.ArrayList;

public class SQLDML_QueryPredicate extends Expression {






    private QueryStmt querystmt;


    public SQLDML_QueryPredicate(
    ) {
        super(
        );
    }



    public QueryStmt getQuerystmt() {
        return querystmt;
    }

    public void setQuerystmt(QueryStmt querystmt) {
        this.querystmt = querystmt;
    }

}