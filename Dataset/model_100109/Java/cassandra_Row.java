





import java.util.List;
import java.util.ArrayList;

public class cassandra_Row  {

    private String key;





    private cassandra_ColumnFamily cassandra_columnfamily;




    private List<cassandra_SuperColumn> cassandra_supercolumns;


    public cassandra_Row(
        String key    ) {
        this.key = key;
        this.cassandra_supercolumns = new ArrayList<>();
    }

    public cassandra_Row(
        String key        ArrayList<cassandra_SuperColumn> cassandra_supercolumns    ) {
        this.key = key;
        this.cassandra_supercolumns = cassandra_supercolumns;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public cassandra_ColumnFamily getCassandra_columnfamily() {
        return cassandra_columnfamily;
    }

    public void setCassandra_columnfamily(cassandra_ColumnFamily cassandra_columnfamily) {
        this.cassandra_columnfamily = cassandra_columnfamily;
    }
    public List<cassandra_SuperColumn> getCassandra_supercolumns() {
        return cassandra_supercolumns;
    }

    public void addCassandra_supercolumn(Cassandra_supercolumn cassandra_supercolumn) {
        this.cassandra_supercolumns.add(cassandra_supercolumn);
    }

}