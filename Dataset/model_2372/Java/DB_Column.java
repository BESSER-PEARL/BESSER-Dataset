





import java.util.List;
import java.util.ArrayList;

public class DB_Column  {

    private String type;
    private String name;
    private boolean notNull;





    private DB_Table db_table;




    private List<DB_ForeignKey> db_foreignkeys;




    private DB_ForeignKey db_foreignkey;




    private DB_Table db_table;




    private DB_Key db_key;




    private DB_Key db_key;


    public DB_Column(
        String type,        String name,        boolean notNull    ) {
        this.type = type;
        this.name = name;
        this.notNull = notNull;
        this.db_foreignkeys = new ArrayList<>();
    }

    public DB_Column(
        String type,        String name,        boolean notNull        ArrayList<DB_ForeignKey> db_foreignkeys    ) {
        this.type = type;
        this.name = name;
        this.notNull = notNull;
        this.db_foreignkeys = db_foreignkeys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNotnull() {
        return notNull;
    }

    public void setNotnull(boolean notNull) {
        this.notNull = notNull;
    }

    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }
    public List<DB_ForeignKey> getDb_foreignkeys() {
        return db_foreignkeys;
    }

    public void addDb_foreignkey(Db_foreignkey db_foreignkey) {
        this.db_foreignkeys.add(db_foreignkey);
    }
    public DB_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(DB_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }
    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }
    public DB_Key getDb_key() {
        return db_key;
    }

    public void setDb_key(DB_Key db_key) {
        this.db_key = db_key;
    }
    public DB_Key getDb_key() {
        return db_key;
    }

    public void setDb_key(DB_Key db_key) {
        this.db_key = db_key;
    }

}