





import java.util.List;
import java.util.ArrayList;

public class DB_Column extends DatabaseElement {

    private boolean notNull;
    private String type;





    private DB_Table db_table;




    private DB_ForeignKey db_foreignkey;




    private DB_Table db_table;




    private DB_Table db_table;




    private DB_ForeignKey db_foreignkey;


    public DB_Column(
        boolean notNull,        String type    ) {
        super(
        );
        this.notNull = notNull;
        this.type = type;
    }


    public boolean getNotnull() {
        return notNull;
    }

    public void setNotnull(boolean notNull) {
        this.notNull = notNull;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
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
    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }
    public DB_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(DB_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }

}