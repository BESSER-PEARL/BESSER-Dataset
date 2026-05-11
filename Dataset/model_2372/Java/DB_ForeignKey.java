





import java.util.List;
import java.util.ArrayList;

public class DB_ForeignKey  {

    private String isMany;





    private DB_Table db_table;


    public DB_ForeignKey(
        String isMany    ) {
        this.isMany = isMany;
    }


    public String getIsmany() {
        return isMany;
    }

    public void setIsmany(String isMany) {
        this.isMany = isMany;
    }

    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }

}