





import java.util.List;
import java.util.ArrayList;

public class sql_OrderByClauseArg extends OrderByClauseArgs {






    private sql_OBCArgs sql_obcargs;




    private sql_AnalyticExprArg sql_analyticexprarg;


    public sql_OrderByClauseArg(
    ) {
        super(
        );
    }



    public sql_OBCArgs getSql_obcargs() {
        return sql_obcargs;
    }

    public void setSql_obcargs(sql_OBCArgs sql_obcargs) {
        this.sql_obcargs = sql_obcargs;
    }
    public sql_AnalyticExprArg getSql_analyticexprarg() {
        return sql_analyticexprarg;
    }

    public void setSql_analyticexprarg(sql_AnalyticExprArg sql_analyticexprarg) {
        this.sql_analyticexprarg = sql_analyticexprarg;
    }

}