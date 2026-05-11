





import java.util.List;
import java.util.ArrayList;

public class rdb_SchemaElement extends NamedElement {

    private String owner;





    private rdb_Schema rdb_schema;


    public rdb_SchemaElement(
        String owner    ) {
        super(
        );
        this.owner = owner;
    }


    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public rdb_Schema getRdb_schema() {
        return rdb_schema;
    }

    public void setRdb_schema(rdb_Schema rdb_schema) {
        this.rdb_schema = rdb_schema;
    }

}