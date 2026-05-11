





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RemoveDefaultValue extends ModelOperation {

    private String owningSchemaName;
    private String owningTableName;
    private String owningColumnName;



    public mm_ops_RemoveDefaultValue(
        String owningSchemaName,        String owningTableName,        String owningColumnName    ) {
        super(
        );
        this.owningSchemaName = owningSchemaName;
        this.owningTableName = owningTableName;
        this.owningColumnName = owningColumnName;
    }


    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }
    public String getOwningtablename() {
        return owningTableName;
    }

    public void setOwningtablename(String owningTableName) {
        this.owningTableName = owningTableName;
    }
    public String getOwningcolumnname() {
        return owningColumnName;
    }

    public void setOwningcolumnname(String owningColumnName) {
        this.owningColumnName = owningColumnName;
    }


}