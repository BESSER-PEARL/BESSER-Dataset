





import java.util.List;
import java.util.ArrayList;

public class mm_ops_AddColumn extends ModelOperation {

    private String name;
    private String owningTableName;
    private String owningSchemaName;
    private String defaultValue;
    private String type;



    public mm_ops_AddColumn(
        String name,        String owningTableName,        String owningSchemaName,        String defaultValue,        String type    ) {
        super(
        );
        this.name = name;
        this.owningTableName = owningTableName;
        this.owningSchemaName = owningSchemaName;
        this.defaultValue = defaultValue;
        this.type = type;
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}