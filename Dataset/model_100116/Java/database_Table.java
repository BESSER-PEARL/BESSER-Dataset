





import java.util.List;
import java.util.ArrayList;

public class database_Table  {

    private boolean is_local;
    private String name;





    private database_Schema database_schema;




    private List<database_ForeignKey> database_foreignkeys;




    private List<database_Column> database_columns;




    private database_ForeignKey database_foreignkey;




    private List<database_Column> database_columns;


    public database_Table(
        boolean is_local,        String name    ) {
        this.is_local = is_local;
        this.name = name;
        this.database_foreignkeys = new ArrayList<>();
        this.database_columns = new ArrayList<>();
        this.database_columns = new ArrayList<>();
    }

    public database_Table(
        boolean is_local,        String name        ArrayList<database_ForeignKey> database_foreignkeys,        ArrayList<database_Column> database_columns,        ArrayList<database_Column> database_columns    ) {
        this.is_local = is_local;
        this.name = name;
        this.database_foreignkeys = database_foreignkeys;
        this.database_columns = database_columns;
        this.database_columns = database_columns;
    }

    public boolean getIs_local() {
        return is_local;
    }

    public void setIs_local(boolean is_local) {
        this.is_local = is_local;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public database_Schema getDatabase_schema() {
        return database_schema;
    }

    public void setDatabase_schema(database_Schema database_schema) {
        this.database_schema = database_schema;
    }
    public List<database_ForeignKey> getDatabase_foreignkeys() {
        return database_foreignkeys;
    }

    public void addDatabase_foreignkey(Database_foreignkey database_foreignkey) {
        this.database_foreignkeys.add(database_foreignkey);
    }
    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }
    public database_ForeignKey getDatabase_foreignkey() {
        return database_foreignkey;
    }

    public void setDatabase_foreignkey(database_ForeignKey database_foreignkey) {
        this.database_foreignkey = database_foreignkey;
    }
    public List<database_Column> getDatabase_columns() {
        return database_columns;
    }

    public void addDatabase_column(Database_column database_column) {
        this.database_columns.add(database_column);
    }

}