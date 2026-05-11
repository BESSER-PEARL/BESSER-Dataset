





import java.util.List;
import java.util.ArrayList;

public class DB_ForeignKey extends DatabaseElement {

    private String isMany;





    private DB_Column db_column;




    private DB_Column db_column;


    public DB_ForeignKey(
        String isMany    ) {
        super(
        );
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

}