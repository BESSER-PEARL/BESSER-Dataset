





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RemoveNotNull extends ModelOperation {

    private String owningSchemaName;
    private String constrainedColumnName;
    private String owningTableName;



    public mm_ops_RemoveNotNull(
        String owningSchemaName,        String constrainedColumnName,        String owningTableName    ) {
        super(
        );
        this.owningSchemaName = owningSchemaName;
        this.constrainedColumnName = constrainedColumnName;
        this.owningTableName = owningTableName;
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


}