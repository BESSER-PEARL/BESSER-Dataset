





import java.util.List;
import java.util.ArrayList;

public class SQL2003_Table  {

    private String name;





    private SQL2003_Schema sql2003_schema;




    private SQL2003_Column sql2003_column;




    private SQL2003_Schema sql2003_schema;




    private List<SQL2003_Column> sql2003_columns;


    public SQL2003_Table(
        String name    ) {
        this.name = name;
        this.sql2003_columns = new ArrayList<>();
    }

    public SQL2003_Table(
        String name        ArrayList<SQL2003_Column> sql2003_columns    ) {
        this.name = name;
        this.sql2003_columns = sql2003_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_Schema getSql2003_schema() {
        return sql2003_schema;
    }

    public void setSql2003_schema(SQL2003_Schema sql2003_schema) {
        this.sql2003_schema = sql2003_schema;
    }
    public SQL2003_Column getSql2003_column() {
        return sql2003_column;
    }

    public void setSql2003_column(SQL2003_Column sql2003_column) {
        this.sql2003_column = sql2003_column;
    }
    public SQL2003_Schema getSql2003_schema() {
        return sql2003_schema;
    }

    public void setSql2003_schema(SQL2003_Schema sql2003_schema) {
        this.sql2003_schema = sql2003_schema;
    }
    public List<SQL2003_Column> getSql2003_columns() {
        return sql2003_columns;
    }

    public void addSql2003_column(Sql2003_column sql2003_column) {
        this.sql2003_columns.add(sql2003_column);
    }

}