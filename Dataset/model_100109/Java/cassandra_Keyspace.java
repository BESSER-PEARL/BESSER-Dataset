





import java.util.List;
import java.util.ArrayList;

public class cassandra_Keyspace  {

    private String name;



    public cassandra_Keyspace(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}