





import java.util.List;
import java.util.ArrayList;

public class genSql_Table  {

    private String name;





    private genSql_DataBase gensql_database;


    public genSql_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public genSql_DataBase getGensql_database() {
        return gensql_database;
    }

    public void setGensql_database(genSql_DataBase gensql_database) {
        this.gensql_database = gensql_database;
    }

}