





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_Table  {

    private String name;





    private SQL2003_evo_Column sql2003_evo_column;




    private SQL2003_evo_Schema sql2003_evo_schema;




    private SQL2003_evo_Schema sql2003_evo_schema;




    private List<SQL2003_evo_Column> sql2003_evo_columns;


    public SQL2003_evo_Table(
        String name    ) {
        this.name = name;
        this.sql2003_evo_columns = new ArrayList<>();
    }

    public SQL2003_evo_Table(
        String name        ArrayList<SQL2003_evo_Column> sql2003_evo_columns    ) {
        this.name = name;
        this.sql2003_evo_columns = sql2003_evo_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_evo_Column getSql2003_evo_column() {
        return sql2003_evo_column;
    }

    public void setSql2003_evo_column(SQL2003_evo_Column sql2003_evo_column) {
        this.sql2003_evo_column = sql2003_evo_column;
    }
    public SQL2003_evo_Schema getSql2003_evo_schema() {
        return sql2003_evo_schema;
    }

    public void setSql2003_evo_schema(SQL2003_evo_Schema sql2003_evo_schema) {
        this.sql2003_evo_schema = sql2003_evo_schema;
    }
    public SQL2003_evo_Schema getSql2003_evo_schema() {
        return sql2003_evo_schema;
    }

    public void setSql2003_evo_schema(SQL2003_evo_Schema sql2003_evo_schema) {
        this.sql2003_evo_schema = sql2003_evo_schema;
    }
    public List<SQL2003_evo_Column> getSql2003_evo_columns() {
        return sql2003_evo_columns;
    }

    public void addSql2003_evo_column(Sql2003_evo_column sql2003_evo_column) {
        this.sql2003_evo_columns.add(sql2003_evo_column);
    }

}