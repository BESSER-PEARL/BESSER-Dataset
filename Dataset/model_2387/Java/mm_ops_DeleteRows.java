





import java.util.List;
import java.util.ArrayList;

public class mm_ops_DeleteRows extends ModelOperation {

    private String owningSchemaName;
    private String tableName;
    private String whereCondition;



    public mm_ops_DeleteRows(
        String owningSchemaName,        String tableName,        String whereCondition    ) {
        super(
        );
        this.owningSchemaName = owningSchemaName;
        this.tableName = tableName;
        this.whereCondition = whereCondition;
    }


    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getWherecondition() {
        return whereCondition;
    }

    public void setWherecondition(String whereCondition) {
        this.whereCondition = whereCondition;
    }


}