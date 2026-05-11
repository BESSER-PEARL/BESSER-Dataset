





import java.util.List;
import java.util.ArrayList;

public class Relational_Table extends Named {






    private List<Column> columns;




    private List<Column> columns;


    public Relational_Table(
    ) {
        super(
        );
        this.columns = new ArrayList<>();
        this.columns = new ArrayList<>();
    }

    public Relational_Table(
        ArrayList<Column> columns,        ArrayList<Column> columns    ) {
        this.columns = columns;
        this.columns = columns;
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