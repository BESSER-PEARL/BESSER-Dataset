





import java.util.List;
import java.util.ArrayList;

public class mongodb_Collection  {

    private String name;





    private mongodb_Database mongodb_database;


    public mongodb_Collection(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mongodb_Database getMongodb_database() {
        return mongodb_database;
    }

    public void setMongodb_database(mongodb_Database mongodb_database) {
        this.mongodb_database = mongodb_database;
    }

}