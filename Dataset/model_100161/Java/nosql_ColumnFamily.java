





import java.util.List;
import java.util.ArrayList;

public class nosql_ColumnFamily  {

    private String name;





    private nosql_KeySpace nosql_keyspace;




    private List<nosql_Column> nosql_columns;




    private List<nosql_Column> nosql_columns;




    private nosql_KeySpace nosql_keyspace;


    public nosql_ColumnFamily(
        String name    ) {
        this.name = name;
        this.nosql_columns = new ArrayList<>();
        this.nosql_columns = new ArrayList<>();
    }

    public nosql_ColumnFamily(
        String name        ArrayList<nosql_Column> nosql_columns,        ArrayList<nosql_Column> nosql_columns    ) {
        this.name = name;
        this.nosql_columns = nosql_columns;
        this.nosql_columns = nosql_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nosql_KeySpace getNosql_keyspace() {
        return nosql_keyspace;
    }

    public void setNosql_keyspace(nosql_KeySpace nosql_keyspace) {
        this.nosql_keyspace = nosql_keyspace;
    }
    public List<nosql_Column> getNosql_columns() {
        return nosql_columns;
    }

    public void addNosql_column(Nosql_column nosql_column) {
        this.nosql_columns.add(nosql_column);
    }
    public List<nosql_Column> getNosql_columns() {
        return nosql_columns;
    }

    public void addNosql_column(Nosql_column nosql_column) {
        this.nosql_columns.add(nosql_column);
    }
    public nosql_KeySpace getNosql_keyspace() {
        return nosql_keyspace;
    }

    public void setNosql_keyspace(nosql_KeySpace nosql_keyspace) {
        this.nosql_keyspace = nosql_keyspace;
    }

}