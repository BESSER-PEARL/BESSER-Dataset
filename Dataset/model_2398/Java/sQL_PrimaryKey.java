





import java.util.List;
import java.util.ArrayList;

public class sQL_PrimaryKey  {






    private sQL_Table sql_table;




    private List<sQL_Column> sql_columns;


    public sQL_PrimaryKey(
    ) {
        this.sql_columns = new ArrayList<>();
    }

    public sQL_PrimaryKey(
        ArrayList<sQL_Column> sql_columns    ) {
        this.sql_columns = sql_columns;
    }


    public sQL_Table getSql_table() {
        return sql_table;
    }

    public void setSql_table(sQL_Table sql_table) {
        this.sql_table = sql_table;
    }
    public List<sQL_Column> getSql_columns() {
        return sql_columns;
    }

    public void addSql_column(Sql_column sql_column) {
        this.sql_columns.add(sql_column);
    }

}