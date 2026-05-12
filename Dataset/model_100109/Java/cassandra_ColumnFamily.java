





import java.util.List;
import java.util.ArrayList;

public class cassandra_ColumnFamily  {

    private String name;





    private cassandra_Keyspace cassandra_keyspace;


    public cassandra_ColumnFamily(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cassandra_Keyspace getCassandra_keyspace() {
        return cassandra_keyspace;
    }

    public void setCassandra_keyspace(cassandra_Keyspace cassandra_keyspace) {
        this.cassandra_keyspace = cassandra_keyspace;
    }

}