





import java.util.List;
import java.util.ArrayList;

public class sql_UnpivotTable  {






    private sql_UnpivotInClause sql_unpivotinclause;




    private sql_PivotForClause sql_pivotforclause;




    private sql_TableOrAlias sql_tableoralias;




    private sql_PivotColumns sql_pivotcolumns;


    public sql_UnpivotTable(
    ) {
    }



    public sql_UnpivotInClause getSql_unpivotinclause() {
        return sql_unpivotinclause;
    }

    public void setSql_unpivotinclause(sql_UnpivotInClause sql_unpivotinclause) {
        this.sql_unpivotinclause = sql_unpivotinclause;
    }
    public sql_PivotForClause getSql_pivotforclause() {
        return sql_pivotforclause;
    }

    public void setSql_pivotforclause(sql_PivotForClause sql_pivotforclause) {
        this.sql_pivotforclause = sql_pivotforclause;
    }
    public sql_TableOrAlias getSql_tableoralias() {
        return sql_tableoralias;
    }

    public void setSql_tableoralias(sql_TableOrAlias sql_tableoralias) {
        this.sql_tableoralias = sql_tableoralias;
    }
    public sql_PivotColumns getSql_pivotcolumns() {
        return sql_pivotcolumns;
    }

    public void setSql_pivotcolumns(sql_PivotColumns sql_pivotcolumns) {
        this.sql_pivotcolumns = sql_pivotcolumns;
    }

}