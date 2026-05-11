





import java.util.List;
import java.util.ArrayList;

public class relational_Schema  {

    private String name;





    private relational_DataBase relational_database;


    public relational_Schema(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public relational_DataBase getRelational_database() {
        return relational_database;
    }

    public void setRelational_database(relational_DataBase relational_database) {
        this.relational_database = relational_database;
    }

}