





import java.util.List;
import java.util.ArrayList;

public class sql_ExprGroup  {






    private sql_FullExpression sql_fullexpression;




    private sql_OrExpr sql_orexpr;


    public sql_ExprGroup(
    ) {
    }



    public sql_FullExpression getSql_fullexpression() {
        return sql_fullexpression;
    }

    public void setSql_fullexpression(sql_FullExpression sql_fullexpression) {
        this.sql_fullexpression = sql_fullexpression;
    }
    public sql_OrExpr getSql_orexpr() {
        return sql_orexpr;
    }

    public void setSql_orexpr(sql_OrExpr sql_orexpr) {
        this.sql_orexpr = sql_orexpr;
    }

}