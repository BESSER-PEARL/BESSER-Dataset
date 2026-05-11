





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RemoveIndex extends ModelOperation {

    private String name;
    private String owningSchemaName;



    public mm_ops_RemoveIndex(
        String name,        String owningSchemaName    ) {
        super(
        );
        this.name = name;
        this.owningSchemaName = owningSchemaName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }


}