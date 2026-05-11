





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RemoveConstraint extends ModelOperation {

    private String owningTableName;
    private String owningSchemaName;
    private String name;



    public mm_ops_RemoveConstraint(
        String owningTableName,        String owningSchemaName,        String name    ) {
        super(
        );
        this.owningTableName = owningTableName;
        this.owningSchemaName = owningSchemaName;
        this.name = name;
    }


    public String getOwningtablename() {
        return owningTableName;
    }

    public void setOwningtablename(String owningTableName) {
        this.owningTableName = owningTableName;
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