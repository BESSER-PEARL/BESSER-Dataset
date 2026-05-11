





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RemoveColumn extends ModelOperation {

    private String owningTableName;
    private String name;
    private String owningSchemaName;



    public mm_ops_RemoveColumn(
        String owningTableName,        String name,        String owningSchemaName    ) {
        super(
        );
        this.owningTableName = owningTableName;
        this.name = name;
        this.owningSchemaName = owningSchemaName;
    }


    public String getOwningtablename() {
        return owningTableName;
    }

    public void setOwningtablename(String owningTableName) {
        this.owningTableName = owningTableName;
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