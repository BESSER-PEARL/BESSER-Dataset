





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_FKey  {






    private List<Column> columns;


    public SimpleRDBMS_FKey(
    ) {
        this.columns = new ArrayList<>();
    }

    public SimpleRDBMS_FKey(
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