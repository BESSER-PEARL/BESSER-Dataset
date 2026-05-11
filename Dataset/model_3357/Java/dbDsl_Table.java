





import java.util.List;
import java.util.ArrayList;

public class dbDsl_Table  {

    private String name;





    private dbDsl_Database dbdsl_database;


    public dbDsl_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbDsl_Database getDbdsl_database() {
        return dbdsl_database;
    }

    public void setDbdsl_database(dbDsl_Database dbdsl_database) {
        this.dbdsl_database = dbdsl_database;
    }

}