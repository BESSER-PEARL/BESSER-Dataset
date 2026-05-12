





import java.util.List;
import java.util.ArrayList;

public class database_Table extends NamedElement {

    private String collation;
    private String storageEngine;





    private database_DataBase database_database;




    private database_DataBase database_database;


    public database_Table(
        String collation,        String storageEngine    ) {
        super(
        );
        this.collation = collation;
        this.storageEngine = storageEngine;
    }


    public String getCollation() {
        return collation;
    }

    public void setCollation(String collation) {
        this.collation = collation;
    }
    public String getStorageengine() {
        return storageEngine;
    }

    public void setStorageengine(String storageEngine) {
        this.storageEngine = storageEngine;
    }

    public database_DataBase getDatabase_database() {
        return database_database;
    }

    public void setDatabase_database(database_DataBase database_database) {
        this.database_database = database_database;
    }
    public database_DataBase getDatabase_database() {
        return database_database;
    }

    public void setDatabase_database(database_DataBase database_database) {
        this.database_database = database_database;
    }

}