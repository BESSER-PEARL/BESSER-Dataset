





import java.util.List;
import java.util.ArrayList;

public class mm_ops_AddPrimaryKey extends ModelOperation {

    private String owningSchemaName;
    private String constrainedColumnName;
    private String owningTableName;
    private String name;



    public mm_ops_AddPrimaryKey(
        String owningSchemaName,        String constrainedColumnName,        String owningTableName,        String name    ) {
        super(
        );
        this.owningSchemaName = owningSchemaName;
        this.constrainedColumnName = constrainedColumnName;
        this.owningTableName = owningTableName;
        this.name = name;
    }


    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}