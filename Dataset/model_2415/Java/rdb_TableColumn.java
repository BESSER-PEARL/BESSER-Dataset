





import java.util.List;
import java.util.ArrayList;

public class rdb_TableColumn extends Column {

    private String isPrimaryKey;
    private String isForeignKey;





    private rdb_Table rdb_table;


    public rdb_TableColumn(
        String isPrimaryKey,        String isForeignKey    ) {
        super(
        );
        this.isPrimaryKey = isPrimaryKey;
        this.isForeignKey = isForeignKey;
    }


    public String getIsprimarykey() {
        return isPrimaryKey;
    }

    public void setIsprimarykey(String isPrimaryKey) {
        this.isPrimaryKey = isPrimaryKey;
    }
    public String getIsforeignkey() {
        return isForeignKey;
    }

    public void setIsforeignkey(String isForeignKey) {
        this.isForeignKey = isForeignKey;
    }

    public rdb_Table getRdb_table() {
        return rdb_table;
    }

    public void setRdb_table(rdb_Table rdb_table) {
        this.rdb_table = rdb_table;
    }

}