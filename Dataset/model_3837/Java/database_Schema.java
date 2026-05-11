





import java.util.List;
import java.util.ArrayList;

public class database_Schema  {

    private String name;





    private List<database_Table> database_tables;


    public database_Schema(
        String name    ) {
        this.name = name;
        this.database_tables = new ArrayList<>();
    }

    public database_Schema(
        String name        ArrayList<database_Table> database_tables    ) {
        this.name = name;
        this.database_tables = database_tables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<database_Table> getDatabase_tables() {
        return database_tables;
    }

    public void addDatabase_table(Database_table database_table) {
        this.database_tables.add(database_table);
    }

}