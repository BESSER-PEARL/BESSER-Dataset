





import java.util.List;
import java.util.ArrayList;

public class database_Table  {

    private String name;





    private database_Scheme database_scheme;


    public database_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public database_Scheme getDatabase_scheme() {
        return database_scheme;
    }

    public void setDatabase_scheme(database_Scheme database_scheme) {
        this.database_scheme = database_scheme;
    }

}