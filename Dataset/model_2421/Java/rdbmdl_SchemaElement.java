





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_SchemaElement extends NamedElement {

    private String owner;





    private rdbmdl_Schema rdbmdl_schema;


    public rdbmdl_SchemaElement(
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

    public rdbmdl_Schema getRdbmdl_schema() {
        return rdbmdl_schema;
    }

    public void setRdbmdl_schema(rdbmdl_Schema rdbmdl_schema) {
        this.rdbmdl_schema = rdbmdl_schema;
    }

}