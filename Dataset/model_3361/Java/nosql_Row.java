





import java.util.List;
import java.util.ArrayList;

public class nosql_Row extends ColumnFamily {






    private List<nosql_Column> nosql_columns;




    private nosql_ColumnFamily nosql_columnfamily;


    public nosql_Row(
    ) {
        super(
        );
        this.nosql_columns = new ArrayList<>();
    }

    public nosql_Row(
        ArrayList<nosql_Column> nosql_columns    ) {
        this.nosql_columns = nosql_columns;
    }


    public List<nosql_Column> getNosql_columns() {
        return nosql_columns;
    }

    public void addNosql_column(Nosql_column nosql_column) {
        this.nosql_columns.add(nosql_column);
    }
    public nosql_ColumnFamily getNosql_columnfamily() {
        return nosql_columnfamily;
    }

    public void setNosql_columnfamily(nosql_ColumnFamily nosql_columnfamily) {
        this.nosql_columnfamily = nosql_columnfamily;
    }

}