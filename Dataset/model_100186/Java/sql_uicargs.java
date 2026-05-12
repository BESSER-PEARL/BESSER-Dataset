





import java.util.List;
import java.util.ArrayList;

public class sql_uicargs extends UnpivotInClauseArgs {






    private List<sql_UnpivotInClauseArg> sql_unpivotinclauseargs;


    public sql_uicargs(
    ) {
        super(
        );
        this.sql_unpivotinclauseargs = new ArrayList<>();
    }

    public sql_uicargs(
        ArrayList<sql_UnpivotInClauseArg> sql_unpivotinclauseargs    ) {
        this.sql_unpivotinclauseargs = sql_unpivotinclauseargs;
    }


    public List<sql_UnpivotInClauseArg> getSql_unpivotinclauseargs() {
        return sql_unpivotinclauseargs;
    }

    public void addSql_unpivotinclausearg(Sql_unpivotinclausearg sql_unpivotinclausearg) {
        this.sql_unpivotinclauseargs.add(sql_unpivotinclausearg);
    }

}