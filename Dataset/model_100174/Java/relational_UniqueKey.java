





import java.util.List;
import java.util.ArrayList;

public class relational_UniqueKey extends RelationalEntity {






    private List<relational_Column> relational_columns;




    private relational_Column relational_column;


    public relational_UniqueKey(
    ) {
        super(
        );
        this.relational_columns = new ArrayList<>();
    }

    public relational_UniqueKey(
        ArrayList<relational_Column> relational_columns    ) {
        this.relational_columns = relational_columns;
    }


    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }
    public relational_Column getRelational_column() {
        return relational_column;
    }

    public void setRelational_column(relational_Column relational_column) {
        this.relational_column = relational_column;
    }

}