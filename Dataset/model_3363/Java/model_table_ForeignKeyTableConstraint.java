





import java.util.List;
import java.util.ArrayList;

public class model_table_ForeignKeyTableConstraint extends TableConstraint {






    private Table table;




    private List<Column> columns;




    private List<Column> columns;


    public model_table_ForeignKeyTableConstraint(
    ) {
        super(
        );
        this.columns = new ArrayList<>();
        this.columns = new ArrayList<>();
    }

    public model_table_ForeignKeyTableConstraint(
        ArrayList<Column> columns,        ArrayList<Column> columns    ) {
        this.columns = columns;
        this.columns = columns;
    }


    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }
    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }
    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }

}