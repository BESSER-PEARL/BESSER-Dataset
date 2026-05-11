





import java.util.List;
import java.util.ArrayList;

public class DB_Table extends DatabaseElement {






    private List<DB_Column> db_columns;




    private List<DB_Column> db_columns;


    public DB_Table(
    ) {
        super(
        );
        this.db_columns = new ArrayList<>();
        this.db_columns = new ArrayList<>();
    }

    public DB_Table(
        ArrayList<DB_Column> db_columns,        ArrayList<DB_Column> db_columns    ) {
        this.db_columns = db_columns;
        this.db_columns = db_columns;
    }


    public List<DB_Column> getDb_columns() {
        return db_columns;
    }

    public void addDb_column(Db_column db_column) {
        this.db_columns.add(db_column);
    }
    public List<DB_Column> getDb_columns() {
        return db_columns;
    }

    public void addDb_column(Db_column db_column) {
        this.db_columns.add(db_column);
    }

}