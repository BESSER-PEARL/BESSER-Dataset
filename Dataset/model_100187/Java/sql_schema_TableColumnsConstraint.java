





import java.util.List;
import java.util.ArrayList;

public class sql_schema_TableColumnsConstraint extends TableConstraint {






    private List<Column> columns;


    public sql_schema_TableColumnsConstraint(
    ) {
        super(
        );
        this.columns = new ArrayList<>();
    }

    public sql_schema_TableColumnsConstraint(
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