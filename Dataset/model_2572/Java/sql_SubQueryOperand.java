





import java.util.List;
import java.util.ArrayList;

public class sql_SubQueryOperand  {






    private sql_SelectQuery sql_selectquery;




    private sql_TableOrAlias sql_tableoralias;


    public sql_SubQueryOperand(
    ) {
    }



    public sql_SelectQuery getSql_selectquery() {
        return sql_selectquery;
    }

    public void setSql_selectquery(sql_SelectQuery sql_selectquery) {
        this.sql_selectquery = sql_selectquery;
    }
    public sql_TableOrAlias getSql_tableoralias() {
        return sql_tableoralias;
    }

    public void setSql_tableoralias(sql_TableOrAlias sql_tableoralias) {
        this.sql_tableoralias = sql_tableoralias;
    }

}