





import java.util.List;
import java.util.ArrayList;

public class mm_ops_AddIndex extends ModelOperation {

    private String name;
    private String columnsNames;
    private String owningTableName;
    private String owningSchemaName;



    public mm_ops_AddIndex(
        String name,        String columnsNames,        String owningTableName,        String owningSchemaName    ) {
        super(
        );
        this.name = name;
        this.columnsNames = columnsNames;
        this.owningTableName = owningTableName;
        this.owningSchemaName = owningSchemaName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getColumnsnames() {
        return columnsNames;
    }

    public void setColumnsnames(String columnsNames) {
        this.columnsNames = columnsNames;
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