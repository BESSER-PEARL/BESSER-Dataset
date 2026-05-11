





import java.util.List;
import java.util.ArrayList;

public class database_PrimaryKey extends NamedElement {






    private List<database_Column> database_columns;




    private database_Column database_column;


    public database_PrimaryKey(
    ) {
        super(
        );
        this.database_columns = new ArrayList<>();
    }

    public database_PrimaryKey(
        ArrayList<database_Column> database_columns    ) {
        this.database_columns = database_columns;
    }


    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }
    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }

}