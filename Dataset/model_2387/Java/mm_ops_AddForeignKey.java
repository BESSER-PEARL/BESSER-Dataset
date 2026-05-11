





import java.util.List;
import java.util.ArrayList;

public class mm_ops_AddForeignKey extends ModelOperation {

    private String name;
    private String owningSchemaName;
    private String targetTableName;
    private String constrainedColumnName;
    private String owningTableName;



    public mm_ops_AddForeignKey(
        String name,        String owningSchemaName,        String targetTableName,        String constrainedColumnName,        String owningTableName    ) {
        super(
        );
        this.name = name;
        this.owningSchemaName = owningSchemaName;
        this.targetTableName = targetTableName;
        this.constrainedColumnName = constrainedColumnName;
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
    public String getTargettablename() {
        return targetTableName;
    }

    public void setTargettablename(String targetTableName) {
        this.targetTableName = targetTableName;
    }
    public String getConstrainedcolumnname() {
        return constrainedColumnName;
    }

    public void setConstrainedcolumnname(String constrainedColumnName) {
        this.constrainedColumnName = constrainedColumnName;
    }
    public String getOwningtablename() {
        return owningTableName;
    }

    public void setOwningtablename(String owningTableName) {
        this.owningTableName = owningTableName;
    }


}