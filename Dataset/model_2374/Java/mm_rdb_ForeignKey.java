





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_ForeignKey extends TableConstraint {






    private Table table;




    private TableColumn tablecolumn;


    public mm_rdb_ForeignKey(
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