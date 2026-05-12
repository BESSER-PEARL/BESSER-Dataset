





import java.util.List;
import java.util.ArrayList;

public class sql_UnipivotInClause extends UnpivotInClause {

    private String op;





    private sql_UnpivotInClauseArgs sql_unpivotinclauseargs;


    public sql_UnipivotInClause(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public sql_UnpivotInClauseArgs getSql_unpivotinclauseargs() {
        return sql_unpivotinclauseargs;
    }

    public void setSql_unpivotinclauseargs(sql_UnpivotInClauseArgs sql_unpivotinclauseargs) {
        this.sql_unpivotinclauseargs = sql_unpivotinclauseargs;
    }

}