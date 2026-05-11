





import java.util.List;
import java.util.ArrayList;

public class nosql_Options  {

    private String value;
    private String name;





    private nosql_ColumnFamily nosql_columnfamily;




    private nosql_KeySpace nosql_keyspace;




    private nosql_KeySpace nosql_keyspace;


    public nosql_Options(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nosql_ColumnFamily getNosql_columnfamily() {
        return nosql_columnfamily;
    }

    public void setNosql_columnfamily(nosql_ColumnFamily nosql_columnfamily) {
        this.nosql_columnfamily = nosql_columnfamily;
    }
    public nosql_KeySpace getNosql_keyspace() {
        return nosql_keyspace;
    }

    public void setNosql_keyspace(nosql_KeySpace nosql_keyspace) {
        this.nosql_keyspace = nosql_keyspace;
    }
    public nosql_KeySpace getNosql_keyspace() {
        return nosql_keyspace;
    }

    public void setNosql_keyspace(nosql_KeySpace nosql_keyspace) {
        this.nosql_keyspace = nosql_keyspace;
    }

}