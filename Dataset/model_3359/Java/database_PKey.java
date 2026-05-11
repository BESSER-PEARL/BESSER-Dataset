





import java.util.List;
import java.util.ArrayList;

public class database_PKey extends RefPKey {

    private String name;





    private List<database_Column> database_columns;


    public database_PKey(
        String name    ) {
        super(
        );
        this.name = name;
        this.database_columns = new ArrayList<>();
    }

    public database_PKey(
        String name        ArrayList<database_Column> database_columns    ) {
        this.name = name;
        this.database_columns = database_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }

}