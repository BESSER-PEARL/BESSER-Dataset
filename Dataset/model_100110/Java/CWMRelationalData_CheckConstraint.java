





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_CheckConstraint  {






    private List<Column> columns;




    private List<Table> tables;


    public CWMRelationalData_CheckConstraint(
    ) {
        this.columns = new ArrayList<>();
        this.tables = new ArrayList<>();
    }

    public CWMRelationalData_CheckConstraint(
        ArrayList<Column> columns,        ArrayList<Table> tables    ) {
        this.columns = columns;
        this.tables = tables;
    }


    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }
    public List<Table> getTables() {
        return tables;
    }

    public void addTable(Table table) {
        this.tables.add(table);
    }

}