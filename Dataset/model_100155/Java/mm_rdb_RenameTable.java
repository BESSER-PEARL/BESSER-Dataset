





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_RenameTable extends Operation {

    private String newName;





    private Table table;


    public mm_rdb_RenameTable(
        String newName    ) {
        super(
        );
        this.newName = newName;
    }


    public String getNewname() {
        return newName;
    }

    public void setNewname(String newName) {
        this.newName = newName;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}