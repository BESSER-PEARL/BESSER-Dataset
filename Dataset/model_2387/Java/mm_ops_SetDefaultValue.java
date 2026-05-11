





import java.util.List;
import java.util.ArrayList;

public class mm_ops_SetDefaultValue extends ModelOperation {

    private String owningSchemaName;
    private String owningTableName;
    private String newDefaultValue;
    private String owningColumnName;



    public mm_ops_SetDefaultValue(
        String owningSchemaName,        String owningTableName,        String newDefaultValue,        String owningColumnName    ) {
        super(
        );
        this.owningSchemaName = owningSchemaName;
        this.owningTableName = owningTableName;
        this.newDefaultValue = newDefaultValue;
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
    public String getNewdefaultvalue() {
        return newDefaultValue;
    }

    public void setNewdefaultvalue(String newDefaultValue) {
        this.newDefaultValue = newDefaultValue;
    }
    public String getOwningcolumnname() {
        return owningColumnName;
    }

    public void setOwningcolumnname(String owningColumnName) {
        this.owningColumnName = owningColumnName;
    }


}