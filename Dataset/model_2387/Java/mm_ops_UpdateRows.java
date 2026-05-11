





import java.util.List;
import java.util.ArrayList;

public class mm_ops_UpdateRows extends ModelOperation {

    private String sourceTableName;
    private String sourceColumnName;
    private String whereCondition;
    private String owningSchemaName;
    private String targetTableName;
    private String targetColumnName;



    public mm_ops_UpdateRows(
        String sourceTableName,        String sourceColumnName,        String whereCondition,        String owningSchemaName,        String targetTableName,        String targetColumnName    ) {
        super(
        );
        this.sourceTableName = sourceTableName;
        this.sourceColumnName = sourceColumnName;
        this.whereCondition = whereCondition;
        this.owningSchemaName = owningSchemaName;
        this.targetTableName = targetTableName;
        this.targetColumnName = targetColumnName;
    }


    public String getSourcetablename() {
        return sourceTableName;
    }

    public void setSourcetablename(String sourceTableName) {
        this.sourceTableName = sourceTableName;
    }
    public String getSourcecolumnname() {
        return sourceColumnName;
    }

    public void setSourcecolumnname(String sourceColumnName) {
        this.sourceColumnName = sourceColumnName;
    }
    public String getWherecondition() {
        return whereCondition;
    }

    public void setWherecondition(String whereCondition) {
        this.whereCondition = whereCondition;
    }
    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }
    public String getTargettablename() {
        return targetTableName;
    }

    public void setTargettablename(String targetTableName) {
        this.targetTableName = targetTableName;
    }
    public String getTargetcolumnname() {
        return targetColumnName;
    }

    public void setTargetcolumnname(String targetColumnName) {
        this.targetColumnName = targetColumnName;
    }


}