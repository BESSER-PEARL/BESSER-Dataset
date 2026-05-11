





import java.util.List;
import java.util.ArrayList;

public class mm_ops_SetColumnType extends ModelOperation {

    private String oldType;
    private String owningTableName;
    private String owningSchemaName;
    private String newType;
    private String owningColumnName;



    public mm_ops_SetColumnType(
        String oldType,        String owningTableName,        String owningSchemaName,        String newType,        String owningColumnName    ) {
        super(
        );
        this.oldType = oldType;
        this.owningTableName = owningTableName;
        this.owningSchemaName = owningSchemaName;
        this.newType = newType;
        this.owningColumnName = owningColumnName;
    }


    public String getOldtype() {
        return oldType;
    }

    public void setOldtype(String oldType) {
        this.oldType = oldType;
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
    public String getNewtype() {
        return newType;
    }

    public void setNewtype(String newType) {
        this.newType = newType;
    }
    public String getOwningcolumnname() {
        return owningColumnName;
    }

    public void setOwningcolumnname(String owningColumnName) {
        this.owningColumnName = owningColumnName;
    }


}