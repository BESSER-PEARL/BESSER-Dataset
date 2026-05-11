





import java.util.List;
import java.util.ArrayList;

public class DB_Key  {

    private String name;





    private DB_ForeignKey db_foreignkey;




    private DB_Table db_table;




    private DB_ForeignKey db_foreignkey;


    public DB_Key(
        String name    ) {
        this.name = name;
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