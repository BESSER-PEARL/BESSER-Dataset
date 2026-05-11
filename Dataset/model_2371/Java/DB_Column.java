





import java.util.List;
import java.util.ArrayList;

public class DB_Column  {

    private String type;
    private String name;
    private boolean notNull;





    private DB_Table db_table;




    private DB_Table db_table;


    public DB_Column(
        String type,        String name,        boolean notNull    ) {
        this.type = type;
        this.name = name;
        this.notNull = notNull;
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
    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }

}