





import java.util.List;
import java.util.ArrayList;

public class sql_PrimaryKey  {






    private List<sql_Column> sql_columns;


    public sql_PrimaryKey(
    ) {
        this.sql_columns = new ArrayList<>();
    }

    public sql_PrimaryKey(
        ArrayList<sql_Column> sql_columns    ) {
        this.sql_columns = sql_columns;
    }


    public List<sql_Column> getSql_columns() {
        return sql_columns;
    }

    public void addSql_column(Sql_column sql_column) {
        this.sql_columns.add(sql_column);
    }

}