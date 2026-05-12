





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_Table  {

    private String name;





    private SQL2003_V3_Schema sql2003_v3_schema;




    private SQL2003_V3_Schema sql2003_v3_schema;




    private List<SQL2003_V3_Column> sql2003_v3_columns;




    private SQL2003_V3_Column sql2003_v3_column;


    public SQL2003_V3_Table(
        String name    ) {
        this.name = name;
        this.sql2003_v3_columns = new ArrayList<>();
    }

    public SQL2003_V3_Table(
        String name        ArrayList<SQL2003_V3_Column> sql2003_v3_columns    ) {
        this.name = name;
        this.sql2003_v3_columns = sql2003_v3_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_V3_Schema getSql2003_v3_schema() {
        return sql2003_v3_schema;
    }

    public void setSql2003_v3_schema(SQL2003_V3_Schema sql2003_v3_schema) {
        this.sql2003_v3_schema = sql2003_v3_schema;
    }
    public SQL2003_V3_Schema getSql2003_v3_schema() {
        return sql2003_v3_schema;
    }

    public void setSql2003_v3_schema(SQL2003_V3_Schema sql2003_v3_schema) {
        this.sql2003_v3_schema = sql2003_v3_schema;
    }
    public List<SQL2003_V3_Column> getSql2003_v3_columns() {
        return sql2003_v3_columns;
    }

    public void addSql2003_v3_column(Sql2003_v3_column sql2003_v3_column) {
        this.sql2003_v3_columns.add(sql2003_v3_column);
    }
    public SQL2003_V3_Column getSql2003_v3_column() {
        return sql2003_v3_column;
    }

    public void setSql2003_v3_column(SQL2003_V3_Column sql2003_v3_column) {
        this.sql2003_v3_column = sql2003_v3_column;
    }

}