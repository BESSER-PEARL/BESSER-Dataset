





import java.util.List;
import java.util.ArrayList;

public class database_ForeignKey  {






    private List<database_Column> database_columns;


    public database_ForeignKey(
    ) {
        this.database_columns = new ArrayList<>();
    }

    public database_ForeignKey(
        ArrayList<database_Column> database_columns    ) {
        this.database_columns = database_columns;
    }


    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }

}