





import java.util.List;
import java.util.ArrayList;

public class sql_AnalyticClause  {






    private sql_WindowingClause sql_windowingclause;




    private sql_FunctionAnalytical sql_functionanalytical;


    public sql_AnalyticClause(
    ) {
    }



    public sql_WindowingClause getSql_windowingclause() {
        return sql_windowingclause;
    }

    public void setSql_windowingclause(sql_WindowingClause sql_windowingclause) {
        this.sql_windowingclause = sql_windowingclause;
    }
    public sql_FunctionAnalytical getSql_functionanalytical() {
        return sql_functionanalytical;
    }

    public void setSql_functionanalytical(sql_FunctionAnalytical sql_functionanalytical) {
        this.sql_functionanalytical = sql_functionanalytical;
    }

}