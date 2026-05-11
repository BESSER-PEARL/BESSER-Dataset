





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_CreateTable extends Operation {

    private String tableName;



    public mm_rdb_CreateTable(
        String tableName    ) {
        super(
        );
        this.tableName = tableName;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }


}