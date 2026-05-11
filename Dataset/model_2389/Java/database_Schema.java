





import java.util.List;
import java.util.ArrayList;

public class database_Schema extends DataBaseElement {






    private List<database_Table> database_tables;


    public database_Schema(
    ) {
        super(
        );
        this.database_tables = new ArrayList<>();
    }

    public database_Schema(
        ArrayList<database_Table> database_tables    ) {
        this.database_tables = database_tables;
    }


    public List<database_Table> getDatabase_tables() {
        return database_tables;
    }

    public void addDatabase_table(Database_table database_table) {
        this.database_tables.add(database_table);
    }

}