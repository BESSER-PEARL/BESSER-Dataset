





import java.util.List;
import java.util.ArrayList;

public class db_Column extends DatabaseElement {

    private String type;





    private db_Table db_table;




    private db_ForeignKey db_foreignkey;




    private db_Table db_table;




    private db_Table db_table;




    private db_ForeignKey db_foreignkey;


    public db_Column(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public db_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(db_Table db_table) {
        this.db_table = db_table;
    }
    public db_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(db_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }
    public db_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(db_Table db_table) {
        this.db_table = db_table;
    }
    public db_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(db_Table db_table) {
        this.db_table = db_table;
    }
    public db_ForeignKey getDb_foreignkey() {
        return db_foreignkey;
    }

    public void setDb_foreignkey(db_ForeignKey db_foreignkey) {
        this.db_foreignkey = db_foreignkey;
    }

}