





import java.util.List;
import java.util.ArrayList;

public class database_Table  {

    private String Name;





    private List<database_Column> database_columns;




    private database_Database database_database;




    private database_ForeignKey database_foreignkey;




    private database_Column database_column;




    private database_ForeignKey database_foreignkey;




    private database_Database database_database;


    public database_Table(
        String Name    ) {
        this.Name = Name;
        this.database_columns = new ArrayList<>();
    }

    public database_Table(
        String Name        ArrayList<database_Column> database_columns    ) {
        this.Name = Name;
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
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public database_Column getDatabase_column() {
        return database_column;
    }

    public void setDatabase_column(database_Column database_column) {
        this.database_column = database_column;
    }
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public database_Database getDatabase_database() {
        return database_database;
    }

    public void setDatabase_database(database_Database database_database) {
        this.database_database = database_database;
    }

}