





import java.util.List;
import java.util.ArrayList;

public class sql_Model  {






    private sql_SelectQuery sql_selectquery;




    private sql_WithQuery sql_withquery;


    public sql_Model(
    ) {
    }



    public sql_SelectQuery getSql_selectquery() {
        return sql_selectquery;
    }

    public void setSql_selectquery(sql_SelectQuery sql_selectquery) {
        this.sql_selectquery = sql_selectquery;
    }
    public sql_WithQuery getSql_withquery() {
        return sql_withquery;
    }

    public void setSql_withquery(sql_WithQuery sql_withquery) {
        this.sql_withquery = sql_withquery;
    }

}