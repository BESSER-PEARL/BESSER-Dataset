





import java.util.List;
import java.util.ArrayList;

public class mm_ops_HasNoOwnInstances extends ModelOperation {

    private String tableName;
    private String owningSchemaName;
    private String whereCondition;



    public mm_ops_HasNoOwnInstances(
        String tableName,        String owningSchemaName,        String whereCondition    ) {
        super(
        );
        this.tableName = tableName;
        this.owningSchemaName = owningSchemaName;
        this.whereCondition = whereCondition;
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
    public String getWherecondition() {
        return whereCondition;
    }

    public void setWherecondition(String whereCondition) {
        this.whereCondition = whereCondition;
    }


}