





import java.util.List;
import java.util.ArrayList;

public class rdb_ForeignKey extends Key {






    private rdb_Column rdb_column;


    public rdb_ForeignKey(
    ) {
        super(
        );
    }



    public rdb_Column getRdb_column() {
        return rdb_column;
    }

    public void setRdb_column(rdb_Column rdb_column) {
        this.rdb_column = rdb_column;
    }

}