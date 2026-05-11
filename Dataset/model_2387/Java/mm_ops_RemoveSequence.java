





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RemoveSequence extends ModelOperation {

    private String owningSchemaName;
    private String name;



    public mm_ops_RemoveSequence(
        String owningSchemaName,        String name    ) {
        super(
        );
        this.owningSchemaName = owningSchemaName;
        this.name = name;
    }


    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}