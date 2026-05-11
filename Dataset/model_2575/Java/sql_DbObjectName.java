





import java.util.List;
import java.util.ArrayList;

public class sql_DbObjectName extends UsingCols, TableFull, ColumnFull, PivotCol {

    private String dbname;





    private sql_UsingCols sql_usingcols;


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

    public sql_UsingCols getSql_usingcols() {
        return sql_usingcols;
    }

    public void setSql_usingcols(sql_UsingCols sql_usingcols) {
        this.sql_usingcols = sql_usingcols;
    }

}