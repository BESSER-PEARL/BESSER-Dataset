





import java.util.List;
import java.util.ArrayList;

public class sql_ForeignKey  {






    private List<sql_Column> sql_columns;




    private sql_Table sql_table;




    private List<sql_Column> sql_columns;


    public sql_ForeignKey(
    ) {
        this.sql_columns = new ArrayList<>();
        this.sql_columns = new ArrayList<>();
    }

    public sql_ForeignKey(
        ArrayList<sql_Column> sql_columns,        ArrayList<sql_Column> sql_columns    ) {
        this.sql_columns = sql_columns;
        this.sql_columns = sql_columns;
    }


    public List<sql_Column> getSql_columns() {
        return sql_columns;
    }

    public void addSql_column(Sql_column sql_column) {
        this.sql_columns.add(sql_column);
    }
    public sql_Table getSql_table() {
        return sql_table;
    }

    public void setSql_table(sql_Table sql_table) {
        this.sql_table = sql_table;
    }
    public List<sql_Column> getSql_columns() {
        return sql_columns;
    }

    public void addSql_column(Sql_column sql_column) {
        this.sql_columns.add(sql_column);
    }

}