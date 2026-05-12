





import java.util.List;
import java.util.ArrayList;

public class database_ForeignKey  {

    private String Name;





    private List<database_Column> database_columns;




    private database_Database database_database;




    private database_Database database_database;




    private List<database_Column> database_columns;


    public database_ForeignKey(
        String Name    ) {
        this.Name = Name;
        this.database_columns = new ArrayList<>();
        this.database_columns = new ArrayList<>();
    }

    public database_ForeignKey(
        String Name        ArrayList<database_Column> database_columns,        ArrayList<database_Column> database_columns    ) {
        this.Name = Name;
        this.database_columns = database_columns;
        this.database_columns = database_columns;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }
    public database_Database getDatabase_database() {
        return database_database;
    }

    public void setDatabase_database(database_Database database_database) {
        this.database_database = database_database;
    }
    public database_Database getDatabase_database() {
        return database_database;
    }

    public void setDatabase_database(database_Database database_database) {
        this.database_database = database_database;
    }
    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }

}