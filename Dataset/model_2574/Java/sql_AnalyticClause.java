





import java.util.List;
import java.util.ArrayList;

public class sql_AnalyticClause  {






    private sql_OrderByClause sql_orderbyclause;




    private sql_FunctionAnalytical sql_functionanalytical;




    private sql_QueryPartitionClause sql_querypartitionclause;


    public sql_AnalyticClause(
    ) {
    }



    public sql_OrderByClause getSql_orderbyclause() {
        return sql_orderbyclause;
    }

    public void setSql_orderbyclause(sql_OrderByClause sql_orderbyclause) {
        this.sql_orderbyclause = sql_orderbyclause;
    }
    public sql_FunctionAnalytical getSql_functionanalytical() {
        return sql_functionanalytical;
    }

    public void setSql_functionanalytical(sql_FunctionAnalytical sql_functionanalytical) {
        this.sql_functionanalytical = sql_functionanalytical;
    }
    public sql_QueryPartitionClause getSql_querypartitionclause() {
        return sql_querypartitionclause;
    }

    public void setSql_querypartitionclause(sql_QueryPartitionClause sql_querypartitionclause) {
        this.sql_querypartitionclause = sql_querypartitionclause;
    }

}