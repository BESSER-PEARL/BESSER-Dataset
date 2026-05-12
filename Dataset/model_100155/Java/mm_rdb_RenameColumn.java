





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_RenameColumn extends Operation {

    private String newColumnName;





    private TableColumn tablecolumn;




    private Table table;


    public mm_rdb_RenameColumn(
        String newColumnName    ) {
        super(
        );
        this.newColumnName = newColumnName;
    }


    public String getNewcolumnname() {
        return newColumnName;
    }

    public void setNewcolumnname(String newColumnName) {
        this.newColumnName = newColumnName;
    }

    public TableColumn getTablecolumn() {
        return tablecolumn;
    }

    public void setTablecolumn(TableColumn tablecolumn) {
        this.tablecolumn = tablecolumn;
    }
    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}