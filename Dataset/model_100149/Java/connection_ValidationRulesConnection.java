





import java.util.List;
import java.util.ArrayList;

public class connection_ValidationRulesConnection extends Connection {

    private String logicalOperator;
    private String refSchema;
    private boolean isDelete;
    private String baseColumnNames;
    private String refColumnNames;
    private boolean isInsert;
    private String baseSchema;
    private String javaCondition;
    private String type;
    private boolean isUpdate;
    private boolean isRejectLink;
    private boolean isDisallow;
    private boolean isSelect;
    private String sqlCondition;



    public connection_ValidationRulesConnection(
        String logicalOperator,        String refSchema,        boolean isDelete,        String baseColumnNames,        String refColumnNames,        boolean isInsert,        String baseSchema,        String javaCondition,        String type,        boolean isUpdate,        boolean isRejectLink,        boolean isDisallow,        boolean isSelect,        String sqlCondition    ) {
        super(
        );
        this.logicalOperator = logicalOperator;
        this.refSchema = refSchema;
        this.isDelete = isDelete;
        this.baseColumnNames = baseColumnNames;
        this.refColumnNames = refColumnNames;
        this.isInsert = isInsert;
        this.baseSchema = baseSchema;
        this.javaCondition = javaCondition;
        this.type = type;
        this.isUpdate = isUpdate;
        this.isRejectLink = isRejectLink;
        this.isDisallow = isDisallow;
        this.isSelect = isSelect;
        this.sqlCondition = sqlCondition;
    }


    public String getLogicaloperator() {
        return logicalOperator;
    }

    public void setLogicaloperator(String logicalOperator) {
        this.logicalOperator = logicalOperator;
    }
    public String getRefschema() {
        return refSchema;
    }

    public void setRefschema(String refSchema) {
        this.refSchema = refSchema;
    }
    public boolean getIsdelete() {
        return isDelete;
    }

    public void setIsdelete(boolean isDelete) {
        this.isDelete = isDelete;
    }
    public String getBasecolumnnames() {
        return baseColumnNames;
    }

    public void setBasecolumnnames(String baseColumnNames) {
        this.baseColumnNames = baseColumnNames;
    }
    public String getRefcolumnnames() {
        return refColumnNames;
    }

    public void setRefcolumnnames(String refColumnNames) {
        this.refColumnNames = refColumnNames;
    }
    public boolean getIsinsert() {
        return isInsert;
    }

    public void setIsinsert(boolean isInsert) {
        this.isInsert = isInsert;
    }
    public String getBaseschema() {
        return baseSchema;
    }

    public void setBaseschema(String baseSchema) {
        this.baseSchema = baseSchema;
    }
    public String getJavacondition() {
        return javaCondition;
    }

    public void setJavacondition(String javaCondition) {
        this.javaCondition = javaCondition;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getIsupdate() {
        return isUpdate;
    }

    public void setIsupdate(boolean isUpdate) {
        this.isUpdate = isUpdate;
    }
    public boolean getIsrejectlink() {
        return isRejectLink;
    }

    public void setIsrejectlink(boolean isRejectLink) {
        this.isRejectLink = isRejectLink;
    }
    public boolean getIsdisallow() {
        return isDisallow;
    }

    public void setIsdisallow(boolean isDisallow) {
        this.isDisallow = isDisallow;
    }
    public boolean getIsselect() {
        return isSelect;
    }

    public void setIsselect(boolean isSelect) {
        this.isSelect = isSelect;
    }
    public String getSqlcondition() {
        return sqlCondition;
    }

    public void setSqlcondition(String sqlCondition) {
        this.sqlCondition = sqlCondition;
    }


}