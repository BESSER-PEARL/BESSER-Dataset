





import java.util.List;
import java.util.ArrayList;

public class sql_Table  {

    private String name;





    private sql_Database sql_database;


    public sql_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sql_Database getSql_database() {
        return sql_database;
    }

    public void setSql_database(sql_Database sql_database) {
        this.sql_database = sql_database;
    }

}