





import java.util.List;
import java.util.ArrayList;

public class MySQL_ForeignColumn extends Column {






    private Table table;


    public MySQL_ForeignColumn(
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

}