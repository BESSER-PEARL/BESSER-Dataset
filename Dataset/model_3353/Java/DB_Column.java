





import java.util.List;
import java.util.ArrayList;

public class DB_Column  {

    private String Name;





    private DB_Table db_table;


    public DB_Column(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }

}