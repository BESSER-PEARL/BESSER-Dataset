





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Unique extends TableConstraint {






    private List<Column> columns;


    public mm_rdb_Unique(
    ) {
        super(
        );
        this.columns = new ArrayList<>();
    }

    public mm_rdb_Unique(
        ArrayList<Column> columns    ) {
        this.columns = columns;
    }


    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }

}