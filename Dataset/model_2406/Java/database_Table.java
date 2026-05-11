





import java.util.List;
import java.util.ArrayList;

public class database_Table extends NamedElement {

    private String collation;
    private String storageEngine;





    private List<database_Unique> database_uniques;




    private database_PrimaryKey database_primarykey;




    private List<database_Index> database_indexs;




    private database_DataBase database_database;




    private database_DataBase database_database;


    public database_Table(
        String collation,        String storageEngine    ) {
        super(
        );
        this.collation = collation;
        this.storageEngine = storageEngine;
        this.database_uniques = new ArrayList<>();
        this.database_indexs = new ArrayList<>();
    }

    public database_Table(
        String collation,        String storageEngine        ArrayList<database_Unique> database_uniques,        ArrayList<database_Index> database_indexs    ) {
        this.collation = collation;
        this.storageEngine = storageEngine;
        this.database_uniques = database_uniques;
        this.database_indexs = database_indexs;
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

    public List<database_Unique> getDatabase_uniques() {
        return database_uniques;
    }

    public void addDatabase_unique(Database_unique database_unique) {
        this.database_uniques.add(database_unique);
    }
    public database_PrimaryKey getDatabase_primarykey() {
        return database_primarykey;
    }

    public void setDatabase_primarykey(database_PrimaryKey database_primarykey) {
        this.database_primarykey = database_primarykey;
    }
    public List<database_Index> getDatabase_indexs() {
        return database_indexs;
    }

    public void addDatabase_index(Database_index database_index) {
        this.database_indexs.add(database_index);
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