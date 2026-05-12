





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_Table  {

    private String name;





    private List<SQL2003_V2_Column> sql2003_v2_columns;




    private SQL2003_V2_Schema sql2003_v2_schema;




    private SQL2003_V2_Column sql2003_v2_column;




    private SQL2003_V2_Schema sql2003_v2_schema;


    public SQL2003_V2_Table(
        String name    ) {
        this.name = name;
        this.sql2003_v2_columns = new ArrayList<>();
    }

    public SQL2003_V2_Table(
        String name        ArrayList<SQL2003_V2_Column> sql2003_v2_columns    ) {
        this.name = name;
        this.sql2003_v2_columns = sql2003_v2_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SQL2003_V2_Column> getSql2003_v2_columns() {
        return sql2003_v2_columns;
    }

    public void addSql2003_v2_column(Sql2003_v2_column sql2003_v2_column) {
        this.sql2003_v2_columns.add(sql2003_v2_column);
    }
    public SQL2003_V2_Schema getSql2003_v2_schema() {
        return sql2003_v2_schema;
    }

    public void setSql2003_v2_schema(SQL2003_V2_Schema sql2003_v2_schema) {
        this.sql2003_v2_schema = sql2003_v2_schema;
    }
    public SQL2003_V2_Column getSql2003_v2_column() {
        return sql2003_v2_column;
    }

    public void setSql2003_v2_column(SQL2003_V2_Column sql2003_v2_column) {
        this.sql2003_v2_column = sql2003_v2_column;
    }
    public SQL2003_V2_Schema getSql2003_v2_schema() {
        return sql2003_v2_schema;
    }

    public void setSql2003_v2_schema(SQL2003_V2_Schema sql2003_v2_schema) {
        this.sql2003_v2_schema = sql2003_v2_schema;
    }

}