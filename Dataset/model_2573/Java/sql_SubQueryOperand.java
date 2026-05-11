





import java.util.List;
import java.util.ArrayList;

public class sql_SubQueryOperand  {






    private sql_TableOrAlias sql_tableoralias;




    private sql_SelectQuery sql_selectquery;




    private sql_PivotInClause sql_pivotinclause;


    public sql_SubQueryOperand(
    ) {
    }



    public sql_TableOrAlias getSql_tableoralias() {
        return sql_tableoralias;
    }

    public void setSql_tableoralias(sql_TableOrAlias sql_tableoralias) {
        this.sql_tableoralias = sql_tableoralias;
    }
    public sql_SelectQuery getSql_selectquery() {
        return sql_selectquery;
    }

    public void setSql_selectquery(sql_SelectQuery sql_selectquery) {
        this.sql_selectquery = sql_selectquery;
    }
    public sql_PivotInClause getSql_pivotinclause() {
        return sql_pivotinclause;
    }

    public void setSql_pivotinclause(sql_PivotInClause sql_pivotinclause) {
        this.sql_pivotinclause = sql_pivotinclause;
    }

}