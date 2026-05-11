





import java.util.List;
import java.util.ArrayList;

public class sql_DbObjectName extends ColumnFull, TableFull {

    private String dbname;





    private sql_Col sql_col;




    private sql_TableOrAlias sql_tableoralias;




    private sql_ColumnOrAlias sql_columnoralias;


    public sql_DbObjectName(
        String dbname    ) {
        super(
        );
        this.dbname = dbname;
    }


    public String getDbname() {
        return dbname;
    }

    public void setDbname(String dbname) {
        this.dbname = dbname;
    }

    public sql_Col getSql_col() {
        return sql_col;
    }

    public void setSql_col(sql_Col sql_col) {
        this.sql_col = sql_col;
    }
    public sql_TableOrAlias getSql_tableoralias() {
        return sql_tableoralias;
    }

    public void setSql_tableoralias(sql_TableOrAlias sql_tableoralias) {
        this.sql_tableoralias = sql_tableoralias;
    }
    public sql_ColumnOrAlias getSql_columnoralias() {
        return sql_columnoralias;
    }

    public void setSql_columnoralias(sql_ColumnOrAlias sql_columnoralias) {
        this.sql_columnoralias = sql_columnoralias;
    }

}