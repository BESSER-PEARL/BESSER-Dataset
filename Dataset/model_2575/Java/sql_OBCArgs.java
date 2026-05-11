





import java.util.List;
import java.util.ArrayList;

public class sql_OBCArgs extends OrderByClauseArgs {






    private List<sql_OrderByClauseArg> sql_orderbyclauseargs;


    public sql_OBCArgs(
    ) {
        super(
        );
        this.sql_orderbyclauseargs = new ArrayList<>();
    }

    public sql_OBCArgs(
        ArrayList<sql_OrderByClauseArg> sql_orderbyclauseargs    ) {
        this.sql_orderbyclauseargs = sql_orderbyclauseargs;
    }


    public List<sql_OrderByClauseArg> getSql_orderbyclauseargs() {
        return sql_orderbyclauseargs;
    }

    public void addSql_orderbyclausearg(Sql_orderbyclausearg sql_orderbyclausearg) {
        this.sql_orderbyclauseargs.add(sql_orderbyclausearg);
    }

}