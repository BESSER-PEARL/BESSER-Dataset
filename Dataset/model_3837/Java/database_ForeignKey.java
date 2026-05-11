





import java.util.List;
import java.util.ArrayList;

public class database_ForeignKey  {






    private database_Table database_table;




    private List<database_Column> database_columns;




    private database_Table database_table;


    public database_ForeignKey(
    ) {
        this.database_columns = new ArrayList<>();
    }

    public database_ForeignKey(
        ArrayList<database_Column> database_columns    ) {
        this.database_columns = database_columns;
    }


    public database_Table getDatabase_table() {
        return database_table;
    }

    public void setDatabase_table(database_Table database_table) {
        this.database_table = database_table;
    }
    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }
    public database_Table getDatabase_table() {
        return database_table;
    }

    public void setDatabase_table(database_Table database_table) {
        this.database_table = database_table;
    }

}