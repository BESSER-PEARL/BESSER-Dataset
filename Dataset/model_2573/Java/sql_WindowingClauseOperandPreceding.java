





import java.util.List;
import java.util.ArrayList;

public class sql_WindowingClauseOperandPreceding extends WindowingClause {






    private sql_WindowingClauseBetween sql_windowingclausebetween;




    private sql_AnalyticExprArg sql_analyticexprarg;


    public sql_WindowingClauseOperandPreceding(
    ) {
        super(
        );
    }



    public sql_WindowingClauseBetween getSql_windowingclausebetween() {
        return sql_windowingclausebetween;
    }

    public void setSql_windowingclausebetween(sql_WindowingClauseBetween sql_windowingclausebetween) {
        this.sql_windowingclausebetween = sql_windowingclausebetween;
    }
    public sql_AnalyticExprArg getSql_analyticexprarg() {
        return sql_analyticexprarg;
    }

    public void setSql_analyticexprarg(sql_AnalyticExprArg sql_analyticexprarg) {
        this.sql_analyticexprarg = sql_analyticexprarg;
    }

}