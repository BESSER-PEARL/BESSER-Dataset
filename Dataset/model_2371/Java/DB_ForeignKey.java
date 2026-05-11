





import java.util.List;
import java.util.ArrayList;

public class DB_ForeignKey  {

    private String isMany;





    private DB_Column db_column;




    private DB_Column db_column;




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

    public DB_Column getDb_column() {
        return db_column;
    }

    public void setDb_column(DB_Column db_column) {
        this.db_column = db_column;
    }
    public DB_Column getDb_column() {
        return db_column;
    }

    public void setDb_column(DB_Column db_column) {
        this.db_column = db_column;
    }
    public DB_Table getDb_table() {
        return db_table;
    }

    public void setDb_table(DB_Table db_table) {
        this.db_table = db_table;
    }

}