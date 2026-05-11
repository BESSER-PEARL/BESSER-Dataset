





import java.util.List;
import java.util.ArrayList;

public class Database_Table  {

    private String heading;





    private List<Database_Column> database_columns;




    private Database_DB database_db;


    public Database_Table(
        String heading    ) {
        this.heading = heading;
        this.database_columns = new ArrayList<>();
    }

    public Database_Table(
        String heading        ArrayList<Database_Column> database_columns    ) {
        this.heading = heading;
        this.database_columns = database_columns;
    }

    public String getHeading() {
        return heading;
    }

    public void setHeading(String heading) {
        this.heading = heading;
    }

    public List<Database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }
    public Database_DB getDatabase_db() {
        return database_db;
    }

    public void setDatabase_db(Database_DB database_db) {
        this.database_db = database_db;
    }

}