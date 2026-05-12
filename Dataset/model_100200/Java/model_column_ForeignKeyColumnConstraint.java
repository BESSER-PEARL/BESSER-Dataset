





import java.util.List;
import java.util.ArrayList;

public class model_column_ForeignKeyColumnConstraint extends ColumnConstraint {






    private Column column;




    private Table table;


    public model_column_ForeignKeyColumnConstraint(
    ) {
        super(
        );
    }



    public Column getColumn() {
        return column;
    }

    public void setColumn(Column column) {
        this.column = column;
    }
    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}