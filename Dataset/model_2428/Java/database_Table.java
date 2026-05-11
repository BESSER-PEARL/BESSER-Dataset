





import java.util.List;
import java.util.ArrayList;

public class database_Table  {

    private String Name;





    private database_Database database_database;




    private database_Database database_database;




    private database_ForeignKey database_foreignkey;




    private database_ForeignKey database_foreignkey;


    public database_Table(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }

}