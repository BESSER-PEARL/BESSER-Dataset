





import java.util.List;
import java.util.ArrayList;

public class rdb_Key  {






    private rdb_Table rdb_table;




    private List<rdb_Column> rdb_columns;


    public rdb_Key(
    ) {
        this.rdb_columns = new ArrayList<>();
    }

    public rdb_Key(
        ArrayList<rdb_Column> rdb_columns    ) {
        this.rdb_columns = rdb_columns;
    }


    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }
    public List<rdb_Column> getRdb_columns() {
        return rdb_columns;
    }

    public void addRdb_column(Rdb_column rdb_column) {
        this.rdb_columns.add(rdb_column);
    }

}