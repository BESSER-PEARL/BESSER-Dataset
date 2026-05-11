





import java.util.List;
import java.util.ArrayList;

public class sql_FromTableJoin  {

    private String join;





    private sql_OrExpr sql_orexpr;




    private sql_FromTable sql_fromtable;




    private sql_TableOrAlias sql_tableoralias;


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

    public sql_OrExpr getSql_orexpr() {
        return sql_orexpr;
    }

    public void setSql_orexpr(sql_OrExpr sql_orexpr) {
        this.sql_orexpr = sql_orexpr;
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

}