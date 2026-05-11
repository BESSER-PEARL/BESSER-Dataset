





import java.util.List;
import java.util.ArrayList;

public class sQL_Table  {

    private String name;





    private sQL_DataBase sql_database;


    public sQL_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sQL_DataBase getSql_database() {
        return sql_database;
    }

    public void setSql_database(sQL_DataBase sql_database) {
        this.sql_database = sql_database;
    }

}