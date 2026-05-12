





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_DeleteColumn extends Operation {






    private Table table;




    private TableColumn tablecolumn;


    public mm_rdb_DeleteColumn(
    ) {
        super(
        );
    }



    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }
    public TableColumn getTablecolumn() {
        return tablecolumn;
    }

    public void setTablecolumn(TableColumn tablecolumn) {
        this.tablecolumn = tablecolumn;
    }

}