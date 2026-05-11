





import java.util.List;
import java.util.ArrayList;

public class relational_Trigger extends SQLObject {

    private String condition;
    private String oldRow;
    private String statementSQL;
    private boolean updateType;
    private String newRow;
    private boolean insertType;
    private String oldTable;
    private String actionTime;
    private String newTable;
    private String actionGranularity;
    private boolean deleteType;





    private relational_Table relational_table;




    private List<relational_Table> relational_tables;




    private relational_Table relational_table;




    private relational_Table relational_table;


    public relational_Trigger(
        String condition,        String oldRow,        String statementSQL,        boolean updateType,        String newRow,        boolean insertType,        String oldTable,        String actionTime,        String newTable,        String actionGranularity,        boolean deleteType    ) {
        super(
        );
        this.condition = condition;
        this.oldRow = oldRow;
        this.statementSQL = statementSQL;
        this.updateType = updateType;
        this.newRow = newRow;
        this.insertType = insertType;
        this.oldTable = oldTable;
        this.actionTime = actionTime;
        this.newTable = newTable;
        this.actionGranularity = actionGranularity;
        this.deleteType = deleteType;
        this.relational_tables = new ArrayList<>();
    }

    public relational_Trigger(
        String condition,        String oldRow,        String statementSQL,        boolean updateType,        String newRow,        boolean insertType,        String oldTable,        String actionTime,        String newTable,        String actionGranularity,        boolean deleteType        ArrayList<relational_Table> relational_tables    ) {
        this.condition = condition;
        this.oldRow = oldRow;
        this.statementSQL = statementSQL;
        this.updateType = updateType;
        this.newRow = newRow;
        this.insertType = insertType;
        this.oldTable = oldTable;
        this.actionTime = actionTime;
        this.newTable = newTable;
        this.actionGranularity = actionGranularity;
        this.deleteType = deleteType;
        this.relational_tables = relational_tables;
    }

    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getOldrow() {
        return oldRow;
    }

    public void setOldrow(String oldRow) {
        this.oldRow = oldRow;
    }
    public String getStatementsql() {
        return statementSQL;
    }

    public void setStatementsql(String statementSQL) {
        this.statementSQL = statementSQL;
    }
    public boolean getUpdatetype() {
        return updateType;
    }

    public void setUpdatetype(boolean updateType) {
        this.updateType = updateType;
    }
    public String getNewrow() {
        return newRow;
    }

    public void setNewrow(String newRow) {
        this.newRow = newRow;
    }
    public boolean getInserttype() {
        return insertType;
    }

    public void setInserttype(boolean insertType) {
        this.insertType = insertType;
    }
    public String getOldtable() {
        return oldTable;
    }

    public void setOldtable(String oldTable) {
        this.oldTable = oldTable;
    }
    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }
    public String getNewtable() {
        return newTable;
    }

    public void setNewtable(String newTable) {
        this.newTable = newTable;
    }
    public String getActiongranularity() {
        return actionGranularity;
    }

    public void setActiongranularity(String actionGranularity) {
        this.actionGranularity = actionGranularity;
    }
    public boolean getDeletetype() {
        return deleteType;
    }

    public void setDeletetype(boolean deleteType) {
        this.deleteType = deleteType;
    }

    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public List<relational_Table> getRelational_tables() {
        return relational_tables;
    }

    public void addRelational_table(Relational_table relational_table) {
        this.relational_tables.add(relational_table);
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}