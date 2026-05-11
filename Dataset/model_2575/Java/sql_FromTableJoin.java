





import java.util.List;
import java.util.ArrayList;

public class sql_FromTableJoin  {

    private String join;





    private sql_FromTable sql_fromtable;




    private sql_TableOrAlias sql_tableoralias;




    private sql_JoinCondition sql_joincondition;


    public sql_FromTableJoin(
        String join    ) {
        this.join = join;
    }


    public String getJoin() {
        return join;
    }

    public void setJoin(String join) {
        this.join = join;
    }

    public sql_FromTable getSql_fromtable() {
        return sql_fromtable;
    }

    public void setSql_fromtable(sql_FromTable sql_fromtable) {
        this.sql_fromtable = sql_fromtable;
    }
    public sql_TableOrAlias getSql_tableoralias() {
        return sql_tableoralias;
    }

    public void setSql_tableoralias(sql_TableOrAlias sql_tableoralias) {
        this.sql_tableoralias = sql_tableoralias;
    }
    public sql_JoinCondition getSql_joincondition() {
        return sql_joincondition;
    }

    public void setSql_joincondition(sql_JoinCondition sql_joincondition) {
        this.sql_joincondition = sql_joincondition;
    }

}