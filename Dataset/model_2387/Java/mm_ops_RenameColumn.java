





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RenameColumn extends ModelOperation {

    private String owningTableName;
    private String name;
    private String owningSchemaName;
    private String newName;



    public mm_ops_RenameColumn(
        String owningTableName,        String name,        String owningSchemaName,        String newName    ) {
        super(
        );
        this.owningTableName = owningTableName;
        this.name = name;
        this.owningSchemaName = owningSchemaName;
        this.newName = newName;
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
    public String getNewname() {
        return newName;
    }

    public void setNewname(String newName) {
        this.newName = newName;
    }


}