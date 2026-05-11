





import java.util.List;
import java.util.ArrayList;

public class sql_OrderByClause  {






    private sql_AnalyticClause sql_analyticclause;




    private sql_OrderByClauseArgs sql_orderbyclauseargs;


    public sql_OrderByClause(
    ) {
    }



    public sql_AnalyticClause getSql_analyticclause() {
        return sql_analyticclause;
    }

    public void setSql_analyticclause(sql_AnalyticClause sql_analyticclause) {
        this.sql_analyticclause = sql_analyticclause;
    }
    public sql_OrderByClauseArgs getSql_orderbyclauseargs() {
        return sql_orderbyclauseargs;
    }

    public void setSql_orderbyclauseargs(sql_OrderByClauseArgs sql_orderbyclauseargs) {
        this.sql_orderbyclauseargs = sql_orderbyclauseargs;
    }

}