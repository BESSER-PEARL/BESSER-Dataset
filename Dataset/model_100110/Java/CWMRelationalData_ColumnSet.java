





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_ColumnSet  {






    private List<Column> columns;


    public CWMRelationalData_ColumnSet(
    ) {
        this.columns = new ArrayList<>();
    }

    public CWMRelationalData_ColumnSet(
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