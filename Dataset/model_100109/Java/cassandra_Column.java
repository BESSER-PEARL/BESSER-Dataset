





import java.util.List;
import java.util.ArrayList;

public class cassandra_Column  {

    private String key;
    private String timestamp;





    private cassandra_Row cassandra_row;




    private cassandra_SuperColumn cassandra_supercolumn;


    public cassandra_Column(
        String key,        String timestamp    ) {
        this.key = key;
        this.timestamp = timestamp;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public cassandra_Row getCassandra_row() {
        return cassandra_row;
    }

    public void setCassandra_row(cassandra_Row cassandra_row) {
        this.cassandra_row = cassandra_row;
    }
    public cassandra_SuperColumn getCassandra_supercolumn() {
        return cassandra_supercolumn;
    }

    public void setCassandra_supercolumn(cassandra_SuperColumn cassandra_supercolumn) {
        this.cassandra_supercolumn = cassandra_supercolumn;
    }

}