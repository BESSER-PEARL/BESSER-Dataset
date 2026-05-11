





import java.util.List;
import java.util.ArrayList;

public class mm_ops_InsertRows extends ModelOperation {

    private String sourceTableName;
    private String targetTableName;
    private String targetColumnNames;
    private String whereCondition;
    private String owningSchemaName;
    private String sourceColumnsNames;



    public mm_ops_InsertRows(
        String sourceTableName,        String targetTableName,        String targetColumnNames,        String whereCondition,        String owningSchemaName,        String sourceColumnsNames    ) {
        super(
        );
        this.sourceTableName = sourceTableName;
        this.targetTableName = targetTableName;
        this.targetColumnNames = targetColumnNames;
        this.whereCondition = whereCondition;
        this.owningSchemaName = owningSchemaName;
        this.sourceColumnsNames = sourceColumnsNames;
    }


    public String getSourcetablename() {
        return sourceTableName;
    }

    public void setSourcetablename(String sourceTableName) {
        this.sourceTableName = sourceTableName;
    }
    public String getTargettablename() {
        return targetTableName;
    }

    public void setTargettablename(String targetTableName) {
        this.targetTableName = targetTableName;
    }
    public String getTargetcolumnnames() {
        return targetColumnNames;
    }

    public void setTargetcolumnnames(String targetColumnNames) {
        this.targetColumnNames = targetColumnNames;
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
    public String getSourcecolumnsnames() {
        return sourceColumnsNames;
    }

    public void setSourcecolumnsnames(String sourceColumnsNames) {
        this.sourceColumnsNames = sourceColumnsNames;
    }


}