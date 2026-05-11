





import java.util.List;
import java.util.ArrayList;

public class sql_PivotTable  {






    private sql_PivotInClause sql_pivotinclause;




    private sql_TableOrAlias sql_tableoralias;




    private sql_PivotForClause sql_pivotforclause;




    private sql_PivotFunctions sql_pivotfunctions;


    public sql_PivotTable(
    ) {
    }



    public sql_PivotInClause getSql_pivotinclause() {
        return sql_pivotinclause;
    }

    public void setSql_pivotinclause(sql_PivotInClause sql_pivotinclause) {
        this.sql_pivotinclause = sql_pivotinclause;
    }
    public sql_TableOrAlias getSql_tableoralias() {
        return sql_tableoralias;
    }

    public void setSql_tableoralias(sql_TableOrAlias sql_tableoralias) {
        this.sql_tableoralias = sql_tableoralias;
    }
    public sql_PivotForClause getSql_pivotforclause() {
        return sql_pivotforclause;
    }

    public void setSql_pivotforclause(sql_PivotForClause sql_pivotforclause) {
        this.sql_pivotforclause = sql_pivotforclause;
    }
    public sql_PivotFunctions getSql_pivotfunctions() {
        return sql_pivotfunctions;
    }

    public void setSql_pivotfunctions(sql_PivotFunctions sql_pivotfunctions) {
        this.sql_pivotfunctions = sql_pivotfunctions;
    }

}