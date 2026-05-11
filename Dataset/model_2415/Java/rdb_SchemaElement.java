





import java.util.List;
import java.util.ArrayList;

public class rdb_SchemaElement extends NamedElement {

    private String owner;



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


}