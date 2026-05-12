





import java.util.List;
import java.util.ArrayList;

public class nosql_DynamicColumnFamily extends ColumnFamily {






    private List<nosql_Column> nosql_columns;


    public nosql_DynamicColumnFamily(
    ) {
        super(
        );
        this.nosql_columns = new ArrayList<>();
    }

    public nosql_DynamicColumnFamily(
        ArrayList<nosql_Column> nosql_columns    ) {
        this.nosql_columns = nosql_columns;
    }


    public List<nosql_Column> getNosql_columns() {
        return nosql_columns;
    }

    public void addNosql_column(Nosql_column nosql_column) {
        this.nosql_columns.add(nosql_column);
    }

}