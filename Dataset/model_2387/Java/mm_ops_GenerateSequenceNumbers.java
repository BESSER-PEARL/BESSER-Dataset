





import java.util.List;
import java.util.ArrayList;

public class mm_ops_GenerateSequenceNumbers extends ModelOperation {

    private String tableName;
    private String owningSchemaName;
    private String columnName;
    private String sequenceName;



    public mm_ops_GenerateSequenceNumbers(
        String tableName,        String owningSchemaName,        String columnName,        String sequenceName    ) {
        super(
        );
        this.tableName = tableName;
        this.owningSchemaName = owningSchemaName;
        this.columnName = columnName;
        this.sequenceName = sequenceName;
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
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getSequencename() {
        return sequenceName;
    }

    public void setSequencename(String sequenceName) {
        this.sequenceName = sequenceName;
    }


}