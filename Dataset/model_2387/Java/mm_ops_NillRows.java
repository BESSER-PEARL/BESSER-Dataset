





import java.util.List;
import java.util.ArrayList;

public class mm_ops_NillRows extends ModelOperation {

    private String owningSchemaName;
    private String columnName;
    private String tableName;
    private String whereCondition;



    public mm_ops_NillRows(
        String owningSchemaName,        String columnName,        String tableName,        String whereCondition    ) {
        super(
        );
        this.owningSchemaName = owningSchemaName;
        this.columnName = columnName;
        this.tableName = tableName;
        this.whereCondition = whereCondition;
    }


    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
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