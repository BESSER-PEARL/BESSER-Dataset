





import java.util.List;
import java.util.ArrayList;

public class sql_DbObjectNameAll  {

    private String dbname;





    private sql_ColumnOrAlias sql_columnoralias;


    public sql_DbObjectNameAll(
        String dbname    ) {
        this.dbname = dbname;
    }


    public String getDbname() {
        return dbname;
    }

    public void setDbname(String dbname) {
        this.dbname = dbname;
    }

    public sql_ColumnOrAlias getSql_columnoralias() {
        return sql_columnoralias;
    }

    public void setSql_columnoralias(sql_ColumnOrAlias sql_columnoralias) {
        this.sql_columnoralias = sql_columnoralias;
    }

}