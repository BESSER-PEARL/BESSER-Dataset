





import java.util.List;
import java.util.ArrayList;

public class rdb_Table  {

    private String name;





    private rdb_Schema rdb_schema;


    public rdb_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdb_Schema getRdb_schema() {
        return rdb_schema;
    }

    public void setRdb_schema(rdb_Schema rdb_schema) {
        this.rdb_schema = rdb_schema;
    }

}