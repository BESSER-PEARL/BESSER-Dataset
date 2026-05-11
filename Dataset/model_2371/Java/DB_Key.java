





import java.util.List;
import java.util.ArrayList;

public class DB_Key  {

    private String name;





    private DB_ForeignKey db_foreignkey;




    private DB_ForeignKey db_foreignkey;




    private DB_Column db_column;




    private List<DB_Column> db_columns;




    private DB_Table db_table;


    public DB_Key(
        String name    ) {
        this.name = name;
        this.db_columns = new ArrayList<>();
    }

    public DB_Key(
        String name        ArrayList<DB_Column> db_columns    ) {
        this.name = name;
        this.db_columns = db_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DB_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(DB_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }
    public DB_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(DB_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }
    public DB_Column getDb_column() {
        return db_column;
    }

    public void setDb_column(DB_Column db_column) {
        this.db_column = db_column;
    }
    public List<DB_Column> getDb_columns() {
        return db_columns;
    }

    public void addDb_column(Db_column db_column) {
        this.db_columns.add(db_column);
    }
    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }

}