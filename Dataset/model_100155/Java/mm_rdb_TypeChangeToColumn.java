





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_TypeChangeToColumn extends Operation {

    private String newType;





    private Table table;




    private TableColumn tablecolumn;


    public mm_rdb_TypeChangeToColumn(
        String newType    ) {
        super(
        );
        this.newType = newType;
    }


    public String getNewtype() {
        return newType;
    }

    public void setNewtype(String newType) {
        this.newType = newType;
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