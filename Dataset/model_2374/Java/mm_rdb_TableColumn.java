





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_TableColumn extends Column {

    private String type;





    private Table table;


    public mm_rdb_TableColumn(
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

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}