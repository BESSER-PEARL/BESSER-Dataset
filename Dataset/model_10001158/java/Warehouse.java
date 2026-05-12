





import java.util.List;
import java.util.ArrayList;

public class Warehouse  {

    private String location;
    private String database;



    public Warehouse(
        String location,        String database    ) {
        this.location = location;
        this.database = database;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }


}