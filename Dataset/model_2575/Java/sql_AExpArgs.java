





import java.util.List;
import java.util.ArrayList;

public class sql_AExpArgs extends AnalyticExprArgs {






    private List<sql_AnalyticExprArg> sql_analyticexprargs;


    public sql_AExpArgs(
    ) {
        super(
        );
        this.sql_analyticexprargs = new ArrayList<>();
    }

    public sql_AExpArgs(
        ArrayList<sql_AnalyticExprArg> sql_analyticexprargs    ) {
        this.sql_analyticexprargs = sql_analyticexprargs;
    }


    public List<sql_AnalyticExprArg> getSql_analyticexprargs() {
        return sql_analyticexprargs;
    }

    public void addSql_analyticexprarg(Sql_analyticexprarg sql_analyticexprarg) {
        this.sql_analyticexprargs.add(sql_analyticexprarg);
    }

}