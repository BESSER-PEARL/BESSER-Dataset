





import java.util.List;
import java.util.ArrayList;

public class relational_ColumnSet extends RelationalEntity {






    private relational_Column relational_column;




    private List<relational_Column> relational_columns;


    public relational_ColumnSet(
    ) {
        super(
        );
        this.relational_columns = new ArrayList<>();
    }

    public relational_ColumnSet(
        ArrayList<relational_Column> relational_columns    ) {
        this.relational_columns = relational_columns;
    }


    public relational_Column getRelational_column() {
        return relational_column;
    }

    public void setRelational_column(relational_Column relational_column) {
        this.relational_column = relational_column;
    }
    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }

}