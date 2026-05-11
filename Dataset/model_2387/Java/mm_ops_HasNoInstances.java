





import java.util.List;
import java.util.ArrayList;

public class mm_ops_HasNoInstances extends ModelOperation {

    private String tableName;
    private String owningSchemaName;



    public mm_ops_HasNoInstances(
        String tableName,        String owningSchemaName    ) {
        super(
        );
        this.tableName = tableName;
        this.owningSchemaName = owningSchemaName;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }


}