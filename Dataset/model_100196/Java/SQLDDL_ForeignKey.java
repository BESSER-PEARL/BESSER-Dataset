





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_ForeignKey extends Key {






    private List<Column> columns;


    public SQLDDL_ForeignKey(
    ) {
        super(
        );
        this.columns = new ArrayList<>();
    }

    public SQLDDL_ForeignKey(
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