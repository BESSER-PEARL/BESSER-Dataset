





import java.util.List;
import java.util.ArrayList;

public class mm_ops_AddUnique extends ModelOperation {

    private String constrainedColumnNames;
    private String name;
    private String owningTableName;
    private String owningSchemaName;



    public mm_ops_AddUnique(
        String constrainedColumnNames,        String name,        String owningTableName,        String owningSchemaName    ) {
        super(
        );
        this.constrainedColumnNames = constrainedColumnNames;
        this.name = name;
        this.owningTableName = owningTableName;
        this.owningSchemaName = owningSchemaName;
    }


    public String getConstrainedcolumnnames() {
        return constrainedColumnNames;
    }

    public void setConstrainedcolumnnames(String constrainedColumnNames) {
        this.constrainedColumnNames = constrainedColumnNames;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
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


}