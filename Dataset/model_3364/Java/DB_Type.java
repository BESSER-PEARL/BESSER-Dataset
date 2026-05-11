





import java.util.List;
import java.util.ArrayList;

public class DB_Type extends DatabaseElement {






    private DB_Column db_column;


    public DB_Type(
    ) {
        super(
        );
    }



    public DB_Column getDb_column() {
        return db_column;
    }

    public void setDb_column(DB_Column db_column) {
        this.db_column = db_column;
    }

}