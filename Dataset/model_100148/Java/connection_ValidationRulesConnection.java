





import java.util.List;
import java.util.ArrayList;

public class connection_ValidationRulesConnection extends Connection {

    private boolean isDisallow;
    private String baseColumnNames;
    private boolean isDelete;
    private String logicalOperator;
    private boolean isUpdate;
    private boolean isRejectLink;
    private boolean isInsert;
    private boolean isSelect;
    private String javaCondition;
    private String refSchema;
    private String type;
    private String sqlCondition;
    private String refColumnNames;
    private String baseSchema;





    private List<connection_ConditionType> connection_conditiontypes;


    public connection_ValidationRulesConnection(
        boolean isDisallow,        String baseColumnNames,        boolean isDelete,        String logicalOperator,        boolean isUpdate,        boolean isRejectLink,        boolean isInsert,        boolean isSelect,        String javaCondition,        String refSchema,        String type,        String sqlCondition,        String refColumnNames,        String baseSchema    ) {
        super(
        );
        this.isDisallow = isDisallow;
        this.baseColumnNames = baseColumnNames;
        this.isDelete = isDelete;
        this.logicalOperator = logicalOperator;
        this.isUpdate = isUpdate;
        this.isRejectLink = isRejectLink;
        this.isInsert = isInsert;
        this.isSelect = isSelect;
        this.javaCondition = javaCondition;
        this.refSchema = refSchema;
        this.type = type;
        this.sqlCondition = sqlCondition;
        this.refColumnNames = refColumnNames;
        this.baseSchema = baseSchema;
        this.connection_conditiontypes = new ArrayList<>();
    }

    public connection_ValidationRulesConnection(
        boolean isDisallow,        String baseColumnNames,        boolean isDelete,        String logicalOperator,        boolean isUpdate,        boolean isRejectLink,        boolean isInsert,        boolean isSelect,        String javaCondition,        String refSchema,        String type,        String sqlCondition,        String refColumnNames,        String baseSchema        ArrayList<connection_ConditionType> connection_conditiontypes    ) {
        this.isDisallow = isDisallow;
        this.baseColumnNames = baseColumnNames;
        this.isDelete = isDelete;
        this.logicalOperator = logicalOperator;
        this.isUpdate = isUpdate;
        this.isRejectLink = isRejectLink;
        this.isInsert = isInsert;
        this.isSelect = isSelect;
        this.javaCondition = javaCondition;
        this.refSchema = refSchema;
        this.type = type;
        this.sqlCondition = sqlCondition;
        this.refColumnNames = refColumnNames;
        this.baseSchema = baseSchema;
        this.connection_conditiontypes = connection_conditiontypes;
    }

    public boolean getIsdisallow() {
        return isDisallow;
    }

    public void setIsdisallow(boolean isDisallow) {
        this.isDisallow = isDisallow;
    }
    public String getBasecolumnnames() {
        return baseColumnNames;
    }

    public void setBasecolumnnames(String baseColumnNames) {
        this.baseColumnNames = baseColumnNames;
    }
    public boolean getIsdelete() {
        return isDelete;
    }

    public void setIsdelete(boolean isDelete) {
        this.isDelete = isDelete;
    }
    public String getLogicaloperator() {
        return logicalOperator;
    }

    public void setLogicaloperator(String logicalOperator) {
        this.logicalOperator = logicalOperator;
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
    public boolean getIsinsert() {
        return isInsert;
    }

    public void setIsinsert(boolean isInsert) {
        this.isInsert = isInsert;
    }
    public boolean getIsselect() {
        return isSelect;
    }

    public void setIsselect(boolean isSelect) {
        this.isSelect = isSelect;
    }
    public String getJavacondition() {
        return javaCondition;
    }

    public void setJavacondition(String javaCondition) {
        this.javaCondition = javaCondition;
    }
    public String getRefschema() {
        return refSchema;
    }

    public void setRefschema(String refSchema) {
        this.refSchema = refSchema;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSqlcondition() {
        return sqlCondition;
    }

    public void setSqlcondition(String sqlCondition) {
        this.sqlCondition = sqlCondition;
    }
    public String getRefcolumnnames() {
        return refColumnNames;
    }

    public void setRefcolumnnames(String refColumnNames) {
        this.refColumnNames = refColumnNames;
    }
    public String getBaseschema() {
        return baseSchema;
    }

    public void setBaseschema(String baseSchema) {
        this.baseSchema = baseSchema;
    }

    public List<connection_ConditionType> getConnection_conditiontypes() {
        return connection_conditiontypes;
    }

    public void addConnection_conditiontype(Connection_conditiontype connection_conditiontype) {
        this.connection_conditiontypes.add(connection_conditiontype);
    }

}